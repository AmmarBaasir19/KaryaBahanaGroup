import cv2
from PIL import Image
import streamlit as st 
from streamlit_modal import Modal
from SrcNew.Controller.DataValidation3 import DataValidation3
from SrcNew.Model.SessionManager import SessionManager

class ComponentsStyle:
    """"""
    def page_setup(self, file):
        """ This Function will be show logo in page header """
        st.set_page_config(
            page_title="Karya Bahana Super App",
            page_icon=file,
            layout="wide"
        )
    
    def display_title(self, title_text):
        """ """
        st.markdown(f"""
                    <div style="text-align: center;">
                    <h1 style="background: #A83939; 
                    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                    font-size: 3rem; font-weight: bold; margin-bottom: 0rem;">
                    {title_text}
                    </h1>
                    </div>
                    """, unsafe_allow_html=True)
    
    def display_uploaded(self, value):
        """ """
        try : 
            st.markdown("""
                <style>
                /* --- Desain Kontainer Utama File Uploader --- */
                div[data-testid="stFileUploader"] {
                    border: 2px solid #ff0000;
                    background-color: #2B2B30;
                    border-radius: 10px;
                    padding: 15px;
                    transition: all 0.3s ease;
                }
                div[data-testid="stFileUploader"]:hover {
                    border-color: #ff0000;
                    box-shadow: 0 9px 20px rgba(212, 157, 157, 0.5);
                }

                /* --- Desain Label/Judul --- */
                div[data-testid="stFileUploader"] label {
                    font-weight: bold;
                    color: white; /* Warna teks judul */
                    font-size: 3.1em;
                }
    
                /* --- Desain Area Drag and Drop & Teksnya --- */
                div[data-testid="stFileUploader"] section {
                    background-color: #1e1e21; /* Background area drop */
                    border: 2px solid #ff0000;
                }
    
                div[data-testid="stFileUploader"] small {
                    color: #d0d0d0; /* Warna teks kecil "Limit 200MB per file" */
                }
                </style>
            """, unsafe_allow_html=True)

            if value == True:
                uploaded_file = st.file_uploader("Upload File PDF Anda", type=["pdf"], key="file_uploader",  accept_multiple_files=True)
                
                return uploaded_file
            
            else : 
                uploaded_file = st.file_uploader("Upload File PDF Anda", type=["pdf"], key="file_uploader")

                return uploaded_file
        
        except Exception as e:
            st.error(f"Error in class ComponentStyle (_display_uploaded) : {e}")
    
    def display_result(self):
        """ This Function will be show title result scanning """
        st.markdown(
            """ 
            <h2 style='text-align: center;'>Data Hasil Pembacaan OCR</h2> 
            """, unsafe_allow_html=True
        )
        st.markdown(" ")
    
    def display_result2(self, label):
        """ This Function will be show title result scanning """
        st.markdown(
            f""" 
            <h2 style='text-align: center;'>{label}</h2> 
            """, unsafe_allow_html=True
        )
        st.markdown(" ")
    
    def display_warning(self, message): 
        """"""
        st.warning(f"{message}", icon="⚠️")
    
    def warning_alert1(self, value1, value2):
        """
        This Function will be check invalid data,
        if there is invalid data will be show alert.
        """

        ## Call Function check_invalid 
        contains_invalid_v1 = DataValidation3().check_invalid(value1)
        contains_invalid_v2 = DataValidation3().check_invalid(value2)
        if contains_invalid_v1 or contains_invalid_v2:  
            st.warning('Terdapat Data Invalid Dari Hasil Scanning Dokumen, Harap Validasi Data Secara Manual', icon="⚠️");

    def warning_alert2(self, value):
        """ This function will be show warning alert if there is still invalid data from scanning result """ 

        modal = Modal(key="warning_alert2", title="⚠️ Warnings!!!", max_width=600, padding=70)
        if value == True:
            with modal.container():
                st.markdown(
                    "<h6 style='color:red;'>Terdapat Data Invalid Dari Hasil Scanning, Mohon Validasi Data Secara Manual!!!</h6>",
                    unsafe_allow_html=True
                )
 
    def warning_alert3(self, value, page1, page2):
        """
        This function will be show warning alert if there is still invalid data in Columns : KEROPOS, KURANG, BOLONG, UNDERCUT, SPATTER, TIDAK TEPAT
        """

        try : 
            modal = Modal(key="warning_alert3", title="⚠️ Warnings!!!", max_width=600, padding=70)
            list_data1 = ','.join(page1)
            list_data2 = ','.join(page2) 
            if value == True: 
                if not list_data2 and list_data1 != None :
                    with modal.container():
                        st.markdown( 
                            f"Terdapat Kesalahan Pembacaan atau Data Invalid di Data Inline Repair : {list_data1}", 
                            unsafe_allow_html=True
                        ) 
                        st.markdown( 
                            f"Tidak Ditemukan Kesalahan Pembacaan atau Data Invalid di Data Noninline Repair",
                            unsafe_allow_html=True
                        ) 
                elif not list_data1 and list_data2 != None : 
                    with modal.container():  
                        st.markdown( 
                            f"Terdapat Kesalahan Pembacaan atau Data Invalid di Data Noninline Repair : {list_data2}", 
                            unsafe_allow_html=True
                        )
                        st.markdown( 
                            f"Tidak Ditemukan Kesalahan Pembacaan atau Data Invalid di Data Inline Repair", 
                            unsafe_allow_html=True
                        ) 
                elif list_data1 != None and list_data2 != None: 
                    with modal.container(): 
                        st.markdown(
                            f"Terdapat Kesalahan Pembacaan atau Data Invalid di Data Inline Repair : {list_data1}", 
                            unsafe_allow_html=True 
                        ) 
                        st.markdown(
                            f"Terdapat Kesalahan Pembacaan atau Data Invalid di Data Noninline Repair : {list_data2}", 
                            unsafe_allow_html=True 
                        )
                else :
                    with modal.container():
                        st.markdown(
                            f"Data Hasil Pembacaan Sudah Tidak Memiliki Data Invalid",  
                            unsafe_allow_html=True 
                    )

        except Exception as e : 
            st.error(f"Error in class ComponentStyle (_warning_alert3) : {e}") 
    
    def warning_alert4(self, value, type_form):
        """
        This function will be show warning alert if there is still invalid data from scanning result
        """ 

        modal = Modal(key="warning_alert4", title="⚠️ Warnings!!!", max_width=600, padding=70) 
        if value == True:
            with modal.container():
                st.markdown(
                    f"<h6 style='color:red;'>Masukkan Data Tahun, Bulan, Tanggal, dan Tipe Form Yang Sesuai dengan Form {type_form} </h6>",
                    unsafe_allow_html=True
                )
    
    def warning_alert5(self, value):
        """ This function will be show warning alert if there is still invalid data from scanning result """ 

        modal = Modal(key="warning_alert5", title="✅ Berhasil!!!", max_width=600, padding=70)
        if value == True:
            with modal.container():
                st.markdown(
                    "<h6 style='color:red;'>Berhasil Mengubah Shift Berdasarkan Halaman!!!</h6>",
                    unsafe_allow_html=True
                )

    def display_done(self, value):
        """ This function will be show done alert after click button """
        st.html(
            """
            <style> 
            div[aria-label="dialog"] > button[aria-label="Close"] {
                display: none; /* Hide the close button */
                }
            </style> 
            """
        )

        modal = Modal(key="done_modal", title="✅ Berhasil Mengunggah Data!!!", max_width=750, padding=30)
        if value == True:
            with modal.container():
                st.markdown(
                    """
                    <style>
                    div[data-testid="stDialog"] h1 {
                    font-size: 4px; /* Ubah ukuran sesuai kebutuhan */
                    }
                    </style>
                    """, 
                    unsafe_allow_html=True
                ) 
    
    def alert_filter(self, text: str):
        """
        This Function will be show alert for filter 
        """
        
        st.warning(f"Mohon Pilih {text} Yang Ingin Ditampilkan", icon="⚠️")
    
    def filter_selected(self, type_form):
        """"""
        try : 
            st.markdown("""
                <style>
                .tooltip {
                    position: relative;
                    display: inline-block;
                    border: 2px solid #ff4d4d;        /* warna border */
                    border-radius: 20%;
                    padding: 3px 5px;
                    cursor: pointer;
                    font-size: 22px;
                    }

                .tooltip .tooltiptext {
                    visibility: hidden;
                    width: 430px;
                    background-color: #F5EDED;
                    color: black;
                    text-align: left; 
                    border-radius: 15px;
                    border: 2px solid red;
                    padding: 8px;
                    position: absolute;
                    z-index: 1;
                    right: 120%;
                    top: 50%;
                    transform: translateY(-50%);
                    opacity: 0;
                    transition: opacity 0.3s;
                    font-size: 14px;
                    line-height: 1.4;
                }

                /* Tanda segitiga */
                .tooltip .tooltiptext::after {
                    content: "";
                    position: absolute;
                    top: 50%;
                    left: 100%;
                    margin-top: -5px;
                    border-width: 6px;
                    border-style: solid;
                    border-color: transparent transparent transparent #e3f2fd;
                }

                .tooltip:hover .tooltiptext {
                    visibility: visible;
                    opacity: 1;
                }
                </style>
                """, unsafe_allow_html=True)
 
            type_form_df = SessionManager().get_setter_state(key='Halaman', df="dataframe_inline").unique() if type_form == "Final Defects" else SessionManager().get_setter_state(key='Halaman', df="dataframe_fpd").unique()
            print(f"Ini filter_selected : {type_form}")
            col1, col2 = st.columns([3, 0.2])
            with col1:
                with st.expander(label="🔍 Cari Data Invalid Berdasarkan Halaman"):    
                    option_1 = st.selectbox(label="Pilih Halaman", options=["None"] + [f"{i}" for i in type_form_df], index=0, key='halaman_selected')
                    option_2 = st.multiselect(label="Pilih Tipe Invalid", options=['Invalid Type 1', 'Invalid Type 2', 'Invalid Type 3', 'Invalid Type 4', 'Invalid Type 5', "Invalid Type 6", "Invalid Type 7", 'Invalid Scanning', 'Invalid Converted to INT'], key='multiselect') 
            
            with col2:
                st.markdown("""
                    <div class="tooltip">❗
                        <span class="tooltiptext">
                            <b>Informasi Tombol Cari Data Invalid Berdasarkan Halaman</b><br><br>
                            • Gunakan tombol ini untuk memudahkan anda mencari data invalid berdasarkan halaman. <br>
                            • Gunakan tombol ini ketika terdapat data invalid dalam tabel. <br>
                            • Untuk mengetahui tabel terdapat data invalid atau tidak, anda dapat menggunakan kotak informasi Jumlah Data Invalid. <br>
                            • Ketika pada kotak informasi Jumlah Data Invalid menampilkan angka selain 0, maka ini menandakan tabel memiliki Data Invalid. <br>
                            • Atur kotak Pilih Halaman ke <b>None<b> dan Pilih Tipe Invalid ke <b>None<b>, agar anda dapat menampilkan semua data invalid maupun data valid. <br>
                            • Ketika anda sudah menggunakan tombol ini untuk menampilkan data invalid berdasarkan halaman dan tabel yang ditampilkan berisi None (kosong). maka ini menandakan halaman tersebut tidak memiliki nilai Invalid. <br>
                            
                            <b> Pilihan Tipe Invalid<b><br>
                        </span>
                    </div>
                    """, unsafe_allow_html=True)
            
            return option_1, option_2
        
        except Exception as e : 
            st.error(f"Error in class ComponentsStyle (filter_selected) : {e}")
            
    def version(self):
        """ This Function will be show title in Home Apps """

        st.markdown( 
                """ 
                <h6 style='text-align: center;'>Created by : Karya Bahana Group</h6>
                <h6 style='text-align: center;'>Version 3.0.1</h6>
                """,
                unsafe_allow_html=True
            )
    