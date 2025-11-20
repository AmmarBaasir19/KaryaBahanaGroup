import pandas as pd 
import streamlit as st 
from SrcNew.Controller.DataValidation1 import DataValidation1
from SrcNew.Controller.DataSyntheticFPD import DataSyntheticFPD
from SrcNew.Controller.ControllerPath import ControllerPath
from SrcNew.Model.SessionManager import SessionManager

class DataPreprocessingFPD:
    def __process_raw_data(self, value) -> pd.DataFrame:
        """
        This function will be process make a table to stored data welding spot. 
        """
        try : 
            dataframe = []
            for table_idx, table in enumerate(value['tables']):
                table_data = {}
                for cell in table['cells']:
                    row, col = cell['rowIndex'], cell['columnIndex']
                    con = cell['content'] 
                    if row not in table_data:
                        table_data[row] = {}  

                    table_data[row][col] = con
                df = pd.DataFrame.from_dict(table_data, orient='index').sort_index(axis=1)
                df.columns = df.iloc[0]
                df = df[1:].reset_index(drop=True)
        
                dataframe.append(df)
            return dataframe 
        
        except Exception as e:
            st.error(f"Error in class DataPreprocessingFPD (_process_raw_data) : {e}") 
    
    def __process_polygon(self, value: any) -> pd.DataFrame:
        """"""
        try : 
            merged = {cols: values for res in value['polygon'] for cols, values in res.items()}
            df = pd.DataFrame([merged])

            return df
        
        except Exception as e : 
            st.error(f"Error in class DataPreprocessingFPD (_process_polygon) : {e}")
    
    def __created_polygon(self, df: pd.DataFrame) -> pd.DataFrame: 
        """"""
        try :
            columns_base = ControllerPath().columns_polygon_fpd

            value_tables = set(columns_base) - set(df.columns)
            if value_tables is not None :
                df_man = pd.DataFrame([[0] * len(value_tables)], columns=sorted(value_tables))
                df = pd.concat([df, df_man], axis=1)
    
            return df

        except Exception as e : 
            st.error(f"Error in class DataPreprocessingFPD (_created_polygon) : {e}")
    
    def __merge_table(self, data: list) -> list: 
        """
        This fuction will be join data header (identifier) and welding spot data
        """
        try :
            dataframe = pd.concat([data[0].reset_index(drop=True), data[1].reset_index(drop=True)], axis=1)
            return dataframe 
        
        except Exception as e:
            st.error(f"Error in class DataPreprocessingFPD (_merge_table) : {e}") 
    
    def run(self, value, i, type_form) -> pd.DataFrame:
        """""" 
        print(f"Ini DataPreprocessingFPD (run) : {value}")
        df = self.__process_raw_data(value)
        print(f"Ini DataPreprocessingFPD _process_raw_data : {df}")
        print(f"Ini DataPreprocessingFPD _process_raw_data len : {len(df)}")
        print(f"Ini DataPreprocessingFPD _process_raw_data columns 1 : {df[0].columns}")
        print(f"Ini DataPreprocessingFPD _process_raw_data columns 2 : {df[1].columns}")

        ## Call function _process_polygon
        polygon_data = self.__process_polygon(value)
        print(f"Ini DataPreprocessingFPD polygon_data : {polygon_data}")

        df = DataValidation1().remove_nan_columns([data for data in df])
        print(f"Ini DataPreprocessingFPD DataValidation1 : {df}") 
        print(f"Len DataPreprocessingFPD : {len(df)}")  

        if len(df) != 2 : 
            df = DataSyntheticFPD().run(df)
        else : 
            df = df
        
        df = DataValidation1().columns_title(df)
        print(f"Ini df DataValidation1()._columns_case : {df}") 

        df = DataValidation1().drop_duplicated_columns(df=df, type_form=type_form)
        print(f"Ini After DataValidation1().drop_duplicated_columns : {df}")

        df = self.__merge_table(df) 
        print(f"Ini DataPreprocessingFPD _merge_table : {df}")

        df = df.dropna(subset=["Model", "Part No", "Part Name", "Part Group"])
        print(f"Ini DataPreprocessingFPD dropna : {df}")

        df = DataValidation1().clean_columns(df) 
        print(f"Ini DataPreprocessingFPD DataValidation1 clean_columns : {df}")

        df['Halaman'] = f"Halaman {i + 1}"
        print(f"Ini DataPreprocessingFPD Halaman : {df}")

        df_polygon = self.__created_polygon(polygon_data)

        return df, df_polygon



