import pandas as pd 
import streamlit as st 

class GenerateReportsWeekly : 
    def groupby(self, df: pd.DataFrame) -> pd.DataFrame:
        try : 
            return (
                df.groupby(['Model', 'Part Name', 'Bulan', 'Detail_Date'], as_index=False)[
                    ['Qty Checked', 'First Pass Def', 'Final Def']
                ].sum()
            )
        
        except Exception as e : 
            st.error(f"Error in class GenerateReportsWeekly (groupby) : {e}")
    
    def melt_data(self, df: pd.DataFrame) -> pd.DataFrame: 
        try : 
            periode = df['Detail_Date'].iat[0] if not df.empty else "Unknown"

            return pd.melt(
                df, 
                id_vars=['Model', 'Part Name'],
                value_vars=['Qty Checked', 'First Pass Def', 'Final Def'],
                var_name='Process',
                value_name=f"Periode : {periode}"
            )
        
        except Exception as e : 
            st.error(f"Error in class GenerateReportsWeekly (melt_data) : {e}")
    
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
            st.error(f"Error in class GenerateReportsWeekly (ordered_values) : {e}") 
    
    def run(self, df: pd.DataFrame) -> pd.DataFrame:
        try : 
            return self.ordered_values(
                self.melt_data(
                    self.groupby(df)
                )
            )
        
        except Exception as e : 
            st.error(f"Error in class GenerateReportsWeekly (run) : {e}") 