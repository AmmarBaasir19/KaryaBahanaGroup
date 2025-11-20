import os 
import streamlit as st 
import pandas as pd
from typing import Any
from datetime import datetime, timedelta
from SrcNew.Controller.ControllerPath import ControllerPath

class FileManager:
    def get_format_name(self, df: pd.DataFrame) -> str :
        """
        This function will be provide format file name.
        This function will get columns name : Tahun, Bulan, Tanggal
        """ 

        try :
            format_name = "".join([str(df.iloc[0, i]) for i in [7, 8, 9]])
            return format_name
        
        except Exception as e :
            st.error(f"Error in class FileManager (get_format_name) : {e}")
    
    def __get_format_name2(self, df: pd.DataFrame) -> str : 
        """""" 
        try :
            format_name = "S".join([str(df.iloc[0, i]) for i in [10]])
            return format_name
        
        except Exception as e :
            st.error(f"Error in class FileManager (get_format_name2) : {e}")
    
    def inline_name(self, df):
        """
        ------------------------------
        Parameter : <br>
            - df : DataFrame Inline Repair <br>
        """
        return f"{'DF_Inline' + '_' + 'ID' + self.get_format_name(df) + '_' + '.csv'}"

    def noninline_name(self, df):
        """
        ------------------------------
        Parameter : <br>
            - df : DataFrame Noninline Repair <br>
        """
        return f"{'DF_Noninline' + '_' + 'ID' + self.get_format_name(df) + '_' + '.csv'}"
    
    def firstpasss_name(self, df):
        """
        ------------------------------
        Parameter : <br>
            - df : DataFrame First Pass Defect <br>
        """
        return f"{'DF_FirstPassDefects' + '_' + 'ID' + self.get_format_name(df) + '_' + '.csv'}"
    
    def uinteraction_name(self, df):
        """
        ------------------------------
        Parameter : <br>
            - df : DataFrame Users <br>
        """
        return f"DF_Users_ID_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_.csv"