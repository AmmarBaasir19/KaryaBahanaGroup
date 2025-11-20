import pandas as pd 
import numpy as np
import streamlit as st  

class GenerateReportsbyShift:
    def __init__(self):
        """ Define Default Values"""
        self.id_vars_column = ['Model', 'Part Name', 'Shift', 'Bulan', 'Tanggal', 'Detail_Date']
        self.value_vars_column = ['Qty Checked', 'First Pass Def', 'Final Def']
        self.pivot_index = ['Model', 'Part Name', 'Process', 'Detail_Date']
        self.pivot_column = ['Bulan', 'Tanggal', 'Shift']

    def melt_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """ """
        try : 
            return pd.melt(
                df,
                id_vars=['Model', 'Part Name', 'Shift', 'Bulan', 'Tanggal', 'Detail_Date'],
                value_vars=['Qty Checked', 'First Pass Def', 'Final Def'],
                var_name='Process',
                value_name='Value',
                ignore_index=True
            )
        
        except Exception as e : 
            st.error(f"Error in class GenerateReportsbyShift (melt_data) : {e}")
    
    def pivot_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """"""
        try : 
            return df.pivot(index=self.pivot_index,
                            columns=self.pivot_column,
                            values='Value')
        
        except Exception as e : 
            st.error(f"Error in class GenerateReportsbyShift (pivot_data) : {e}") 
    
    def pivot_table(self, df: pd.DataFrame) -> pd.DataFrame:
        """"""
        try : 
            return df.pivot_table(index=self.pivot_index,
                                  columns=self.pivot_column,
                                  values='Value',
                                  aggfunc='sum')
        
        except Exception as e : 
            st.error(f"Error in class GenerateReportsbyShift (pivot_data) : {e}") 
    
    def ordered_values(self, df: pd.DataFrame) -> pd.DataFrame:
        try : 
            df = df.reset_index()
            df['Process'] = pd.Categorical(
                df['Process'],
                categories=['Qty Checked', 'First Pass Def', 'Final Def'],
                ordered=True
            )
            
            df = df.sort_values(['Model', 'Part Name', 'Process'])
            return df.set_index(['Model', 'Part Name', 'Process'])
        
        except Exception as e : 
            st.error(f"Error in class GenerateReportsby_Shift (ordered_values) : {e}") 

    def sum_total(self, df: pd.DataFrame) -> pd.DataFrame:
        try : 
            return (
                df.assign(**{
                    f"Periode : {df['Detail_Date'].unique()[0]}": df.filter(like='Shift').sum(axis=1)
                })
                .drop(columns='Detail_Date', level='Bulan')
            )
        
        except Exception as e : 
            st.error(f"Error in class GenerateReportsbyShift (sum_total) : {e}")  
    
    def run(self, df: pd.DataFrame) -> pd.DataFrame:
        try : 
            df = self.melt_data(df)
            df = self.pivot_table(df)
            df = self.ordered_values(df)
            
            return self.sum_total(df)
        
        except Exception as e : 
            st.error(f"Error in class GenerateReportsbyShift (run) : {e}")