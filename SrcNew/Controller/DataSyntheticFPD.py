import pandas as pd 
import streamlit as st
from SrcNew.Controller.ControllerPath import ControllerPath

class DataSyntheticFPD:
    def miss_table(self, df):
        """"""
        try : 
            table_reference = {'table_1' : ControllerPath().table_1_fpd['columns_name'],
                               'table_2' : ControllerPath().table_2_fpd['columns_name']}
            
            detected_tables = set()

            for data in df:
                for table_name, required_col in table_reference.items():
                    if any(col in data.columns for col in required_col):
                        detected_tables.add(table_name)
            
            table_missing = [tab for tab in table_reference.keys() if tab not in detected_tables]

            return table_missing 
        
        except Exception as e : 
            st.error(f"Error in class DataSyntheticFPD (miss_table) : {e}")
    
    def create_table(self, df):
        """"""
        try : 
            miss_table = self.miss_table(df)

            table_reference = {'table_1' : ControllerPath().table_1_fpd['columns_name'],
                               'table_2' : ControllerPath().table_2_fpd['columns_name']}
            
            synthetic_table = []
            for table in miss_table:
                col  = table_reference.get(table, [])
                val_rows = ["Invalid Scanning"] * len(col)
                synthetic_table.append(pd.DataFrame([val_rows], columns=col))
            
            return synthetic_table

        except Exception as e : 
            st.error(f"Error in class DataSyntheticFPD (create_table) : {e}")
    
    def run(self, df):
        """"""
        try : 
            df_new = df.copy()
            table_synthetic = self.create_table(df)

            df_final = pd.merge(df_new.reset_index(drop=True), table_synthetic.reset_index(drop=True), axis=1) 

            return df_final 

        except Exception as e : 
            st.error(f"Error in class DataSyntheticFPD (run) : {e}") 