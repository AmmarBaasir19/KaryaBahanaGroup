import pandas as pd 
import numpy as np 
import streamlit as st 
from SrcNew.GenerateReports.StylingReports import StylingReports
from SrcNew.GenerateReports.Controller.DataPreprocessingReports import DataPreprocessingReports
from SrcNew.GenerateReports.Model.GenerateReportsWeekly import GenerateReportsWeekly
from SrcNew.GenerateReports.Model.GenerateReportsbyShift import GenerateReportsbyShift
from SrcNew.GenerateReports.Controller.ControllerReports import ControllerReports
from SrcNew.GenerateReports.Model.YieldCalculation import YieldCalculation

class MainAutomaticReports:
    def _remove_duplicated(self, df: pd.DataFrame, columns: list) -> pd.DataFrame:
        try :  
            mask = df.duplicated(subset=[columns], keep='first')
            df.loc[mask, columns] = np.nan

            return df
        
        except Exception as e : 
            print(f"Error in class MainPageReports (remove_duplicated) : {e}")
    
    def _remove_multiple_duplicates(self, df: pd.DataFrame, columns: list):
        try : 
            for col in columns:
                df = self._remove_duplicated(df, col) 
            return df
        
        except Exception as e : 
            print(f"Error in class MainPageReports (_remove_multiple_duplicates) : {e}")
    
    def run(self, df1: pd.DataFrame, df2: pd.DataFrame, option: str, start_date: pd.to_datetime, end_date: pd.to_datetime) -> pd.DataFrame:
        try : 
            df1, df2 = DataPreprocessingReports().run(df1, df2)
            st.write(f"Ini After DataPreprocessingReports : ")
            st.dataframe(df1) 
            st.dataframe(df2) 

            df_ctrl = ControllerReports().run(df1, df2, start_date, end_date)
            st.write(f"Ini After df_ctrl : ")
            st.dataframe(df_ctrl)
            print(f"Ini df_ctrl info : {df_ctrl.info()}")

            df_yield = YieldCalculation().run(df_ctrl) 
            st.write(f"Ini After df_yield : ")
            st.dataframe(df_yield)  

            if option == 'Format 1':
                df_reports = GenerateReportsWeekly().run(df_ctrl)

                df_reports = pd.merge(df_reports, df_yield, on=['Model', 'Part Name', 'Process'], how='left')
                df_reports = self._remove_multiple_duplicates(df_reports, [
                    'Model', 'Part Name', 'Final Yield / Line', 'First Pass Yield / Line', 'GAP (FY - FPY)'
                ])
                df_reports.drop(columns=['Detail_Date', 'index'], inplace=True)

                #wb = StylingReports().run(df_reports, 1, len(df_reports.columns) - 3, 4, len(df_reports.columns) + 1, option)

            else : 
                df_reports = GenerateReportsbyShift().run(df_ctrl).reset_index()
                #st.write(f"Ini After df_reports : ")
                #st.dataframe(df_reports)  

                df_yield.columns = pd.MultiIndex.from_tuples([
                    ("Model", "", ""),
                    ("Part Name", "", ""), 
                    ("Detail_Date", "", ""),
                    ("Final Yield / Line", "", ""),
                    ("First Pass Yield / Line", "", ""),
                    ("GAP (FY - FPY)", "", ""), 
                    ("Process", "", "")
                ])

                df_reports = pd.merge(
                    df_reports, df_yield,
                    on=[('Model', '', ''), ('Part Name', '', ''), ('Process', '', '')],
                    how='inner'
                )

                df_reports.drop(columns=[('Detail_Date', '', '')], inplace=True)
                df_reports = self._remove_multiple_duplicates(df_reports, [
                    ('Model', '', ''), ('Part Name', '', ''),
                    ('Final Yield / Line', '', ''), ('First Pass Yield / Line', '', ''), ('GAP (FY - FPY)', '', '')
                ])

                #wb = StylingReports().run(df_reports, 1, len(df_reports.columns) - 3, 4, len(df_reports.columns) + 1, option)

            return df_reports  
        
        except Exception as e :  
            st.error(f"Error in class MainAutomaticReports (run) : {e}")