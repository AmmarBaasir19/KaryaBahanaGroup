import time
import os 
import streamlit as st 
from datetime import datetime
from SrcNew.Model.Model import Model
from SrcNew.Controller.ReadFile import ReadFile 
from SrcNew.Model.SessionManager import SessionManager
from SrcNew.Controller.DataPreprocessingFD import DataPreprocessingFD
from SrcNew.Controller.DataPreprocessingFPD import DataPreprocessingFPD

class RunProcessingLayer1:
    def _initialize_session(self, data1, data2):
        SessionManager().set_setter_state('list_images', data1)
        SessionManager().set_setter_state('list_pdf', data2)
        SessionManager().set_setter_state('start_time', datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

    def _show_upload_progress(self):
        """ To Show Progress Upload with Bars Progress"""
        try : 
            progress_bar = st.progress(0)
            status_text = st.empty() 

            for percent_complete in range(0, 101, 10):
                time.sleep(0.5)
                progress_bar.progress(percent_complete)
                status_text.text(f"🔄 Sedang Mengunggah File : {percent_complete}%")
            
            status_text = st.empty() 
            progress_bar.progress(100)
            progress_bar.empty()
            status_text.text(f"✅ Berhasil Mengunggah File!")
        
        except Exception as e : 
            st.error(f"Error in class RunProcessLayer1 () : ")
    
    def _show_done_upload(self, data):
        try : 
            status_text = st.empty()

            # Get List of Images in Folder
            status_text.text(f"📄 Total Halaman Yang Terbaca : {len(data)} Halaman") 
        
        except Exception as e : 
            st.error(f"Error in class RunProcessLayer1 () : ")

    def _read_pdf(self, uploaded_file):
        try : 
            with st.spinner(f"🔄 Sedang Membaca File PDF ...."):
                read_file = ReadFile(uploaded_file)
                read_file_1, read_file_2 = read_file() 
            
            return read_file_1, read_file_2
        
        except Exception as e : 
            st.error(f"Error in class RunProcessLayer1 () : ")

    def _read_model(self, value, i, len_page):
        """ To Read Data from image to Model OCR (Structured Data)"""
        try : 
            with st.spinner(f"🔄Sedang Memproses Halaman Ke-{i+1} Dari {len_page} Halaman ...."):
                result_data = Model(value)
            
            return result_data

        except Exception as e : 
            st.error(f"Error in class RunProcessLayer1 () : ")

    def run(self, uploaded_file, type_form):
        """
        This Function will be processing several function : <br>
        1. _show_upload_progress <br>
        2. _show_done_upload <br>
        3. _initialize_session <br>
        4. _read_pdf <br>
        """
        try : 
            status_text = st.empty()
            print(f"Ini run") 

            progress_bar = st.progress(0) 
            status_text = st.empty()

            for percent_complete in range(0, 101, 10):
                time.sleep(0.5)
                progress_bar.progress(percent_complete)
                status_text.text(f"🔄 Sedang Mengunggah File : {percent_complete}%")
            
            progress_bar.progress(100)
            progress_bar.empty()
            status_text.text(f"✅ Berhasil Mengunggah File!")
            status_text = st.empty() 

            # Get List of Images in Folder
            status_text.text(f"📄 Total Halaman Yang Terbaca : {len(uploaded_file)} Halaman") 
            data1, data2 = self._read_pdf(uploaded_file)
            with st.spinner(f"🔄 Sedang Membaca File PDF ...."):
                read_file = ReadFile(uploaded_file) 
                read_file_1, read_file_2 = read_file() 
            
            SessionManager().set_setter_state('list_images', data1) 
            SessionManager().set_setter_state('list_pdf', data2)
            SessionManager().set_setter_state('start_time', datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
            
            list_inline, list_noninline, list_fpd = [], [], []
            list_polygon, process_time, error_pages = [], [], []
            total_halaman = 1 
            print(f"Ini run RunProcessingLayer1")

            try : 
                for i, list_img in enumerate(data1):
                    if os.path.exists(list_img):
                        try :
                            start_time = time.time() 

                            df_result = self._read_model(list_img, i, len(data1))

                            if type_form == "Final Defects" :
                                print(f"Ini Final Defects") 
                                print(f"Ini df_result : {df_result()}")
                                df1, df2, df_polygon = DataPreprocessingFD().run(df_result(), i, type_form)

                                print(f"Before append Final Defects")  

                                list_inline.append(df1.values.tolist())
                                list_noninline.append(df2.values.tolist())
                                list_polygon.append(df_polygon.values.tolist())
                        
                            else : 
                                print(f"Ini First Pass Defects")
                                df, df_polygon = DataPreprocessingFPD().run(df_result(), i, type_form)
                                print(f"Ini First Pass Defects data : {df}")
                                print(f"Ini First Pass Defects data type : {type(df)}")
                                print(f"Ini First Pass Defects data : {df.columns}")
                                list_fpd.append(df.values.tolist())
                                list_polygon.append(df_polygon.values.tolist()) 

                        
                            end_time = time.time()
                            processing_time = end_time - start_time
                            process_time.append(processing_time)
                            total_halaman += 1
                            status_text.text(f"✅ Halaman {i+1} selesai diproses dalam {processing_time:.2f} detik.")
                        
                        except Exception as e : 
                            st.warning(f"Model Gagal Memproses Form Di Halaman ke - {i+1}")
                            error_pages.append(i+1)
                            continue 
                
                sum_processing_time = f"{sum([float(x) for x in process_time]):.2f}"
                status_text.text(f"✅ Sukses Melakukan Scanning {len(data1)} Halaman Dengan Waktu : {sum([float(x) for x in process_time]):.2f} detik")
                SessionManager().set_setter_state(key='sum_processing', value=sum_processing_time)
                SessionManager().set_setter_state(key='processing_page', value=process_time)
        
                print(f"Ini RunProcessingLayerMain list_fpd : {list_fpd}")
            except Exception as e : 
                SessionManager().set_setter_state('error_page', error_pages)
                st.error(f"Error in class RunProcessLayer1 (run) : {e}")

            print(f"Ini RunProcessingLayerMain list_fpd Kedua : {list_fpd}")
            return list_inline, list_noninline, list_fpd, list_polygon, error_pages 
    
        except Exception as e :  
            st.error(f"Error in class RunProcessLayer1 (run) : {e}")




