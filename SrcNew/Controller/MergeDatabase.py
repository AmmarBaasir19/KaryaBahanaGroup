import streamlit as st 
import pandas as pd 
import os 
import glob
from SrcNew.Controller.ControllerPath import ControllerPath

class MergeDatabase:
    def __init__(self):
        """"""
        try : 
            try :
                if not os.path.exists(ControllerPath().folder_output_calender_fd): 
                    os.makedirs(ControllerPath().folder_output_calender_fd) 

                else : 
                    for file_name in os.listdir(ControllerPath().folder_output_calender_fd): 
                        file_path = os.path.join(ControllerPath().folder_output_calender_fd, file_name) 
                        try : 
                            if os.path.isfile(ControllerPath().folder_path_fd_noninline):
                                os.remove(ControllerPath().folder_path_fd_noninline) 
                        
                        except Exception as e : 
                            st.error(f"Error in Processing Remove File Final Defects") 
                
                all_csv_file = glob.glob(os.path.join(ControllerPath().folder_path_fd_noninline, "*.csv"))

                ## Read File Csv  
                df_list = [pd.read_csv(file) for file in all_csv_file]  
                combined_df = pd.concat(df_list, ignore_index=True) 
                output_file_1 = os.path.join(ControllerPath().folder_output_calender_fd, f"Master_Activity_FD.csv")

                ## Save Merge Result
                combined_df.to_csv(output_file_1, index=False) 

            except Exception as e : 
                st.error(f"Error in MergeDatabase (__init__) Processing Final Defects : {e}") 
            
            try : 
                if not os.path.exists(ControllerPath().folder_output_calender_fpd):  
                    os.makedirs(ControllerPath().folder_output_calender_fpd) 

                else : 
                    for file_name in os.listdir(ControllerPath().folder_output_calender_fpd): 
                        file_path = os.path.join(ControllerPath().folder_output_calender_fpd, file_name) 
                        try : 
                            if os.path.isfile(file_path):
                                os.remove(file_path) 

                        except Exception as e : 
                            st.error(f"Error in Processing Remove File First Pass Defects") 
                
                all_csv_file = glob.glob(os.path.join(ControllerPath().folder_path_fpd, "*.csv")) 

                ## Read File Csv 
                df_list = [pd.read_csv(file) for file in all_csv_file] 
                combined_df = pd.concat(df_list, ignore_index=True) 
                output_file_2 = os.path.join(ControllerPath().folder_output_calender_fpd, f"Master_Activity_FPD.csv")

                ## Save Merge Result
                combined_df.to_csv(output_file_2, index=False) 

            except Exception as e : 
                st.error(f"Error in MergeDatabase (__init__) Processing First Pass Defects : {e}") 
        
        except Exception as e : 
            st.error(f"Error in MergeDatabase (__init__) : {e}")