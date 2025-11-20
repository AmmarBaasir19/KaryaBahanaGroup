import re
import pandas as pd 
import streamlit as st 

class DataValidation3:
    def join_and_replace(self, data: pd.DataFrame):
        """
        This Function will be join and replace several values. 
        """ 
        try : 
            index_range = data.groupby(["Model", "Part Name", "Part No"]).apply(
            lambda x: pd.Series({
                'Nik_Nipm' : x['Nik_Nipm'].iloc[0],
                'Tahun' : x['Tahun'].iloc[0],
                'Bulan' : x['Bulan'].iloc[0], 
                'Tanggal' : x['Tanggal'].iloc[0],
                'Shift' : x['Shift'].iloc[0],
                'start_index' : x.index.min(),
                'end_index' : x.index.max(), 
                })
            ).reset_index()

                        # Contoh: update kolom 'Halaman' pada baris pertama setiap grup
            for i, row in index_range.iterrows():
                start_idx = row['start_index']
                end_idx = row['end_index']
                # Misalnya, kita ingin mencatat rentang indeks di kolom 'Halaman'
                data.loc[start_idx:end_idx, 'Nik_Nipm'] = row['Nik_Nipm']
                data.loc[start_idx:end_idx, 'Tahun'] = row['Tahun']
                data.loc[start_idx:end_idx, 'Bulan'] = row['Bulan'] 
                data.loc[start_idx:end_idx, 'Tanggal'] = row['Tanggal']
                data.loc[start_idx:end_idx, 'Shift'] = row['Shift']

            return data
        
        except Exception as e : 
            st.error(f"Error in class DataValidation3 (join_and_replace) : {e}")
    
    def sorted_data(self, df: pd.DataFrame, type_form: str) -> pd.DataFrame:
        """"""
        try : 
            if type_form == "Final Defects" :
                df = df[self.controller_path.dataframe_format_fpy]
                return df

            else : 
                df = df[self.controller_path.data_format_2] 
                return df 
        
        except Exception as e : 
            st.error(f"Error in class DataValidation3 (sorted_data) : {e}")
    
    def find_index_error1(self, df: pd.DataFrame, type_form):
        """"""
        try : 
            if type_form == "Final Defects" :
                test = self.check_invalid(df[['Tahun', 'Bulan', 'Tanggal', 'Shift', 'Keropos', 'Kurang', 'Bolong', 'Undercut', 'Spatter', 'Tidak Tepat']])
                test1 = df[test.any(axis=1)].index.tolist()
                test_final = df.iloc[test1]['Halaman'].unique().tolist()
                return test_final 

            else : 
                test = self.check_invalid(df[['Tahun', 'Bulan', 'Tanggal', 'Shift', 'Total Repair', 'Total Top', 'Total Middle', 'Total Bottom']])
                test1 = df[test.any(axis=1)].index.tolist() 
                test_final = df.iloc[test1]['Halaman'].unique().tolist()
                return test_final 
        
        except Exception as e : 
            st.error(f"Error in class DataValidation3 (find_index_error1) : {e}")
    
    def find_index_error2(self, df: pd.DataFrame):
        """"""
        try : 
            test = self.check_invalid(df[list(self.controller_path.table_5['columns_name'])])
            test1 = df[test.any(axis=1)].index.tolist()
            test_final = df.iloc[test1]['Halaman'].unique().tolist() 
            return test_final
        
        except Exception as e : 
            st.error(f"Error in DataValidation3 (find_index_error2) : {e}")
    
    def validation_welding_points(self, data):
        """"""    
        try : 
            corrected_values = [] 

            if isinstance(data, (int, float)) and not pd.isna(data):
                corrected_values.append(int(data))
            
            elif isinstance(data, str):
                numbers = re.findall(r'\d', data)
                if numbers:
                    corrected_values.append(int(numbers[0]))
        
        except Exception as e :
            st.error(f"Error in class DataValidation3 (_validation_welding_points) : {e}")
    
    def get_counts_quality(self, df):  
        """
        This Function will be get or return sum (total) calculate valid data and invalid data. 
        """
        
        try : 
            ## Convert data to String and calculate (grouping) data by Invalid dan Valid Teks. 
            invalid_mask = df.astype(str).apply(lambda col: col.map(lambda x: "Invalid" in x))
            valid_sum = (~invalid_mask).sum().sum() 
            invalid_sum = (invalid_mask).sum().sum() 
            return valid_sum, invalid_sum 
        
        except Exception as e :
            st.error(f"Error in class DataValidation3 (get_counts_quality) : {e}")

    def check_invalid(self, value):
        """"""
        try : 
            return value.astype(str).apply(lambda col: col.str.contains("Invalid", na=False)).any().any()
        
        except Exception as e : 
            st.error(f"Error in class DataValidation3 (check_invalid) : {e}")