import pandas as pd 
import streamlit as st 

class CalenderActivity:
    def get_database(self):
        """"""
        try : 
            df1 = pd.read_csv("home\cortex\Medallion_Hub\Karya_Bahana_Apps\Calender_DB\FD\Master_Activity_FD.csv")
            df2 = pd.read_csv("home\cortex\Medallion_Hub\Karya_Bahana_Apps\Calender_DB\FPD\Master_Activity_FPD.csv")
            df1 = df1[['title', 'Tahun', 'Bulan', 'Tanggal', 'Shift']]
            df2 = df2[['title', 'Tahun', 'Bulan', 'Tanggal', 'Shift']]

            return df1, df2

        except Exception as e : 
            print(f"Error in class CalenderActivity (get_database) : {e}")
    
    def merge_database(self, df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        """"""
        try : 
            df = pd.concat([df1, df2])
            df = df.dropna()

            return df

        except Exception as e : 
            print(f"")

    def generate_db_activity(self, df: pd.DataFrame) -> pd.DataFrame:
        """"""
        try : 
            df['production_date'] = df['Tahun'].astype(str) + '-' + df['Bulan'].astype(str) + '-' + df['Tanggal'].astype(str)

            ## Filter Data 
            df = df[['title', 'production_date']]

            ## Add Data 
            df['status'] = 'yes' 

            return df 
    
        except Exception as e : 
            print(f"Error in class CalenderActivity (generate_db_activity) : {e}")
    
    def run(self):
        """"""
        try : 
            ## Get Database
            df1, df2 = self.get_database()

            ## Merge Database
            df = self.merge_database(df1, df2)

            ## Generate Databse and Refredh Calender Activity
            df = self.generate_db_activity(df)
            df = df.drop_duplicates(keep='first') 

            df.to_csv("home/cortex/Medallion_Hub/Karya_Bahana_Apps/Calender_DB/Data_Calender.csv")

        except Exception as e : 
            print(f"")
        