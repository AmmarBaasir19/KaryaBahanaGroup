import streamlit as st 
import pandas as pd 
from SrcNew.Controller.DataValidation2 import DataValidation2
from SrcNew.Controller.DataValidation3 import DataValidation3
from SrcNew.Controller.ControllerPath import ControllerPath
from SrcNew.Model.SessionManager import SessionManager

class RunProcessingLayer2:
    def __reconstruction_inline(self, data: list) -> list:
        print(f"Ini __reconstruction_inline : {data}")
        """
        This Function will be reconstruction data inline repair from Final Defects Form
        Input Data : 
        |Index Inputan|Name Inputan|Index Outputan|Name Outputan|
        |-------------|------------|--------------|-------------|
        |0|Model|1|Model|
        |1|Part No|2|Part No|
        |2|Part Name|3|Part Name|
        |3|TTD KASIE|4|Ttd Kasie| 
        |4|TTD OPERATOR|5|Ttd Operator|
        |5|NIK OPERATOR|6|Nik Operator|
        |6|TAHUN|7|Tahun| 
        |7|BULAN|8|Bulan|
        |8|TANGGAL|9|Tanggal|
        |9|SHIFT|10|Shift|
        |10|Welding Check Points|11|Welding Check Points|
        |11|KEROPOS|12|Keropos|
        |12|KURANG|13|Kurang|
        |13|BOLONG|14|Bolong|
        |14|UNDERCUT|15|Undercut|
        |15|SPATTER|16|Spatter|
        |16|TIDAK TEPAT|17|Tidak Tepat|
        |17|Halaman|0|Halaman|
        """
        try : 
            df = [[row[-1]] + 
                  [row[0]] +
                  [DataValidation2().fuzzy_matching1(row[1])] +
                  [DataValidation2().fuzzy_matching2(row[2])] + 
                  [row[3]] +
                  [row[4]] + 
                  [row[5]] + 
                  [DataValidation2().invalid_type_1(DataValidation2().convert_to_int(row[6]))] +
                  [DataValidation2().invalid_type_2(DataValidation2().convert_to_int(row[7]))] + 
                  [DataValidation2().invalid_type_3(DataValidation2().convert_to_int(row[8]))] + 
                  [DataValidation2().invalid_shift(DataValidation2().invalid_convert_int(row[9]))] + 
                  [DataValidation2().invalid_convert_int(row[10])] + 
                  [" "] +  
                  [" "] + 
                  [" "] + 
                  [" "] + 
                  [" "] + 
                  [" "]
                  for row in data]
            
            return df
        
        except Exception as e : 
            st.error(f"Error in class RunProcessLayer2 (reconstruction_inline) : {e}")
    
    def __reconstruction_noninline(self, data: list) -> list:
        print(f"Ini __reconstruction_noninline : {data}")
        """
        -----------------------------------------
        Input Data : <br>
            1. , 2. , 3. , 4. , 5. , <br>
            6. , 7. , 8. , 9. , 10. , <br>
            11. , 12. , 13. , 14. , 15. , <br>
            16. , 17. , 18. , 19. , 20. , <br>
        """
        print(f"Ini __reconstruction_noninline")
        print(data)
        try : 
            df = [[row1[-1]] + 
                  [row1[0]] +
                  [DataValidation2().fuzzy_matching1(row1[1])] +
                  [DataValidation2().fuzzy_matching2(row1[2])] +
                  [row1[3]] + 
                  [row1[4]] + 
                  [row1[5]] +  
                  [DataValidation2().invalid_type_1(DataValidation2().convert_to_int(row1[6]))] +   
                  [DataValidation2().invalid_type_2(DataValidation2().convert_to_int(row1[7]))] +  
                  [DataValidation2().invalid_type_3(DataValidation2().convert_to_int(row1[8]))] +   
                  [DataValidation2().invalid_shift(DataValidation2().invalid_convert_int(row1[9]))] +  
                  [" "] +
                  [" "] + 
                  [" "] +
                  [" "] +
                  [" "] +
                  [" "] + 
                  [" "] +
                  [" "] +
                  [" "] + 
                  [" "] + 
                  [" "] + 
                  [" "] +
                  [" "] + 
                  DataValidation2().validate_quantity(row1[-6:-2]) +  
                  [row1[-2]]
                  for val in data for row1 in val]

            return df

        except Exception as e : 
            st.error(f"Error in class RunProcessLayer2 (reconstruction_noninline) : {e}")
    
    def __reconstruction_fpd(self, data: list) -> list:
        print(f"Ini __reconstruction_fpd : {data}")
        """
        --------------------------------
        Input Data : <br>
            1. Model, 2. Part No, 3. Part Name, 4. Part Group, 5. Shift, <br>
            6. Tahun, 7. Bulan, 8. Tanggal, 9. Nik_Nipm, 10. Total Repair, <br>
            11. Total Top, 12. Total Middle, 13. Total Bottom, 14. Halaman <br>
        """
        try : 
            df = [[row[-1]] + 
                  [row[0]] +
                  [DataValidation2().fuzzy_matching1(row[1])] +
                  [DataValidation2().fuzzy_matching2(row[2])] + 
                  [row[3]] + 
                  [DataValidation2().invalid_convert_int(row[4])] + 
                  [DataValidation2().invalid_type_1(DataValidation2().convert_to_int(row[5]))] + 
                  [DataValidation2().invalid_type_2(DataValidation2().convert_to_int(row[6]))] + 
                  [DataValidation2().invalid_type_3(DataValidation2().convert_to_int(row[7]))] + 
                  [row[8]] +  
                  [DataValidation2().convert_to_int(row[9])] +
                  [DataValidation2().convert_to_int(row[10])] + 
                  [DataValidation2().convert_to_int(row[11])] + 
                  [DataValidation2().convert_to_int(row[12])] 
                  for row in data]  
         
            return df
        
        except Exception as e : 
            st.error(f"Error in class RunProcessLayer2 (_reconstruction_fpd) : {e}")
    
    def __reconstruction_polygon1(self, data: list) -> list:
        print(f"Ini __reconstruction_polygon1 : {data}")
        """
        --------------------------------
        Input Data : <br>
            1. Model, 2. Part No, 3. Part Name, 4. Part Group, 5. Shift, <br>
            6. Tahun, 7. Bulan, 8. Tanggal, 9. Nik_Nipm, 10. Total Repair, <br>
            11. Total Top, 12. Total Middle, 13. Total Bottom, 14. Halaman <br>
        """
        try : 
            df = [[row[0]] + 
                  [row[1]] +
                  [row[2]] +
                  [row[3]] +
                  [row[4]] +
                  [row[5]] 
                  for row in data]  
         
            return df
        
        except Exception as e : 
            st.error(f"Error in class RunProcessLayer2 (_reconstruction_polygon1) : {e}")
    
    def __reconstruction_polygon2(self, data: list) -> list:
        print(f"Ini __reconstruction_polygon2 : {data}")
        """
        """
        try : 
            df = [[row[0]] + 
                  [row[1]]
                  for row in data]  
         
            return df
        
        except Exception as e : 
            st.error(f"Error in class RunProcessLayer2 (_reconstruction_polygon2) : {e}")
    
    def __created_df_fd(self, df1: list, df2: list) -> pd.DataFrame:
        try :  
            df1 = pd.DataFrame(self.__reconstruction_inline(df1), columns=ControllerPath().inline).astype(str) 
            df2 = pd.DataFrame(self.__reconstruction_noninline(df2), columns=ControllerPath().noninline).astype(str) 

            return df1, df2
        
        except Exception as e : 
            st.error(f"Error in class RunProcessLayer2 (__created_df_fd) : {e}")
    
    def __created_df_fpd(self, df: list) -> pd.DataFrame:  
        """
        """
        try :
            df = pd.DataFrame(self.__reconstruction_fpd(df), columns=ControllerPath().firstpass).astype(str) 

            return df 
        
        except Exception as e : 
            st.error(f"Error in class RunProcessLayer2 (__created_dataframe_fpd) : {e}") 
    
    def __created_df_polygon(self, df: list, type_form: str) -> pd.DataFrame:  
        """
        """
        try :
            if type_form == "Final Defects":
                df = pd.DataFrame(self.__reconstruction_polygon1(df), columns=['table_1', 'table_2', 'table_3', 'table_4', 'table_5', 'table_6']).astype(str) 
            
            else : 
                df = pd.DataFrame(self.__reconstruction_polygon2(df), columns=['table_1', 'table_2']).astype(str)

            return df 
        
        except Exception as e : 
            st.error(f"Error in class RunProcessLayer2 (__created_df_polygon) : {e}") 
    
    def run(self, df1: list, df2: list, df3: list, df4: list, type_form: str) -> pd.DataFrame:
        """
        This function will be run several function like : 
            1. _created_df_fd 
            2. DataValidation3().join_and_replace
            3. DataValidation3().sorted_data
            4. _created_df_fd
        ----------------------------------------------------
        Parameter : 
            - df1 : Dataframe Final Defects (Inline Repair)
            - df2 : Datafarme Final Defects (Noninline Repair)
            - df3 : Dataframe First Pass Defects
            - type_form : Input Type Form (Final Defects or First Pass Defects) 
        """
        try : 
            df_polygon = self.__created_df_polygon(df=df4, type_form=type_form)
            if type_form == "Final Defects":
                df1, df2 = self.__created_df_fd(df1, df2)

                df1['Part Name'] = df1['Part Name'].str.replace(r"\s+", "", regex=True).str.strip()
                df2['Part Name'] = df2['Part Name'].str.replace(r"\s+", "", regex=True).str.strip() 

                df1 = df1.rename(columns={'Nik Operator' : 'Nik_Nipm'})
                df2 = df2.rename(columns={'Nik Operator' : 'Nik_Nipm'})

                if len(df1) > 1 :
                    df1 = DataValidation3().join_and_replace(df1)
                else :
                    df1 = df1

                #df2 = df2.drop_duplicates(subset=['Model', 'Part No', 'Part Name', 'Shift'], keep='first')

                #df2 = DataValidation3().sorted_data(df2, type_form=type_form)

                SessionManager().set_setter_state(key='dataframe_inline', value=df1) 
                SessionManager().set_setter_state(key='dataframe_noninline', value=df2) 
                SessionManager().set_setter_state(key='dataframe_polygon', value=df_polygon) 
            
            else : 
                df3 = self.__created_df_fpd(df3)
                print(f"Ini RunProcessingLayer2 (df3) : {df3}")
                print(f"Ini RunProcessingLayer2 (df3) Columns : {df3.columns}")

                df3['Part Name'] = df3['Part Name'].str.replace(r"\s+", "", regex=True).str.strip() 
                df3 = df3.rename(columns={'Nik/Nipm' : 'Nik_Nipm'})
                print(f"Ini df")

                if len(df3) > 1 : 
                    print(f"Ini RunProcessingLayer2 (df3) rename : {df3}") 
                    df3 = DataValidation3().join_and_replace(df3)

                else :
                    df3 = df3 

                SessionManager().set_setter_state(key='dataframe_fpd', value=df3)
                SessionManager().set_setter_state(key='dataframe_polygon', value=df_polygon)
        
        except Exception as e :  
            st.error(f"Error in class RunProcessLayer2 (run) : {e}")