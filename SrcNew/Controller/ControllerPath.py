import streamlit as st 
import json
import yaml 

class ControllerPath:
    def __init__(self):
        """"""
        try : 
            with open("Configs/config.yaml", "r") as file: 
                config = yaml.safe_load(file)
            
            self.api_keys = config.get("api_adi").get("keys_api") 
            self.api_endpoint = config.get("api_adi").get("path_api") 

        except Exception as e : 
            st.error(f"Error in class ControllerPath (Open config.yaml) : {e}") 

        try : 
            with open("Configs/Data.json", "r") as file1:
                data_tab = json.load(file1) 

        
            ## Set Columns Name for Final Defects and First Pass Defects
            self.table_1_fd = data_tab['data_table']['format_fd']['table_1']
            self.table_2_fd = data_tab['data_table']['format_fd']['table_2']
            self.table_3_fd = data_tab['data_table']['format_fd']['table_3']
            self.table_4_fd = data_tab['data_table']['format_fd']['table_4']
            self.table_5_fd = data_tab['data_table']['format_fd']['table_5']
            self.table_1_fpd = data_tab['data_table']['format_fpd']['table_1']
            self.table_2_fpd = data_tab['data_table']['format_fpd']['table_2']


            ## Set Directory Path to Save Data
            self.path_fd_inline = data_tab['directory_path'][0]['dir_path1']['path']
            self.path_fd_noninline = data_tab['directory_path'][0]['dir_path2']['path']
            self.path_login_users = data_tab['directory_path'][0]['dir_path3']['path']
            self.path_reports = data_tab['directory_path'][0]['dir_path4']['path']
            self.path_fpd = data_tab['directory_path'][0]['dir_path5']['path']
            self.path_merge = data_tab['directory_path'][0]['dir_path6']['path'] 


            ## Set Columns Name Format
            self.inline = ["Halaman"] + self.table_1_fd["columns_name"] + self.table_2_fd["columns_name"] + self.table_4_fd["columns_name"]
            self.noninline = ["Halaman"] + self.table_1_fd["columns_name"] + self.table_2_fd["columns_name"] + self.table_5_fd['columns_name'] + self.table_3_fd['columns_name'] + ["Catatan Problem"]
            self.firstpass = ["Halaman"] + self.table_1_fpd["columns_name"] + self.table_2_fpd["columns_name"]

            ## For Generate Data Synthetics
            self.columns_polygon_fd = ['Table_1', 'Table_2', 'Table_3', 'Table_4', 'Table_5', 'Table_6']
            self.columns_polygon_fpd = ['Table_1', 'Table_2']


            ## Set Manual Final Defects
            #self.

            ## Set Invalid Type 
            self.invalid_type = data_tab['data_invalid']['invalid_type']

            ## Part Name and Part No
            self.part_name = data_tab['data_part'][0]['part_name']
            self.part_no = data_tab['data_part'][0]['part_no']

            self.database_part = data_tab['database_parts']
            self.database_part_check = data_tab['database_parts_check'][0]

            # Set Database users
            self.users = data_tab['login_data']

            # set path merge reports
            self.folder_path_fpd = "home\cortex\Medallion_Hub\Karya_Bahana_Apps\First_Pass_Def"
            self.folder_path_fd_noninline = "home\cortex\Medallion_Hub\Karya_Bahana_Apps\FD_Noninline_Repair"
            self.folder_output_fd = "home\cortex\Medallion_Hub\Karya_Bahana_Apps\Master_FD"
            self.folder_output_fpd = "home\cortex\Medallion_Hub\Karya_Bahana_Apps\Master_FPD"

            ## Set Path Beranda Page
            self.folder_output_calender = "home\cortex\Medallion_Hub\Karya_Bahana_Apps\Calender_DB" 
            self.folder_output_calender_fd = "home\cortex\Medallion_Hub\Karya_Bahana_Apps\Calender_DB\FD" 
            self.folder_output_calender_fpd = "home\cortex\Medallion_Hub\Karya_Bahana_Apps\Calender_DB\FPD" 
        
        except Exception as e : 
            st.error(f"Error in class ControllerPath (__init__) : {e}")