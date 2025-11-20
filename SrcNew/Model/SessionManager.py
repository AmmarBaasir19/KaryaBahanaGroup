import numpy as np 
import pandas as pd
import streamlit as st 
from typing import Any

class SessionManager:
    def __init__(self):
        self.session_state_values = {              
            'changes_list' : [],
            'popup_show' : False,
            'dataset_name' : [],
            'sum_processing' : [],
            'start_processing' : [],
            'end_processing' : [],
            'modal' : [], 
            'halaman' : [],
            'button_auto' : False,
            'current_page' : "Beranda", 
            'pdf_merged' : False,
            'data_loaded' : False,
            'merged_file_path' : None,
            'error_flag' : False,
            'error_page' : [],
            'list_images' : [],
            'list_pdf' : [],
            'file_uploader' : [],
            'start_time_fpy' : [],
            'end_time_fpy' : [], 
            'valid_fpy' : [],
            'invalid_fpy' : [], 
            'halaman_selected' : [],
            'tahun_user' : [],
            'bulan_user' : [],
            'tanggal_user' : [], 
            'form_type' : [],
            'username' : [],
            'name' : [],
            'nik_nipm' : [], 
            'location' : [],
            'role' : [],
            'start_actv' : [],
            'end_actv' : [],
            'login_time' : [], 
            'login_condition' : False,
            'dataframe_loaded' : False,
            'btn_click' : 0, 
            'button_start' : False
        } 

        self._initialize_session_state()
    
    def _initialize_session_state(self):
        """"""
        for key, value in self.session_state_values.items():
            if key not in st.session_state:
                st.session_state[key] = value 
    
    def set_setter_state(self, key, value, df=None) -> Any:
        """
        -------------------------------------------------------
        Parameter : <br>
            - key : "Key Values in Session State, if DataFrame Key is Columns Name" <br>
            - value : "Values will be define in Session State", <br>
            - df : The Name of Dataframe (default df = None) <br>
        -------------------------------------------------------
        Example : 
        SessionManager()._set_setter_state('dataframe', values)
        """
        if df == None : 
            st.session_state[key] = value  
        
        else : 
            st.session_state[df][key] = value

    def get_setter_state(self, key, df=None) -> Any:
        """
        ------------------------------------
        Parameter : <br>
            - key : "Key Values in Session State" <br>
            - df : "The Name of Dataframe (default df = None)"
        -----------------------------------
        Example : 
        SessionManager()._get_setter_state('dataframe')
        """
        if df == None :
            return st.session_state.get(key, None)
        
        else : 
            return st.session_state[df][key] 

    def get_dataframe(self, df, key, value=None):
        """"""
        if value != None :
            return st.session_state[df][key] == value
        
        else : 
            return st.session_state[df][key]
    
    def has_dataframe(self, df):
        """
        ----------------------------------------------
        Parameter : <br>
            - df : Is Dataframe will be show (get) <br>
        """ 
        return st.session_state[df]

    def set_start_time(self, data):
        """"""
        st.session_state['start_time'] = data 
    
    def set_end_time(self, data):
        """"""
        st.session_state['end_time'] 
    
    def get_start_time(self):
        """"""
        return st.session_state.get('start_time', None)
    
    def get_end_time(self):
        """"""
        return st.session_state.get('end_time', None)
    
    def set_file_uploader(self):
        """"""
        st.session_state['file_uploader'] = None
    
    def has_error_flag(self):
        """"""
        return 'error_flag' not in st.session_state
    
    def error_flag(self):
        return 'error_flag' not in st.session_state 
    
    def set_dataframe_index(self, df, index, df_new):
        """"""
        st.session_state[df].loc[index] = df_new

    def generate_dataframe(self, key, rows, cols, *columns):
        """
        -----------------------------------------
        Parameter : 
            - key : The name of DataFrame 
            - rows : The total of rows will be generate in DataFrame
            - cols : The total of cols will be genetate in DataFrame
        """
        st.session_state[key] = pd.DataFrame(np.zeros((rows, cols)), columns=list(columns))
    
    def has_dataframe_inline(self):
        """"""
        return "dataframe_inline" in st.session_state
    
    def has_dataframe_fpd(self):
        """"""
        return "dataframe_fpd" in st.session_state 
    
    def check_date_values_empty(self):
        return (st.session_state.tahun_user == "None" and 
                st.session_state.bulan_user == "None" and
                st.session_state.tanggal_user == "None")
    
    def update_shift(self, df: pd.DataFrame, columns1: str, value1: str, columns2: str, value2: str):
        """
        ----------------------------------
        Parameter : <br>
            - df : Is DataFrame will be change
            - columns1 : Is Name Column for filter
            - value1 : Is value for filter condition
            - columns2 : Is Name Column will be change
            - value2 : Is Value will be add in columns2 (Name Columns)
        """
        st.session_state[df].loc[st.session_state[df][columns1] == value1, columns2] = value2
    
    def has_key(self, key):
        """"""
        return st.session_state[key]  
    
    def set_start_btn(self, tahun, bulan, tanggal, form_type, btn_auto):
        """"""
        self.set_setter_state(key='tahun_user', value=tahun)
        self.set_setter_state(key='bulan_user', value=bulan)
        self.set_setter_state(key='tanggal_user', value=tanggal)
        self.set_setter_state(key='form_type', value=form_type)
        self.set_setter_state(key='button_auto', value=btn_auto)
    
    def reset_session(self, keeps_key):
        for key in list(st.session_state.keys()):
            if key not in keeps_key:
                del st.session_state[key]