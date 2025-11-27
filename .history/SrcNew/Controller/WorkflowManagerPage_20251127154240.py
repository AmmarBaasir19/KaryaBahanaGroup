import streamlit as st 
import time
import os 
import glob
import pandas as pd 
from io import BytesIO 
from PyPDF2 import PdfMerger 
from SrcNew.Controller.ControllerPath import ControllerPath
from SrcNew.Model.SessionManager import SessionManager
from SrcNew.View.ComponentsStyle import ComponentsStyle
from SrcNew.Controller.MergeData import MergeData
from SrcNew.View.ComponentsButton import ComponentsButton
from SrcNew.View.ComponentsUserInput import ComponentsUserInput
from SrcNew.GenerateReports.MainAutomaticReports import MainAutomaticReports
from SrcNew.GenerateReports.StylingReports import StylingReports
from SrcNew.Controller.WorkflowManagerAddData import WorkflowManagerAddData
from SrcNew.View.ComponentsShiftInput import ComponentsShiftInput
from SrcNew.View.ComponentsDataFrame import ComponentsDataFrame 
from SrcNew.Controller.MergeDatabase import MergeDatabase
from SrcNew.Model.MainCalender import MainCalender 
from SrcNew.Model.DatabaseConfig import DatabaseConfig



class WorkflowManagerPage:
    def render_beranda(self):
        """ This Function will be Processing Beranda Page """
        try : 
            MainCalender().run()
            st.write("Hai")

        except Exception as e : 
            st.error(f"Error in class WorkflowManagerPage (render_beranda) : {e}") 
    
    def render_generate_reports(self): 
        """ This Function will be Processing Automatic Generate Reports """
        try : 
            val_format, val_start, val_end, val_click = ComponentsUserInput().reports_input(label="Buat Reports")

            if val_format != "None" and val_click == True:
                st.write(" ") 
                st.write(" ") 
                st.write(" ") 
                progress_text = "Sedang Membuat Reports, Harap Tunggu Beberapa Detik......"
                my_bar = st.progress(0, text=progress_text) 

                for percent_complete in range(100):
                    time.sleep(0.03) 
                    my_bar.progress(percent_complete + 1, text=progress_text)   
                time.sleep(1) 
                my_bar.empty() 

                
                ## Read Database to Generate Reports
                col_df1 = ['model', 'part_no', 'part_name', 'shift', 'tahun', 'bulan', 'tanggal', 'checked', 'ok', 'repair', 'scrap']
                col_df2 = ['model', 'part_no', 'part_name', 'shift', 'total_repair', 'tahun', 'bulan', 'tanggal']

                df1 = DatabaseConfig().get_database(start_date=val_start, end_date=val_end, db_name='fd_noninline', col_name=col_df1)
                #pd.read_csv(output_file_1, usecols=['Model', 'Part No', 'Part Name', 'Shift', 'Tahun', 'Bulan', 'Tanggal', 'Checked', 'Ok', 'Repair', 'Scrap'])

                df2 = DatabaseConfig().get_database(start_date=val_start, end_date=val_end, db_name='fpd', col_name=col_df2)
                #pd.read_csv(output_file_2, usecols=['Model', 'Part No', 'Part Name', 'Shift', 'Tahun', 'Bulan', 'Tanggal', 'Total Repair', 'Total Top', 'Total Middle', 'Total Bottom']) 
                
                ## Generate Reports
                wb = MainAutomaticReports().run(df1=df1, df2=df2, option=val_format, start_date=val_start, end_date=val_end)

                ## Add Styling Reports
                wb_final = StylingReports().run(wb, 1, len(wb.columns) - 3, 4, len(wb.columns) + 1, val_format)

                ## Download Button
                ComponentsButton().button_download_reports(wb_final, val_start, val_end)
        
        except Exception as e : 
            st.error(f"Error in class WorkflowManagerPage (render_buat_reports) : {e}") 
    
    def render_add_data(self):
        """ This Function will be Processing Form with OCR Model """
        uploaded_file = ComponentsStyle().display_uploaded(True)   

        if len(uploaded_file) != 0 : 
            if not SessionManager().get_setter_state('button_auto'):
                WorkflowManagerAddData().handling_date_input()
            
            else :  
                try :   
                    merger = PdfMerger()    
                    for pdf_file in uploaded_file:
                        merger.append(pdf_file) 

                    output = "Temporary/File_PDF.pdf" 
                    merger.write(output) 
                    merger.close()

                    SessionManager().set_setter_state(key='pdf_input', value=output)

                    form_type = SessionManager().get_setter_state(key='form_type')
                    if SessionManager().has_key(key='dataframe_loaded') == False : 
                        print(f"Before _handling_scanning_data") 
                        WorkflowManagerAddData().handling_scanning_data(uploaded_file=uploaded_file, type_form=form_type) 
                        SessionManager().set_setter_state(key='dataframe_loaded', value=True)
                        #print(f"Ini After WorkflowManagerPage : {SessionManager().get_setter_state(key='dataframe_fpd')}") 
                        ## Additional DF 

                    else : 
                        pass

                    print(f"Ini sebelum check_date_values_empty")  
                    if SessionManager().check_date_values_empty() :
                        print(f"Ini After check_date_values_empty()")
                        ComponentsStyle().display_warning(
                            "Harap Masukkan Data Tahun, Bulan, Tanggal dan Tipe Form Yang Sesuai Dengan Form"
                        )
                        WorkflowManagerAddData().handling_date_input()
                        ComponentsStyle().display_result() 
                    
                    else : 
                        print(f"Ini sebelum state_key2")
                        state_key2 = SessionManager().get_setter_state(key="dataframe_inline") if form_type == "Final Defects" else SessionManager().get_setter_state(key="dataframe_fpd") 

                        print(f"Ini sebelum WorkflowManagerAddData().handling_date_in_df(form_type)")
                        WorkflowManagerAddData().handling_date_in_df(form_type) 
                        print(f"Ini sebelum WorkflowManagerAddData().handling_quality_data(form_type)") 
                        WorkflowManagerAddData().handling_quality_data(form_type)   
                        
                        halaman, shift, btn_shift = ComponentsShiftInput().display_input(state_key2, "Perbarui Shift") 
                        print(f"Ini sebelum WorkflowManagerAddData().handling_quality_data(form_type)") 

                        option_1, option_2 = ComponentsStyle().filter_selected(form_type)

                        if form_type == "Final Defects" :
                            WorkflowManagerAddData().handling_filter_fd(option_1, option_2, uploaded_file)

                        else :
                            WorkflowManagerAddData().handling_filter_fpd(option_1, option_2, uploaded_file)  
                
                except Exception as e :  
                    st.error(f"Error in class WorkflowManagerPage (render_add_data) : {e}")  
    

    def render_merge_data(self): 
        """ This Function Will be Processing Merge PDF from Input Users """
        try : 
            result_merge = MergeData().run() 
            SessionManager().set_setter_state('MergeData_Path', result_merge)  
            SessionManager().set_setter_state('MergeData', True) 

        except Exception as e :  
            st.error(f"Error in class WorkflowManagerPage (_render_gabungkan_data) : {e}")

            
    def render_manual_data(self): 
        """ This Function Will be Processing Merge PDF from Input Users """
        try : 
            inp_model, inp_no, inp_date, inp_shift, inp_form = ComponentsUserInput().manual_input() 

            if inp_model != "None" and inp_no != "None" and inp_date != "None" and inp_shift != "None" and inp_form != "None":
                #if ComponentsButton().button_start_manual():
                WorkflowManagerAddData().handling_manual_input(inp_form=inp_form, inp_model=inp_model, inp_no=inp_no, inp_date=inp_date, inp_shift=inp_shift)  

        except Exception as e :  
            st.error(f"Error in class WorkflowManagerPage (render_manual_data) : {e}") 