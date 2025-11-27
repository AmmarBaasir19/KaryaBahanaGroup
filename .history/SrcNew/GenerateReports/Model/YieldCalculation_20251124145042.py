import pandas as pd 
import numpy as np 

class YieldCalculation: 
    def groupby_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """ Groupby Data with Specific Columns and Specific Aggregation"""
        try : 
            return (df.groupby(['Model', 'Part Name', 'Bulan', 'Detail_Date'])[['Qty Checked', 'First Pass Def', 'Final Def']].sum().reset_index())
        
        except Exception as e : 
            print(f"Error in class YieldCalculation (groupby_data) : {e}")
    
    def yield_generations(self, df: pd.DataFrame) -> pd.DataFrame: 
        """ Calculate Yield in Final Def, and First Pass Def"""
        try : 
            df['Final Yield / Line'] = (((df['Qty Checked'] - df['Final Def'])/df['Qty Checked'].replace(0, pd.NA)) * 100).fillna(0).astype(float)
            df['First Pass Yield / Line'] = (((df['Qty Checked'] - df['First Pass Def'])/df['Qty Checked'].replace(0, pd.NA)) * 100).fillna(0).astype(float)
            df['GAP (FY - FPY)'] = df['Final Yield / Line'] - df['First Pass Yield / Line'] 

            for col in ['Final Yield / Line', 'First Pass Yield / Line', 'GAP (FY - FPY)']:
                df[col] = df[col].round(2).astype(str) + "%"

            return df
        
        except Exception as e : 
            print(f"Error in class YieldCalculation (yield_generations) : {e}")
    
    def melt_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """ Melt DataFrame (Row to Columns)"""
        try : 
            return pd.melt(
                df,
                id_vars=['Model', 'Part Name', 'Detail_Date', 'Final Yield / Line', 'First Pass Yield / Line', 'GAP (FY - FPY)'],
                value_vars=['Qty Checked', 'First Pass Def', 'Final Def'],
                var_name='Process'
                )
        
        except Exception as e : 
            print(f"Error in class YieldCalculation (melt_data) : {e}")
    
    def filter_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """ Filter Specific Columns"""
        try : 
            df = df[['Model', 'Part Name', 'Detail_Date', 'Final Yield / Line',
                         'First Pass Yield / Line', 'GAP (FY - FPY)',
                         'Process']]
            
            return df
        
        except Exception as e : 
            print(f"Error in class YieldCalculation (filter_data) : {e}") 
    
    def run(self, df: pd.DataFrame) -> pd.DataFrame:
        """ Processing Several Function in Class YieldCalculation"""
        try : 
            df = self.groupby_data(df) 
            df = self.yield_generations(df) 
            df = self.melt_data(df)
            return self.filter_data(df)

        except Exception as e :  
            print(f"Error in class YieldCalculation (run) : {e}")