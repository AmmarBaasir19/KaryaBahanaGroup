import pandas as pd 
import numpy as np
import streamlit as st 

class DataPreprocessingReports:
    def __init__(self):
        """" Define Default Values"""
        self.columns_data1_int = [
            'Qty Checked', 'Ok', 'Final Def', 'Scrap', 'Tahun', 'Bulan', 'Tanggal', 'Shift'
        ]
        self.columns_data2_int = [
            'Shift', 'Tahun', 'Bulan', 'Tanggal',
            'First Pass Def'
        ] 
        self.columns_data1_str = ['Model', 'Part No', 'Part Name'] 
        self.columns_data2_str = ['Model', 'Part No', 'Part Name']
        #self.filter_data1 = ['Model', 'Checked', 'Ok', 'Reapir', 'Scrap', 'Part No', 'Part Name', 'Tahun', 'Bulan', 'Tanggal', 'Shift']
        #self.filter_data2 = ['Model', 'Part No', 'Part Name', 'Shift', 'Tahun', 'Bulan', 'Tanggal', 'Total Repair', 'Total Top', 'Total Middle', 'Total Bottom']

    def change_columns_name(self, df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        """ Rename Columns Name (Set Style Title)"""
        df1 = df1.rename(str.title, axis=1)
        df2 = df2.rename(str.title, axis=1)
        df1.columns = df1.columns.str.replace('_', ' ')
        df2.columns = df2.columns.str.replace('_', ' ')
        return df1, df2

    def rename_columns(self, df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        """ Rename Columns Name"""
        try : 
            df1 = df1.rename(columns={'Checked': 'Qty Checked', 'Repair': 'Final Def'})
            df2 = df2.rename(columns={'Total Repair': 'First Pass Def'})

            return df1, df2
        
        except Exception as e :
            print(f"Error in class DataPreprocessingReports (rename_columns) : {e}")
    
    def wrangling_data(self, df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        """ Drop Specific Columns and Replace Values"""
        try : 
            df2['Total_Middle'] = df2['Total_Middle'].replace('-', 0)
            return df1, df2

        except Exception as e : 
            print(f"Error in class DataPreprocessingReports (wrangling_data) : {e}")
    
    def drop_duplicated(self, df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        """ Drop Duplicated Values"""
        try :
            df1 = df1.replace('', pd.NA).replace(' ', pd.NA)
            df2 = df2.replace('', pd.NA).replace(' ', pd.NA)
            df1 = df1.dropna(subset=['Model', 'Part Name', 'Part No', 'Shift', 'Tahun', 'Bulan', 'Tanggal'])
            df2 = df2.dropna(subset=['Model', 'Part Name', 'Part No', 'Shift', 'Tahun', 'Bulan', 'Tanggal']) 
            return df1, df2
        
        except Exception as e : 
            print(f"Error in class DataPreprocessingReports (drop_duplicated) : {e}")
    
    def change_data_type(self, df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        """ Change Data Type in Specific Columns"""
        try : 
            df1['Qty Checked'] = df1['Qty Checked'].fillna(0).astype(int)
            df1['Ok'] = df1['Ok'].fillna(0).astype(int)
            df1['Final Def'] = df1['Final Def'].fillna(0).astype(int)
            df1['Scrap'] = df1['Scrap'].fillna(0).astype(int)
            df2['First Pass Def'] = df2['First Pass Def'].fillna(0).astype(int)

            df1[self.columns_data1_int] = df1[self.columns_data1_int].astype('int64')
            df1[self.columns_data1_str] = df1[self.columns_data1_str].astype(str)
            df2[self.columns_data2_int] = df2[self.columns_data2_int].astype('int64') 
            df2[self.columns_data2_str] = df2[self.columns_data2_str].astype(str)

            return df1, df2

        except Exception as e : 
            print(f"Error in class DataPreprocessingReports (change_data_type) : {e}")
    
    def run(self, df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        """ Processing Several Function in Class DataPreprocessingReports"""
        try : 
            df1, df2 = self.change_columns_name(df1, df2)

            df1, df2 = self.rename_columns(df1, df2)

            #df1, df2 = self.wrangling_data(df1, df2)
            #print(f"Ini setelah wrangling df1 : {df1})")
            #print(f"Ini setelah wrangling df2 : {df1})")

            df1, df2 = self.drop_duplicated(df1, df2)

            df1, df2 = self.change_data_type(df1, df2) 

            return df1, df2

        except Exception as e : 
            st.error(f"Error in class DataPreprocessingReports (run) : {e}")  