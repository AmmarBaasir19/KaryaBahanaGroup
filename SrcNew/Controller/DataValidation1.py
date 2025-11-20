import re 
import streamlit as st 
import pandas as pd 
from SrcNew.Controller.ControllerPath import ControllerPath


class DataValidation1:
    def columns_title(self, value):
        """""" 
        try : 
            return [df.rename(columns=lambda x: str(x).title()) for df in value]
    
        except Exception as e : 
            st.error(f"Error in class DataValidation1 (_columns_title) : {e}") 

        
    def remove_nan_columns(self, value):
        """"""
        try : 
            print(f"Ini DataValidation1 remove_nan_columns type : {type(value)}")
            df = [data.loc[:, data.columns.notna()] for data in value]
                
            return df
            
        except Exception as e : 
            st.error(f"Error in class DataValidation1 (_remove_nan_columns)")
    
    def drop_duplicated_columns(self, df, type_form):
        """"""
        try :  

            if type_form == "Final Defects":
                df1 = df[0].loc[:, ~df[0].columns.duplicated()]
                df2 = df[1].loc[:, ~df[1].columns.duplicated()]
                df3 = df[2].loc[:, ~df[2].columns.duplicated()]
                df4 = df[3].loc[:, ~df[3].columns.duplicated()] 
                df5 = df[4].loc[:, ~df[4].columns.duplicated()] 
                df6 = df[5].loc[:, ~df[5].columns.duplicated()] 

                return df1, df2, df3, df4, df5, df6 
            
            else : 
                df1 = df[0].loc[:, ~df[0].columns.duplicated()]
                df2 = df[1].loc[:, ~df[1].columns.duplicated()]

                return df1, df2
        
        except Exception as e : 
            st.error(f"")
    
    def clean_columns(self, df) -> pd.DataFrame:
        """
        This Function will be clean columns name in dataframe, 
        if columns name have special character
        """
        try : 
            ## Define Pattern Regex 
            replace_list = [":unselected:", ":selected:", ":selected:", ":unselected:", ".", "!", "?", "<", ">", "|", "[", "]",
                            ":", ";", "@", "#", "$", "%", "^", "&", "*", "-", "_", "+", "=", "~", "{", "}", " ", "  "] 
            pattern = "|".join(map(re.escape, replace_list)) 

            ## Implemented In Columns Name
            df.columns = df.columns.astype(str).str.replace(pattern, ' ', regex=True) 
            df.columns = df.columns.str.strip() 
        
            return df
        
        except Exception as e : 
            st.error(f"Error in class DataValidation1 (_clean_columns) : {e}")
    
    def drop_columns(self, df, type_form):
        """
        This Function will be drop columns that not in list_spot1, list_spot2, list_spot3, list_spot4, list_spot5, list_spot6
        """
        try : 
            if type_form == "Final Defects" :
                ## List of Columns Name
                drop_spot = [self.list_spot1, self.list_spot2,
                             self.list_spot3, self.list_spot4, 
                             self.list_spot4, self.list_spot5] 
             
        
                ## Validate Columns Name
                dataframes = [ 
                    df[i].drop(columns=[col for col in df[i].columns if col not in drop_spot[i]])
                    for i in range(6)
                ] 

                ## Define Variable for Each Dataframe 
                dataframe_spot1, dataframe_spot2, dataframe_spot3, dataframe_spot4, dataframe_spot5, dataframe_spot6 = dataframes

                return dataframe_spot1, dataframe_spot2, dataframe_spot3, dataframe_spot4, dataframe_spot5, dataframe_spot6
            
            else : 
                pass
        
        except Exception as e : 
            st.error(f"")  
    
    def order_dataframe(self, data) : 
        """
        
        """
        result = [[] for _ in range(6)]
        spot_4_filled = False

        spots = [ControllerPath().table_1_fd['columns_name'],
                 ControllerPath().table_2_fd['columns_name'], 
                 ControllerPath().table_3_fd['columns_name'],
                 ControllerPath().table_4_fd['columns_name'],
                 ControllerPath().table_5_fd['columns_name']]
        
        for data_list in data:
            for idx, spot in enumerate(spots):
                if any(item in spot for item in data_list):
                    if idx == 3 : 
                        result[3 if not spot_4_filled else 4].append(data_list)
                        spot_4_filled = True
                    
                    else : 
                        target = idx if idx < 3 else 5
                        result[target].append(data_list)
                    break
        
        return sum(result, [])