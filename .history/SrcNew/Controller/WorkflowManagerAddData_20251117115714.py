import time
import pandas as pd 
from io import BytesIO
import streamlit as st 
from typing import Any
from PyPDF2 import PdfMerger 
from datetime import datetime, timedelta
from SrcNew.Model.SessionManager import SessionManager
from SrcNew.Controller.RunProcessingLayerMain import RunProcessingLayerMain
from SrcNew.View.ComponentsStyle import ComponentsStyle
from SrcNew.View.ComponentsUserInput import ComponentsUserInput
from SrcNew.View.ComponentsButton import ComponentsButton
from SrcNew.View.ComponentsDataMonitoring import ComponentsDataMonitoring
from SrcNew.View.ComponentsDataFrame import ComponentsDataFrame
from SrcNew.Controller.DataValidation3 import DataValidation3
from SrcNew.Controller.DataProblemScanning import DataProblemScanning
from SrcNew.Controller.FileManager import FileManager
from SrcNew.Controller.ControllerPath import ControllerPath
from SrcNew.Model.DatabaseConfig import DatabaseConfig

class WorkflowManagerAddData: 
    def handling_date_input(self): 
        """ This function will be handling data input form user like Tahun, Bulan, Tanggal, and Tipe Form"""
        try : 
            ComponentsStyle().display_warning(
                "Harap Masukkan Data Tahun, Bulan, Tanggal dan Tipe Form Yang Sesuai Dengan Form Production"
            )
        
            tahun, bulan, tanggal, type = ComponentsUserInput().date_input()  
            button_start = SessionManager().get_setter_state(key="button_start") 

            if tahun != "None" and bulan != "None" and tanggal != "None"  and type != "None" and button_start == False: 
                now_start = datetime.now()
                SessionManager().set_setter_state(key='start_processing', value=now_start) 
                if ComponentsButton().button_start(tahun=tahun, bulan=bulan, tanggal=tanggal, form_type=type): 
                    SessionManager().set_setter_state(key="button_start", value=True) 
        
        except Exception as e : 
            st.error(f"Error in class WorkflowManagerAddData (handling_date_input) : {e}")
    
    def handling_date_in_df(self, type_form: str): 
        """
        This Function will be define data Tahun, Bulan, Tanggal in Session State. 
        ----------------------------------------------------------------------------
        Parameter : <br>
            - type_form : Type Form input from User (Final Defects or First Pass Defects) <br> 
        """
        try : 
            if type_form == "Final Defects" : 
                ## Setting Values in Dataframe Inline Repair
                SessionManager().set_setter_state(key='Tahun', value=SessionManager().get_setter_state(key='tahun_user'), df='dataframe_inline')
                SessionManager().set_setter_state(key='Bulan', value=SessionManager().get_setter_state(key='bulan_user'), df='dataframe_inline')
                SessionManager().set_setter_state(key='Tanggal', value=SessionManager().get_setter_state(key='tanggal_user'), df='dataframe_inline')
                SessionManager().set_setter_state(key='dataset_name', value=f"FRM-QC-026_rev3_{datetime.now().strftime('%Y-%m-%d')}_Final_Defects_Merge_File.pdf")

                ## Setting Values in Dataframe Noninline Repair
                SessionManager().set_setter_state(key='Tahun', value=SessionManager().get_setter_state(key='tahun_user'), df='dataframe_noninline')
                SessionManager().set_setter_state(key='Bulan', value=SessionManager().get_setter_state(key='bulan_user'), df='dataframe_noninline')
                SessionManager().set_setter_state(key='Tanggal', value=SessionManager().get_setter_state(key='tanggal_user'), df='dataframe_noninline')
            
            else : 
                SessionManager().set_setter_state(key='Tahun', value=SessionManager().get_setter_state(key='tahun_user'), df='dataframe_fpd') 
                SessionManager().set_setter_state(key='Bulan', value=SessionManager().get_setter_state(key='bulan_user'), df='dataframe_fpd') 
                SessionManager().set_setter_state(key='Tanggal', value=SessionManager().get_setter_state(key='tanggal_user'), df='dataframe_fpd')  
                SessionManager().set_setter_state(key='dataset_name', value=f"FRM-QC-026_rev3_{datetime.now().strftime('%Y-%m-%d')}_First_Pass_Defects_Merge_File.pdf")
        
        except Exception as e : 
            st.error(f"Error in class WorkflowManagerAddData (handling_date_in_df) : {e}")

    def handling_quality_data(self, type_form: str): 
        """
        This function will be processing data like calculate sum of valid and invalid data.
        -------------------------------------------------------------------------------------
        Parameter : <br>
            - type_form : Type Form input from User (Final Defects or First Pass Defects) <br>
        """
        try : 
            if type_form == "Final Defects" :
                valid1, invalid1 = DataValidation3().get_counts_quality(SessionManager().get_setter_state(key='dataframe_inline'))
                valid2, invalid2 = DataValidation3().get_counts_quality(SessionManager().get_setter_state(key='dataframe_noninline'))
                SessionManager().set_setter_state(key='valid_inline', value=valid1)
                SessionManager().set_setter_state(key='valid_noninline', value=valid2)
                SessionManager().set_setter_state(key='invalid_inline', value=invalid1)
                SessionManager().set_setter_state(key='invalid_noninline', value=invalid2)
            
            else :  
                valid, invalid = DataValidation3().get_counts_quality(SessionManager().get_setter_state(key='dataframe_fpd'))
                SessionManager().set_setter_state(key='valid_fpd', value=valid)
                SessionManager().set_setter_state(key='invalid_fpd', value=invalid)
        
        except Exception as e : 
            st.error(f"Error in class WorkflowManagerAddData (handling_quality_data) : {e}")

    def handling_scanning_data(self, uploaded_file: Any, type_form: str) -> Any:
        """
        This function will be processing form (file) from user. and will be return dataframe.
        --------------------------------------------------------------------------------------
        Parameter : 
            - uploaded_file : 
            - type form : 
        """ 
        try :  
            df_inline, df_noninline, df_fpd, error_page = RunProcessingLayerMain().run(uploaded_file, type_form)
            #print(f"Ini handling_scanning_data")
            if type_form == "Final Defects" :  
                SessionManager().set_setter_state(key='dataframe_inline', value=df_inline)
                SessionManager().set_setter_state(key='dataframe_noninline', value=df_noninline)
                SessionManager().set_setter_state(key='error_page', value=error_page) 
            
            else : 
                SessionManager().set_setter_state(key='dataframe_fpd', value=df_fpd)
                SessionManager().set_setter_state(key='error_page', value=error_page)
        
        except Exception as e :
            SessionManager().has_error_flag(True) 
            st.error(f"Error in class WorkflowManagerAddData (handling_scanning_data) : {e}")
    
    def handling_filter_fd(self, option_1, option_2, uploaded_file):
        """
        This function will be show data by filter (Dataframe Final Defects) <br>
        ----------------------------------------------------------------------------
        Parameter : <br>
            - option_1 : Type filter (Halaman) <br>
            - option_2 : Type filter (Tipe Invalid) <br>
            - uploaded_file : Input file from Users <br>
        """
        try : 
            if (len(option_1) == 0 or option_1 == "None") and len(option_2) != 0:
                ComponentsStyle().alert_filter("Halaman")
            
            elif (len(option_1) != 0 and option_1 != "None") and len(option_2) == 0:
                ComponentsStyle().alert_filter("Tipe Invalid")
            
            elif (len(option_1) != 0 or option_1 != "None") and len(option_2) != 0:
                ComponentsDataMonitoring().run(data1=SessionManager().get_setter_state(key='invalid_inline'), data2=SessionManager().get_setter_state(key='valid_inline'))
                df1, list_index1 = self.__handling_filter_inline(option_1=option_1, option_2=option_2)

                ComponentsDataMonitoring().run(data1=SessionManager().get_setter_state(key='invalid_noninline'), data2=SessionManager().get_setter_state(key='valid_noninline'))
                df2, list_index2 = self.__handling_filter_noninline(option_1=option_1, option_2=option_2)

                self.__handling_update_fd_index(value1=DataValidation3().check_invalid(SessionManager().get_setter_state(key='dataframe_inline')), 
                                                value2=DataValidation3().check_invalid(SessionManager().get_setter_state(key='dataframe_noninline')),
                                                df1=df1, df2=df2, list_index1=list_index1, list_index2=list_index2) 
            
            else :
                ComponentsDataMonitoring().run(data1=SessionManager().get_setter_state(key='invalid_inline'), data2=SessionManager().get_setter_state(key='valid_inline'))
                df1 = ComponentsDataFrame().display_dataframe(value=SessionManager().get_setter_state(key='dataframe_inline'), column_configs=ComponentsDataFrame().table_inline())

                ComponentsDataMonitoring().run(data1=SessionManager().get_setter_state(key='invalid_noninline'), data2=SessionManager().get_setter_state(key='valid_noninline'))
                df2 = ComponentsDataFrame().display_dataframe(value=SessionManager().get_setter_state(key='dataframe_noninline'), column_configs=ComponentsDataFrame().table_noninline())

                
                try : 
                    self.__handling_update_fd(DataValidation3().check_invalid(SessionManager().get_setter_state(key='dataframe_inline')), 
                                               DataValidation3().check_invalid(SessionManager().get_setter_state(key='dataframe_noninline')), 
                                               df1, df2, SessionManager().get_setter_state(key='type_form'), uploaded_file=uploaded_file) 
                
                except Exception as e : 
                    st.error(f"Error in WorkflowManagerAddData (__handling_update_fd) : {e}")
        
        except Exception as e : 
            st.error(f"Error in class WorkflowManagerAddData (handling_filter_fd) : {e}")

    def handling_filter_fpd(self, option_1, option_2, uploaded_file): 
        """
        This function will be show data by filter (Dataframe First Pass Defects)
        -----------------------------------------------------------------------
        Parameter : <br>
            - option_1 : Type filter (Halaman) <br>
            - option_2 : Type filter (Tipe Invalid) <br>
            - uploaded_file : Input file from Users <br>
        """
        try : 
            if (len(option_1) == 0 or option_1 == "None") and len(option_2) != 0:
                #print(f"Hai ini handling_filter_fpd elif Nomor 1") 
                ComponentsStyle().alert_filter("Halaman") 
            
            elif (len(option_1) != 0 and option_1 != "None") and len(option_2) == 0:
                #print(f"Hai ini handling_filter_fpd elif Nomor 2")
                ComponentsStyle().alert_filter("Tipe Invalid") 
            
            elif (len(option_1) != 0 or option_1 != "None") and len(option_2) != 0:   
                ComponentsDataMonitoring().run(data1=SessionManager().get_setter_state(key='invalid_fpd'), data2=SessionManager().get_setter_state(key='valid_fpd'))

                df1, list_index1 = self.__handling_filter_fpd(option_1=option_1, option_2=option_2)

                self.__handling_update_fpd_index(value1=DataValidation3().check_invalid(SessionManager().get_setter_state(key='dataframe_fpd')),
                                                 df=df1, list_index=list_index1)
            
            else :   
                #print(f"Hai ini handling_filter_fpd else ")  
                ComponentsDataMonitoring().run(data1=SessionManager().get_setter_state(key='invalid_fpd'), data2=SessionManager().get_setter_state(key='valid_fpd'))

                df = ComponentsDataFrame().display_dataframe(value=SessionManager().get_setter_state(key='dataframe_fpd'), column_configs=ComponentsDataFrame().table_firstpass())
                #print(f"Hai ini handling_filter_fpd elif else after ComponentsDataFarme")

                try :  
                    self.__handling_update_fpd(value1=DataValidation3().check_invalid(SessionManager().get_setter_state(key='dataframe_fpd')), 
                                               df_value=df, type_form=SessionManager().get_setter_state(key='form_type'), uploaded_file=uploaded_file) 
                
                except Exception as e :
                    st.error(f"Error in class WorkflowManagerAddData function handling_filter_fpd (__handling_update_fpd) : {e}")
        
        except Exception as e : 
            st.error(f"Error in class WorkflowManagerAddData (handling_filter_fpd) : {e}")  
    
    def __handling_update_fd(self, value1, value2, df1, df2, type_form, uploaded_file):
        """
        This function will be processing like Save Dataframe Final Defects after manipulation. <br> 
        ---------------------------------------------------------------------------------------
        Parameter : <br> 
            - value1 : The Value of Check Invalid in DataFrame Inline Repair <br>
            - value2 : The Value of Check Noninvalid in DataFrame Noninline Repair <br>
            - df1 : DataFrame Inline Repair <br> 
            - df2 : DataFrame Noninline Repair <br>
            - type_form : Type Form of Input Users <br>
        """
        try : 
            if value1 or value2 : 
                if ComponentsButton().button_update(): 
                    SessionManager().set_setter_state(key='dataset_name', value=f"FRM-QC-026_rev3_{datetime.now().strftime('%Y-%m-%d')}_Final_Defects_Merge_File.pdf")
                    SessionManager().set_setter_state(key='dataframe_inline', value=df1)
                    SessionManager().set_setter_state(key='dataframe_noninline', value=df2)

                    df_invalid1 = DataValidation3().find_index_error1(SessionManager().get_setter_state(key='dataframe_inline'), type_form=type_form) 
                    df_invalid2 = DataValidation3().find_index_error2(SessionManager().get_setter_state(key='dataframe_noninline')) 

                    if df_invalid1 or df_invalid2 : 
                        ComponentsStyle().warning_alert3(value=True, page1=df_invalid1, page2=df_invalid2) 
                    
                    else : 
                        ComponentsStyle().warning_alert2(True) 

                ComponentsButton().button_save_merge(type_form=type_form) 
            
            else : 
                if ComponentsButton().button_download(): 
                    now_end = datetime.now()
                    SessionManager().generate_dataframe('dataframe_users', 1, 6, "User_Name", "Name", "Nik", "Location", "Role", "Login_Time") 

                    SessionManager().set_setter_state(key='User_Name', value=SessionManager().get_setter_state(key='username'), df='dataframe_users')
                    SessionManager().set_setter_state(key='Name', value=SessionManager().get_setter_state(key='name'), df='dataframe_users')
                    SessionManager().set_setter_state(key='Nik_Nipm', value=SessionManager().get_setter_state(key='nik_nipm'), df='dataframe_users') 
                    SessionManager().set_setter_state(key='Location', value=SessionManager().get_setter_state(key='location'), df='dataframe_users')
                    SessionManager().set_setter_state(key='Role', value=SessionManager().get_setter_state(key='role'), df='dataframe_users')
                    SessionManager().set_setter_state(key='Login_Id', value=SessionManager().get_setter_state(key='login_id'), df='dataframe_users')

                    ## Create Data File Name
                    data = SessionManager().get_setter_state(key='dataframe_noninline')
                    data[['title', 'file_name_dataset']] = ['Final Defects', SessionManager().get_setter_state(key='dataset_name')] 
                    data['start_processing'] = SessionManager().get_setter_state(key='start_processing')
                    data['end_processing'] = now_end
                    data['time_processing_all'] = SessionManager().get_setter_state(key='sum_processing')
                    data['time_processing_page'] = SessionManager().get_setter_state(key='processing_page')
                    data['login_id'] = SessionManager().get_setter_state(key='login_id')

                    ## Join With Dataset 
                    df_join = pd.concat([SessionManager().get_setter_state(key='dataframe_noninline'), SessionManager().get_setter_state(key='dataframe_polygon')], axis=1)
                    SessionManager().set_setter_state(key='dataframe_noninline', value=df_join) 

                    ## Lower Case Column Names
                    
                    ## Save Data
                    SessionManager().get_setter_state('dataframe_inline').to_csv(f"{ControllerPath().path_fd_inline}\\{FileManager().inline_name(SessionManager().get_setter_state('dataframe_inline'))}", index=False) 
                    SessionManager().get_setter_state('dataframe_noninline').to_csv(f"{ControllerPath().path_fd_noninline}\\{FileManager().noninline_name(SessionManager().get_setter_state('dataframe_noninline'))}", index=False) 
                    SessionManager().get_setter_state('dataframe_users').to_csv(f"{ControllerPath().path_login_users}\\{FileManager().uinteraction_name(SessionManager().get_setter_state('dataframe_users'))}", index=False)

                    SessionManager().get_setter_state('dataframe_inline').to_sql('fd_inline', con=DatabaseConfig().connect_to_db(), if_exists='append', index=False, dtype=DatabaseConfig().mapping_fd_inline()) 
                    SessionManager().get_setter_state('dataframe_noninline').to_sql('fd_noninline', con=DatabaseConfig().connect_to_db(), if_exists='append', index=False, dtype=DatabaseConfig().mapping_fd_noninline()) 
                    SessionManager().get_setter_state('dataframe_users').to_sql('users_activity', con=DatabaseConfig().connect_to_db(), if_exists='append', index=False, dtype=DatabaseConfig().mapping_users_activity()) 

                    ## Notification Pop Up 
                    ComponentsStyle().display_done(True)
                    time.sleep(0.5)
                    SessionManager().reset_session(['login_condition'])
                
                if SessionManager().get_setter_state(key='error_page'): 
                    DataProblemScanning().run(SessionManager().get_setter_state(key='pdf_input'), SessionManager().get_setter_state(key='error_page'), FileManager().get_format_name(SessionManager().get_setter_state(key='dataframe_fpd')), type_form) 
                
                ComponentsButton().button_save_merge(type_form=type_form)

        except Exception as e : 
            st.error(f"Error in class WorkflowManagerAddData (__handling_update_fd) : {e}")

    def __handling_update_fpd(self, value1, df_value, type_form, uploaded_file): 
        """
        This function will be processing like Save DataFrame First Pass Defects after manipulation. <br>
        ---------------------------------------------------------------------------------------------
        Parameter : 
            - value1 : The Value of Check Invalid in DataFrame Fist Pass Defects. <br>
            - df_value : Dataframe First Pass Defects. <br>
            - type_form : Type Form from Users. <br>
        """
        try : 
            if value1:
                if ComponentsButton().button_update(): 
                    SessionManager().set_setter_state(key='dataset_name', value=f"FRM-QC-026_rev3_{datetime.now().strftime('%Y-%m-%d')}_First_Pass_Defects_Merge_File.pdf") 
                    SessionManager().set_setter_state(value=df_value, key='dataframe_fpd') 

                    error_list = DataValidation3().find_index_error1(SessionManager().get_setter_state(key='dataframe_fpd'), type_form)

                    ComponentsStyle().warning_alert2(True) 
                
                ComponentsButton().button_save_merge(type_form=type_form)  
            
            else : 
                if ComponentsButton().button_download(): 
                    now_end = datetime.now()
                    st.write(now_end)
                    st.write(SessionManager().get_setter_state(key='start_processing'))
                    SessionManager().generate_dataframe('dataframe_users', 1, 6, "User_Name", "Name", "Nik", "Location", "Role", "Login_Time") 

                    SessionManager().set_setter_state(key='User_Name', value=SessionManager().get_setter_state(key='username'), df='dataframe_users')
                    SessionManager().set_setter_state(key='Name', value=SessionManager().get_setter_state(key='name'), df='dataframe_users')
                    SessionManager().set_setter_state(key='Nik_Nipm', value=SessionManager().get_setter_state(key='nik_nipm'), df='dataframe_users')
                    SessionManager().set_setter_state(key='Location', value=SessionManager().get_setter_state(key='location'), df='dataframe_users')
                    SessionManager().set_setter_state(key='Role', value=SessionManager().get_setter_state(key='role'), df='dataframe_users')
                    SessionManager().set_setter_state(key='Login_Id', value=SessionManager().get_setter_state(key='login_id'), df='dataframe_users')

                    st.dataframe(SessionManager().get_setter_state(key='dataframe_users')) 

                    ## Create Data File Name 
                    data = SessionManager().get_setter_state(key='dataframe_fpd')
                    data[['title', 'file_name_dataset']] = ['First Pass Defects', SessionManager().get_setter_state(key='dataset_name')] 
                    data['start_processing'] = SessionManager().get_setter_state(key='start_processing')
                    data['end_processing'] = now_end 
                    data['time_processing_all'] = SessionManager().get_setter_state(key='sum_processing')
                    data['time_processing_page'] = SessionManager().get_setter_state(key='processing_page')
                    data['login_id'] = SessionManager().get_setter_state(key='login_id')

                    ## Join With Dataset  
                    df_join = pd.concat([SessionManager().get_setter_state(key='dataframe_fpd'), SessionManager().get_setter_state(key='dataframe_polygon')], axis=1)
                    SessionManager().set_setter_state(key='dataframe_fpd', value=df_join)
                    print(f"Ini After df_join") 

                    ## Save Data 
                    SessionManager().get_setter_state(key='dataframe_fpd').to_csv(f"{ControllerPath().path_fpd}\\{FileManager().firstpasss_name(SessionManager().get_setter_state(key='dataframe_fpd'))}", index=False) 
                    SessionManager().get_setter_state(key='dataframe_users').to_csv(f"{ControllerPath().path_login_users}\\{FileManager().uinteraction_name(SessionManager().get_setter_state(key='dataframe_users'))}", index=False)

                    ## Notification Pop Up
                    ComponentsStyle().display_done(True) 
                    time.sleep(0.5) 
                    SessionManager().reset_session(['']) 
                
                if SessionManager().get_setter_state(key='error_page'): 
                    DataProblemScanning().run(SessionManager().get_setter_state(key='pdf_input'), SessionManager().get_setter_state(key='error_page'), FileManager().get_format_name(SessionManager().get_setter_state(key='dataframe_fpd')), type_form) 
                
                ComponentsButton().button_save_merge(type_form=type_form)
        
        except Exception as e : 
            st.error(f"Error in class WorkflowManagerAddData (__handling_update_fpd) : {e}")


    def __handling_update_fd_index(self, value1, value2, df1, df2, list_index1, list_index2): 
        """ 
        Handling Update Data By Filter Button. <br>
        ------------------------------------------------------------------------
        Parameter : <br>
            - value1 : The Value of Check Invalid in DataFrame Inline Repair <br>
            - value2 : The Value of Check Invalid in DataFrame Noninline Repair <br>
            - df1 : DataFrame Inline Repair Update <br>
            - df2 : DataFrame Noninline Repair Update <br>
            - list_index1 : The List of Index Update Data Inline Repair <br> 
            - list_index2 : The List of Index Update Data Noninline Repair <br>
        """
        try : 
            if value1 or value2 : 
                if ComponentsButton().button_update():
                    SessionManager().set_dataframe_index(df='dataframe_inline', index=list_index1, df_new=df1)
                    SessionManager().set_dataframe_index(df='dataframe_noninline', index=list_index2, df_new=df2)

                    list_error1 = DataValidation3().find_index_error1(SessionManager.get_setter_state(key='dataframe_inline'))
                    list_error2 = DataValidation3().find_index_error1(SessionManager.get_setter_state(key='dataframe_noninline'))

                    if list_error1 or list_error2:
                        ComponentsStyle().warning_alert3(True, list_error1, list_error2) 
                    
                    else : 
                        ComponentsStyle().warning_alert2(True)

        except Exception as e : 
            st.error(f"Error in class WorkflowManagerAddData (_handling_update_fd_index) : {e}") 

    def __handling_update_fpd_index(self, value1, df, list_index) : 
        """
        Handling update data berdasarkan filter button <br>
        -----------------------------------------------------------
        Parameter : <br>
            - value1 : Is Condition if There is Invalid Type in Specific Index (Halaman), Then return True in dataframe first pass defects. <br>
            - df : Is Dataframe and There is Invalid Type. <br>
            - list_index : List Index of Invalid Type (In Specific index), will be return index if there is Invalid Type. <br>
        """
        try : 
            if value1 :
                if ComponentsButton().button_update():
                    SessionManager().set_dataframe_index(df='dataframe_fpd', index=list_index, df_new=df)
                    ComponentsStyle().warning_alert2(True) 

        except Exception as e : 
            st.error(f"Error in class WorkflowManagerAddData (_handling_update_fpd_index) : {e}")
    
    def __handling_filter_inline(self, option_1: str, option_2: str):
        """
        Will be Filter Specific Data in DataFrame by Option Filter <br>
        ---------------------------------------------------------------------
        Parameter : 
            - option_1 : Type of Filter (Halaman) <br>
            - option_2 : Type of Filter (Type Invalid) <br>
        """
        try : 
            mask_halaman = SessionManager().get_dataframe(df='dataframe_inline', key='Halaman', value=option_1)
            mask_value = SessionManager().has_dataframe(df='dataframe_inline').isin(option_2).any(axis=1) 

            combine_mask = mask_halaman & mask_value 

            df = ComponentsDataFrame().display_dataframe(value=SessionManager().get_setter_state('dataframe_inline')[combine_mask], column_configs=ComponentsDataFrame().table_inline()) 

            list_index = df.index.tolist()

            return df, list_index

        except Exception as e : 
            st.error(f"Error in class WorkflowManagerAddData (__handling_filter_inline) : {e}")
    
    def __handling_filter_noninline(self, option_1: str, option_2: str):
        """
        This Function will be Show Data by Filter from Users <br>
        ---------------------------------------------------------------
        Parameter : <br>
            - option_1 : Type Filter (Halaman) <br>
            - option_2 : Type Filter (Tipe Invalid) <br>
        """
        try : 
            mask_halaman = SessionManager().get_dataframe(df='dataframe_noninline', key='Halaman', value=option_1)
            mask_value = SessionManager().has_dataframe(df='dataframe_noninline').isin(option_2).any(axis=1)

            combine_mask = mask_halaman & mask_value 

            df = ComponentsDataFrame().display_dataframe(value=SessionManager().get_setter_state('dataframe_noninline')[combine_mask], column_configs=ComponentsDataFrame().table_noninline())

            list_index = df.index.tolist()

            return df, list_index 

        except Exception as e : 
            st.error(f"Error in class WorkflowManagerAddData (__handling_filter_noninline) : {e}")
    
    def __handling_filter_fpd(self, option_1: str, option_2: str):
        """
        This Function will be Show Data by Filter from Users. <br>
        Parameter : <br> 
            - option_1 : Type Filter (Halaman) <br> 
            - option_2 : Type Filter (Tipe Invalid) <br> 
        """
        try : 
            mask_halaman = SessionManager().get_dataframe(df='dataframe_fpd', key='Halaman', value=option_1)
            mask_value = SessionManager().has_dataframe(df='dataframe_fpd').isin(option_2).any(axis=1) 

            combine_mask = mask_halaman & mask_value 

            df = ComponentsDataFrame().display_dataframe(SessionManager().get_setter_state('dataframe_fpd')[combine_mask], ComponentsDataFrame().table_firstpass())

            list_index = df.index.tolist()

            return df, list_index

        except Exception as e : 
            st.error(f"Error in class WorkflowManagerAddData (__handling_filter_fpd) : {e}")
    
    def handling_generate_data(self, inp_form, inp_model, inp_no, inp_date, inp_shift):
        """"""
        part_name = list(ControllerPath().database_part_check[inp_model][inp_no].keys())[0] 
        check_points = list(ControllerPath().database_part_check[inp_model][inp_no].values())[0]
        df_1 = pd.DataFrame({
                    'Halaman' : ['Halaman 1'] * int(check_points), 
                    'Model': [inp_model] * int(check_points),
                    'Part No': [inp_no] * int(check_points), 
                    'Part Name': [part_name] * int(check_points),
                    'Ttd Kasie': [' '] * int(check_points),
                    'Ttd Operator': [' '] * int(check_points),
                    'Nik Operator': [' '] * int(check_points), 
                    'Tahun': [str(inp_date.year)] * int(check_points),
                    'Bulan': [inp_date.month] * int(check_points),
                    'Tanggal': [inp_date.day] * int(check_points), 
                    'Shift': [inp_shift] * int(check_points),
                    'Welding Check Points': list(range(1, int(check_points)+1)),
                    'Keropos': [' '] * int(check_points),
                    'Kurang': [' '] * int(check_points), 
                    'Bolong': [' '] * int(check_points),
                    'Undercut': [' '] * int(check_points),
                    'Spatter': [' '] * int(check_points), 
                    'Tidak Tepat': [' '] * int(check_points)
                }) 
                            
        df_2 = pd.DataFrame({
                    'Halaman' : ['Halaman 1'],
                    'Model': [inp_model],
                    'Part No': [inp_no],
                    'Part Name': [part_name],
                    'Ttd Kasie': [' '],
                    'Ttd Operator': [' '], 
                    'Nik Operator': [' '], 
                    'Tahun': [str(inp_date.year)], 
                    'Bulan': [inp_date.month],  
                    'Tanggal': [inp_date.day],
                    'Shift': [inp_shift],
                    "Folding Keras": [' '],
                    "Karat": [' '],
                    "Deformasi": [' '],
                    "Cat_Coating": [' '],
                    "Tidak Masuk Gonogo": [' '],
                    "Step Loss": [' '],
                    "Step Loncat": [' '],
                    "Step Lebih": [' '],
                    "Step Kurang": [' '],
                    "Salah Pasang": [' '],
                    "Goresan": [' '],
                    "Noisy": [' '],
                    "Tidak Lengkap": [' '],
                    'Checked': [' '],
                    'Ok': [' '],
                    'Repair': [' '], 
                    'Scrap': [' '],
                    'Catatan': [' ']
                })
        
        df_3 = pd.DataFrame({ 
                    'Halaman' : ['Halaman 1'],
                    'Model' : [inp_model],
                    'Part No' : [inp_no],
                    'Part Name' : [part_name],
                    'Part Group' : [' '],
                    'Shift' : [inp_shift],
                    'Tahun' : [str(inp_date.year)],
                    'Bulan' : [inp_date.month],
                    'Tanggal' : [inp_date.day],
                    'Nik_Nipm' : [' '],
                    'Total Repair' : [' '],
                    'Total Top' : [' '],
                    'Total Middle' : [' '],
                    'Total Bottom' : [' ']
                }) 
            
        SessionManager().set_setter_state(key='part_name_manual', value=part_name)
        SessionManager().set_setter_state(key='dataframe_manual_fd_inline', value=df_1)
        SessionManager().set_setter_state(key='dataframe_manual_fd_noninline', value=df_2)
        SessionManager().set_setter_state(key='dataframe_manual_fpd', value=df_3)
        SessionManager().set_setter_state(key='inp_date_manual', value=inp_date) 
        SessionManager().set_setter_state(key='inp_shift_manual', value=inp_shift) 

    
    def handling_manual_input(self, inp_form, inp_model, inp_no, inp_date, inp_shift):
        """
        This Function will be handling input manual from users <br>
        ---------------------------------------------------------------------
        Paremater : 
            - inp_form  : Input Type Form from Users <br>
            - inp_model : Input Type Model from Users <br>
            - inp_no    : Input Part No from Users <br>
            - inp_date  : Input Date from Users <br>
            - inp_shift : Input Shift from Users <br>
        """
        try : 
            self.handling_generate_data(inp_form=inp_form, inp_model=inp_model, inp_no=inp_no, inp_date=inp_date, inp_shift=inp_shift)
            if inp_form == "Final Defects" :
                st.write("-------------------------------------------------")

                ComponentsStyle().display_result2(f"Tambahkan Data {SessionManager().get_setter_state(key='part_name_manual')}")

                dff_1 = ComponentsDataFrame().display_dataframe(value=SessionManager().get_setter_state(key='dataframe_manual_fd_inline'), column_configs=ComponentsDataFrame().table_inline())
                dff_2 = ComponentsDataFrame().display_dataframe(value=SessionManager().get_setter_state(key='dataframe_manual_fd_noninline'), column_configs=ComponentsDataFrame().table_noninline())

                if ComponentsButton().button_download():
                    path_save_1 = f"DF_FinalDefects_Inline_ID_{SessionManager().get_setter_state(key='part_name_manual')}_{SessionManager().get_setter_state(key='inp_date_manual')}_{SessionManager().get_setter_state(key='inp_shift_manual')}_.csv"
                    path_save_2 = f"DF_FinalDefects_Noninline_ID_{SessionManager().get_setter_state(key='part_name_manual')}_{SessionManager().get_setter_state(key='inp_date_manual')}_{SessionManager().get_setter_state(key='inp_shift_manual')}_.csv"

                    ## Add Several Data
                    dff_2[['table_1', 'table_2', 'table_3', 'table_4', 'table_5', 'table_6', 'title', 'file_name_dataset', 'start_processing', 'end_processing', 'time_processing_all', 'time_processing_page']] = ['', '', '', '', '', '', 'Final Defects', '', '', '', '', '']

                    ## Save Data
                    dff_1.to_csv(f"{ControllerPath().path_fd_inline}\\{path_save_1}", index=False) 
                    dff_2.to_csv(f"{ControllerPath().path_fd_noninline}\\{path_save_2}", index=False) 
                    ComponentsStyle().display_done(True) 
                    time.sleep(0.5) 
                
            else :  
                st.write("-------------------------------------------------")
                ComponentsStyle().display_result2(f"Tambahkan Data {SessionManager().get_setter_state(key='part_name_manual')}")  

                dff_3 = ComponentsDataFrame().display_dataframe(value=SessionManager().get_setter_state(key='dataframe_manual_fpd'), column_configs=ComponentsDataFrame().table_firstpass())   

                if ComponentsButton().button_download():
                    path_save_3 = f"DF_FirstPassDefects_ID_{SessionManager().get_setter_state(key='part_name_manual')}_{SessionManager().get_setter_state(key='inp_date_manual')}_{SessionManager().get_setter_state(key='inp_shift_manual')}_.csv" 

                    ## Add Several Data
                    dff_3[['table_1', 'table_2', 'title', 'file_name_dataset', 'start_processing', 'end_processing', 'time_processing_all', 'time_processing_page']] = ['', '', 'First Pass Defects', '', '', '', '', '']

                    ## Save Data 
                    dff_3.to_csv(f"{ControllerPath().path_fpd}\\{path_save_3}", index=False)
                    ComponentsStyle().display_done(True) 
                    time.sleep(0.5) 

        except Exception as e : 
            st.error(f"Error in class WorkflowManagerAddData (handling_manual_input) : {e}")