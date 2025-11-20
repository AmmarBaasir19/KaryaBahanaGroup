import pandas as pd  
import streamlit as st 
from SrcNew.Controller.ControllerPath import ControllerPath
from SrcNew.Controller.DataValidation1 import DataValidation1
from SrcNew.Controller.DataSyntheticFD import DataSyntheticFD
from SrcNew.Model.SessionManager import SessionManager

class DataPreprocessingFD:
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
        
        except Exception as e : 
            st.error(f"Error in class DataPreprocessingFD (__process_raw_data) : {e}") 
    
    def __process_polygon(self, value: any) -> pd.DataFrame:
        """"""
        try : 
            merged = {cols: values for res in value['polygon'] for cols, values in res.items()}
            df = pd.DataFrame([merged]) 

            return df 
        
        except Exception as e : 
            st.error(f"Error in class DataPreprocessingFD (__process_polygon) : {e}")
    
    def __get_catatan(self, data):
        """
        This function will be get data problem in points catatan
        """
        try :
            page_save = [] 
            for page in data['pages']:
                for word in page['words']:
                    page_save.append(word['content']) 

            fin_index_start = []
            fin_val_start = []
            for i, page_1 in enumerate(page_save):
                fin_val_start.append(page_1) 
                if page_1.lower() == 'catatan:':
                    fin_index_start.append(i)
        
            fin_index2_start = []
            fin_val2_start = []
            for x, page_2 in enumerate(page_save):
                fin_val2_start.append(page_2) 
                if 'FRM' in page_2 or 'frm' in page_2.lower(): 
                    fin_index2_start.append(x)
                elif 'QC' in page_2 or 'qc' in page_2.lower():
                    fin_index2_start.append(x)

            if fin_index_start:
                fin_index_start[0] += 1
                text_catatan = fin_val_start[fin_index_start[0]:fin_index2_start[-1]] 
                data_catatan = ' '.join(text_catatan)
    
            return data_catatan 
        except Exception as e:
            st.error(f"Error in class DataPreprocessingFD (_get_catatan) : {e}")
    
    def __merge_table(self, df): 
        """
        This fuction will be join data header (identifier) and welding spot data
        """
        try :
            print(f"Ini DataPreprocessingFD data 1 : {df[0]}")
            print(f"Ini DataPreprocessingFD data 2 : {df[1]}")
            print(f"Ini DataPreprocessingFD data 3 : {df[2]}")
            print(f"Ini DataPreprocessingFD data 4 : {df[3]}")
            print(f"Ini DataPreprocessingFD data 5 : {df[4]}")
            print(f"Ini DataPreprocessingFD data 6 : {df[5]}") 
            table_1_3 = pd.concat([df[0], df[1]], axis=1) 
 
            data_inline = pd.concat([df[3], df[4]], ignore_index=True)
            print(f"Ini __merge_table data_inline : {data_inline}") 

            dataframe_temp = pd.concat([table_1_3.reset_index(drop=True)] * len(data_inline), ignore_index=True)
            dataframe_1 = pd.concat([dataframe_temp, data_inline], axis=1)
            dataframe_2 = pd.concat([df[0], df[1], df[5], df[2]], axis=1) 
        
            return dataframe_1, dataframe_2 
        except Exception as e: 
            st.error(f"Error in class DataPreprocessingFD (merge_table) : {e}")

    def __created_polygon(self, df: pd.DataFrame) -> pd.DataFrame: 
        """"""
        try : 
            columns_base = ControllerPath().columns_polygon_fd

            value_tables = set(columns_base) - set(df.columns)
            if value_tables is not None :
                df_man = pd.DataFrame([[0] * len(value_tables)], columns=sorted(value_tables))
                df = pd.concat([df, df_man], axis=1)
     
            return df

        except Exception as e : 
            st.error(f"Error in class DataPreprocessingFD (__created_polygon) : {e}")
    
    def run(self, value, i, type_form):
        """"""
        ## Call Function process_raw_data
        df = self.__process_raw_data(value)
        print(f"Hasil __process_raw_data fd len : {len(df)}")
        print(f"Hasil __process_raw_data fd : {df}")    

        ## Call function _process_polygon
        polygon_data = self.__process_polygon(value)
        print(f"Hasil __process_polygon fd : {polygon_data}")
        
        ## Call function text_catatan
        catatan_data = self.__get_catatan(value)
        print(f"Hasil __get_catatan fd : {catatan_data}")

        df = DataValidation1().remove_nan_columns([data for data in df])
        print(f"Hasil remove_nan_columns : {df}")   

        if len(df) != 6:
            ## Create Synthetic Data if len columns_drop != 6 
            df = DataSyntheticFD().run(df)  
        
        else :   
            df = df 
        
        df = DataValidation1().columns_title(df)
        print(f"Hasil columns_title : {df}") 
        print(f"Hasil columns_title : {len(df)}") 

        df = DataValidation1().drop_duplicated_columns(df=df, type_form=type_form)
        print(f"Ini After DataValidation1().drop_duplicated_columns() : {df}")

        df = DataValidation1().order_dataframe(df)
        print(f"Ini Hasil DataValidation1().order_dataframe : {df}") 

        df1, df2 = self.__merge_table(df) 
        print(f"Ini After __merge_table df1 : {df1}")
        print(f"Ini After __merge_table df1 columns : {df1.columns}")
        print(f"Ini After __merge_table df2 : {df2}")
        print(f"Ini After __merge_table df2 columns : {df2.columns}")

        ## Clean Columns for Specific Character
        df1 = DataValidation1().clean_columns(df1) 
        df2 = DataValidation1().clean_columns(df2) 
        print(f"Hasil clean_columns : {df1}") 
        print(f"Hasil clean_columns : {df2}") 

        ## Add Columns Catatan in dataframe_final_format_2 
        df2['Catatan'] = catatan_data
        print(f"Ini Hasil Add Catatan : {df2}") 

        ## Add Columns Halaman in df1 and df2
        df1['Halaman'] = (f"Halaman {i + 1}")
        df2['Halaman'] = (f"Halaman {i + 1}")
        print(f"Hasil add Halaman df1 : {df1}")
        print(f"Hasil add Halaman df2 : {df2}")

        df1 = df1[((df1['Model'].notna()) & (df1['Part No'].notna()) & (df1['Part Name'].notna()))]  
        df2 = df2[((df2['Model'].notna()) & (df2['Part No'].notna()) & (df2['Part Name'].notna()))]
        print(f"Hasil notna df1 : {df1}") 
        print(f"Hasil notna df1 columns : {df1.columns}")
        print(f"Hasil notna df2 : {df2}") 
        print(f"Hasil notna df1 columns : {df2.columns}")

        df_polygon = self.__created_polygon(polygon_data) 

        return df1, df2, df_polygon

