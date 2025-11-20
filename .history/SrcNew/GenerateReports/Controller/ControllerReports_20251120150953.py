import pandas as pd 
import numpy as np 

class ControllerReports:
    def join_data(self, df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        """ Join Data (Final Def and First Pass Def)"""
        try :
            return pd.merge(
                df1, df2,
                on=['Model', 'Part No', 'Part Name', 'Tahun', 'Bulan', 'Tanggal', 'Shift'],
                how='outer'
            )
        
        except Exception as e : 
            print(f"Error in class ControllerReports (join_data) : {e}")
    
    def feature_engineering(self, df:pd.DataFrame) -> pd.DataFrame:
        """ Feature Engineering (replace values in columns Bulan)"""
        try : 
            month_map = {
                1: 'Januari', 2: 'Februari', 3: 'Maret', 4: 'April', 5: 'Mei',
                6: 'Juni', 7: 'Juli', 8: 'Agustus', 9: 'September',
                10: 'Oktober', 11: 'November', 12: 'Desember'
            }

            ## Merge Column Tahun, Bulan, Tanggal Become YYYY-MM-DD Format
            df['Production Date'] = pd.to_datetime(
                df[['Tahun', 'Bulan', 'Tanggal']].astype(str).agg('-'.join, axis=1),
                errors='coerce'
            )

            ## Change Number Format in Bulan Column to Bulan Name in Indonesia
            df['Bulan'] = df['Bulan'].replace(month_map)

            return df

        except Exception as e : 
            print(f"Error in class ControllerReports (feature_engineering) : {e}")
    
    def sort_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """ Sort Data with Specific Format"""
        try :
            cols = ['Model', 'Part Name', 'Production Date', 'Tahun', 'Bulan', 'Tanggal', 'Shift', 'Qty Checked', 'First Pass Def', 'Final Def']

            return df[cols]
        
        except Exception as e : 
            print(f"Error in class ControllerReports (sort_data) : {e}")
    
    def filter_date(self, df: pd.DataFrame, start_date: pd.to_datetime, end_date: pd.to_datetime) -> pd.DataFrame:
        """ Filter Data with Specific Date"""
        try : 
            print(df.info())
            return df[(df['Production Date'] >= pd.to_datetime(start_date)) & (df['Production Date'] <= pd.to_datetime(end_date))] 

        except Exception as e : 
            print(f"Error in class ControllerReports (filter_date) : {e}")
    
    def generate_periode(self, df: pd.DataFrame) -> pd.DataFrame:
        """ Genereta Automatic Values in Specific Columns"""
        try : 
            min_date = df['Tanggal'].min()
            max_date = df['Tanggal'].max()

            df['Bulan'] = df['Bulan'].astype(str) + " " + df['Tahun'].astype(str)
            df['Shift'] = "Shift " + df['Shift'].astype(str)
            df['Detail_Date'] = f"{min_date}-{max_date} " + df['Bulan']

            return df 

        except Exception as e : 
            print(f"Error in class ControllerReports (generate_periode) : {e}")
    
    def remove_duplicated(self, df: pd.DataFrame, column: str) -> pd.DataFrame:
        """ Remove Duplicated Data with Specific Columns"""
        try : 
            dup_mask = df.reset_index()[column].duplicated(keep='first')
            df.loc[dup_mask, column] = np.nan

            return df

        except Exception as e : 
            print(f"Error in class ControllerReports (remove_duplicated) : {e}")
    
    def run(self, df1: pd.DataFrame, df2: pd.DataFrame, start_date: pd.to_datetime, end_date: pd.to_datetime) -> pd.DataFrame:
        """ Processing Several Function in Class ControllerReports"""
        try : 
            df = self.join_data(df1, df2)
            print(f"Ini setelah join_data (ControllerReports) : {df}")
            df = self.feature_engineering(df)
            print(f"Ini setelah feature_engineering (ControllerReports) : {df}")
            df = self.sort_data(df)
            print(f"Ini setelah sort_data (ControllerReports) : {df}")
            df = self.filter_date(df, start_date, end_date)
            print(f"Ini setelah filter_data (ControllerReports) : {df}")
            return self.generate_periode(df)

        except Exception as e :  
            print(f"Error in class ControllerReports (run) : {e}") 