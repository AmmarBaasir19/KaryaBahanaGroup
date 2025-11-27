import os
import io
import streamlit as st 
import shutil 
from datetime import datetime
from SrcNew.Model.SessionManager import SessionManager
from SrcNew.Controller.ControllerPath import ControllerPath

class ComponentsButton:
    """ 
    This class will be Display All about button <br>
    ---------------------------------------------
    1. Button Error <br>
    2. Button Download <br>
    3. Button Update  <br>
    4. Button Download Reports <br>
    5. Button Start  <br>
    """
    def _delete_all_files(self, folder_path): 
        """"""
        try : 
            if os.path.exists(folder_path):
                files = os.listdir(folder_path)
                for file in files:
                    file_path = os.path.join(folder_path, file)
                    if os.path.isfile(file_path):
                        os.remove(file_path) 
        
        except Exception as e : 
            st.error(f"Error in class ComponentsButton (_delete_all_files) : {e}")
    
    def button_error(self, path_pdf, file_name, type_form):
        """
        **Display Error Processing Button** <br>
        ----------------------------------------
        Parameter : <br>
            - path_pdf : Path PDF File after Merged (Problem File) <br>
            - file_name : The Name of File Problem (Can't Scanning in System) <br>
            - type_form : Type of Form Input Final Defects or First Pass Defects <br>
        """
        st.markdown("""
            <style>
            div[data-testid="stDownloadButton"] > button {
                background: #2B2B30; 
                color: white;
                border: 2px solid green;
                border-radius: 10px;
                padding: 0.5rem 1.2rem;
                font-weight: bold;
                width: 100%;
                height: 40px;  
                transition: all 0.3s ease;
            }

            div[data-testid="stDownloadButton"] > button:hover {
                transform: scale(1.05);
                box-shadow: 0 9px 20px rgba(212, 157, 157, 0.4);
            }

            div[data-testid="stDownloadButton"] > button:active {
                background: green;
                border-color: #a00000;
                transform: scale(0.98);
            }
            </style>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns([3, 0.2])
        with col1:
            self.timestamp = datetime.now().strftime("%Y-%m-%d")
            if st.download_button(
                label="💾 Unduh PDF Yang Tidak Dapat Di Baca Sistem",
                data=path_pdf, 
                file_name=f"File_Problem_{file_name}_Type_{type_form}.pdf",
                mime="application/pdf",
                use_container_width=True) :
                self._delete_all_files("apps/storage/PDF_Problem")
        
        with col2:
            st.markdown("""
                <div class="tooltip">❗
                    <span class="tooltiptext">
                        <b>Informasi Tombol Simpan Data Hasil Pindai</b><br><br>
                        • Menyimpan data hasil pindai ke penyimpanan data perusahaan.
                    </span>
                </div>
                """, unsafe_allow_html=True)

    def button_download(self):
        """ Display Download Button """
        st.markdown("""
            <style> 
            div[data-testid="stButton"] > button {
                background: #2B2B30; 
                color: white;
                border: 3px solid green;
                border-radius: 10px;
                padding: 0.5rem 1.2rem;
                font-weight: bold;
                width: 100%;
                height: 40px;
                cursor: pointer;
                transition: all 0.3s ease;
                
                /* Styling untuk label */
                text-align: center;             /* Posisi teks di tengah */
                font-size: 16px;                /* Ukuran teks */
                font-family: Arial, sans-serif;/* Jenis huruf */
                letter-spacing: 0.5px;          /* Jarak antar huruf */
                line-height: 1.2;               /* Tinggi baris */ 
            }
                    
            /* Styling untuk tombol popover */
            div[data-testid="stPopover"] button {
                background: #2B2B30; 
                color: red;
                border: 3px solid red;
                border-radius: 10px;
                padding: 0.5rem 1.2rem;
                font-weight: bold;
                width: 100%;
                height: 40px;
                cursor: pointer;
                transition: all 0.3s ease;

                /* Styling teks */
                text-align: center;
                font-size: 16px;
                font-family: Arial, sans-serif;
                letter-spacing: 0.5px;
                line-height: 1.2;
                }
            
            /* Efek hover popover */
            div[data-testid="stPopover"] button:hover {
                background: green;
            }

            div[data-testid="stButton"] > button:hover {
                background: green; 
                color: white; 
                transform: scale(1.05);
                box-shadow: 0 9px 20px rgba(100, 255, 100, 0.3);
            }

            div[data-testid="stButton"] > button:active {
                background: green;
                border-color: green;
                transform: scale(0.98); 
            }
            </style>
            """, unsafe_allow_html=True)

        # Tampilkan tombol
        col1, col2 = st.columns([3, 0.2])
        with col1: 
            option1 = st.button(label="💾 Simpan Data Hasil Pindai", key="download_button", use_container_width=True)

        with col2:
            st.markdown("""
                <div class="tooltip">❗
                    <span class="tooltiptext">
                        <b>Informasi Tombol Simpan Data Hasil Pindai</b><br><br>
                        • Ketika anda menekan tombol ini, maka data hasil pindai akan disimpan otomatis pada penyimpanan data perusahaan. <br>
                        • Pastikan <b>Persentase Data Valid 100%<b>, Sebelum menekan tombol ini. <br>
                        • Setelah anda menekan tombol ini, maka tugas harian anda dinyatakan selesai.
                    </span>
                </div>
                """, unsafe_allow_html=True)
    
        return option1
    
    def button_update(self):
        """ Display Update Processing Button """
        st.markdown("""
            <style>
            div[data-testid="stButton"] > button {
                background: #2B2B30; 
                color: white;
                border: 2px solid #ff0000; 
                border-radius: 10px;
                padding: 0.5rem 1.2rem; 
                font-weight: bold;
                width: 100%;
                height: 40px;  
                transition: all 0.3s ease;
            }

            div[data-testid="stButton"] > button:hover {
                transform: scale(1.05);
                box-shadow: 0 9px 20px rgba(212, 157, 157, 0.4);
            }

            div[data-testid="stButton"] > button:active {
                background: #ff0000;
                border-color: #a00000;
                transform: scale(0.98);
            }
            </style>
        """, unsafe_allow_html=True)

        # Tampilkan tombol
        col1, col2 = st.columns([3, 0.2])
        with col1: 
            option1 = st.button("🔁 Perbarui Data Hasil Pindai", key="update_button", use_container_width=True)
        
        with col2:
            st.markdown("""
                <div class="tooltip">❗
                    <span class="tooltiptext">
                        <b>Informasi Tombol Perbarui Data Hasil Pindai</b><br><br>
                        • Anda dapat menekan tombol ini ketika anda sudah melakukan perubahan data hasil pindah (Mengubah isi data dalam tabel) <br>
                        • Anda wajib menekan tombol ini setelah anda melakukan perubahan data dalam tabel, agar semua perubahan yang anda lakukan tersimpan didalam sistem.<br>
                        • Gunakan tombol ini ketika <b>Persentase Data Valid kurang dari 100%<b>.
                        • Gunakan tombol ini ketika anda sudah mengubah <b>nilai Invalid di dalam tabel menjadi nilai Valid (Sesuai dengan form)<b>.
                    </span>
                </div>
                """, unsafe_allow_html=True)
    
        return option1 
    
    def button_download_reports(self, wb, start, end):
        """ Display styled save button and return True if clicked """

        # Tambahkan CSS untuk styling tombol
        st.markdown("""
            <style> 
            div[data-testid="stDownloadButton"] > button {
                background: #2B2B30; 
                color: white;
                border: 3px solid green; 
                border-radius: 10px;
                padding: 0.5rem 1.2rem;
                font-weight: bold;
                width: 100%;
                height: 40px;
                cursor: pointer;
                transition: all 0.3s ease;
                
                /* Styling untuk label */
                text-align: center;             /* Posisi teks di tengah */
                font-size: 16px;                /* Ukuran teks */
                font-family: Arial, sans-serif;/* Jenis huruf */
                letter-spacing: 0.5px;          /* Jarak antar huruf */
                line-height: 1.2;               /* Tinggi baris */ 
            }

            div[data-testid="stDownloadButton"] > button:hover {
                transform: scale(1.05);
                box-shadow: 0 9px 20px rgba(100, 255, 100, 0.3);
            } 

            div[data-testid="stDownloadButton"] > button:active {
                background: green;  
                border-color: green;
                transform: scale(0.98); 
            }
            </style>
            """, unsafe_allow_html=True)

        # Tampilkan tombol
        excel_buffer = io.BytesIO()
        wb.save(excel_buffer)
        excel_buffer.seek(0)

        col1 = st.columns(1)[0]
        with col1: 
            if st.download_button(
                label="💾 Unduh Reports",
                data=excel_buffer,
                file_name=f"Reports_{start}_{end}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True) :
                pass
    
    def button_save_merge(self, type_form): 
        """ Display Download Button """
        st.markdown("""
            <style> 
            div[data-testid="stDownloadButton"] > button {
                background: #2B2B30; 
                color: white;
                border: 3px solid green;
                border-radius: 10px; 
                padding: 0.5rem 1.2rem; 
                font-weight: bold;
                width: 100%;
                height: 40px;
                cursor: pointer;
                transition: all 0.3s ease;
                
                /* Styling untuk label */
                text-align: center;             /* Posisi teks di tengah */
                font-size: 16px;                /* Ukuran teks */
                font-family: Arial, sans-serif;/* Jenis huruf */
                letter-spacing: 0.5px;          /* Jarak antar huruf */
                line-height: 1.2;               /* Tinggi baris */ 
            }
            
            .tooltip {
                position: relative;
                display: inline-block;
                border: 2px solid #ff4d4d;        /* warna border */
                border-radius: 20%;
                padding: 3px 5px;
                cursor: pointer;
                font-size: 20px;
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

            div[data-testid="stDownloadButton"] > button:hover {
                background: green; 
                color: white; 
                transform: scale(1.05);
                box-shadow: 0 9px 20px rgba(100, 255, 100, 0.3);
            }

            div[data-testid="stDownloadButton"] > button:active {
                background: green;
                border-color: green; 
                transform: scale(0.98); 
            }
            </style>
            """, unsafe_allow_html=True)
        with open("Temporary/File_PDF.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
            col1, col2 = st.columns([3, 0.2]) 
            with col1:
                if type_form == "Final Defects": 
                    if st.download_button(label="💾 Unduh PDF Form",
                                          data=PDFbyte, 
                                          file_name=f"FRM-QC-026_rev3_{datetime.now().strftime('%Y-%m-%d')}_Final_Defects_Merge_File.pdf",
                                          mime="application/pdf", 
                                          use_container_width=True) : 
                        save_path = os.path.join(ControllerPath().path_merge, f"FRM-QC-026_rev3_{datetime.now().strftime('%Y-%m-%d')}_Final_Defects_Merge_File.pdf") 
                        shutil.copy("Temporary/File_PDF.pdf", save_path) 
                        SessionManager().set_setter_state(key='dataset_name', value=f"FRM-QC-026_rev3_{datetime.now().strftime('%Y-%m-%d')}_Final_Defects_Merge_File.pdf")
        
                else :
                    if st.download_button(label="💾 Unduh PDF Form",
                                          data=PDFbyte,
                                          file_name=f"FRM-QC-026_rev3_{datetime.now().strftime('%Y-%m-%d')}_First_Pass_Defects_Merge_File.pdf",
                                          mime="application/pdf",
                                          use_container_width=True) : 
                        save_path = os.path.join(ControllerPath().path_merge, f"FRM-QC-026_rev3_{datetime.now().strftime('%Y-%m-%d')}_First_Pass_Defects_Merge_File.pdf") 
                        shutil.copy("Temporary/File_PDF.pdf", save_path) 
                        SessionManager().set_setter_state(key='dataset_name', value=f"FRM-QC-026_rev3_{datetime.now().strftime('%Y-%m-%d')}_First_Pass_Defects_Merge_File.pdf") 
            
            with col2:
                st.markdown("""
                    <div class="tooltip">❗
                        <span class="tooltiptext">
                            <b>Informasi Tombol Unduh PDF Form</b><br><br>
                            • Gunakan tombol ini untuk mendapatkan form PDF yang diunggah diawal proses pemindaian <br>
                            • Setelah menekan tombol ini, anda akan diberikan file Form PDF. <br>
                            • File PDF yang diberikan akan berjumlah 1 file PDF, dan ketika anda mengunggah file PDF diawal proses pemindaian dengan jumlah lebih dari 1 file PDF, Maka otomatis semua file akan digabungkan menjadi 1 File saja. <br>
                            • File PDF yang diberikan dapat anda simpan dan dapat digunakan untuk mencocokkan antara Data Hasil Pemindaian dan Data aslinya.  
                        </span>
                    </div>
                    """, unsafe_allow_html=True)
    
    def button_start(self, tahun, bulan, tanggal, form_type): 
        """ Display start processing button """  
        st.markdown("""
            <style> 
            div[data-testid="stDownloadButton"] > button {
                background: #2B2B30; 
                color: white;
                border: 3px solid green; 
                border-radius: 10px;
                padding: 0.5rem 1.2rem;
                font-weight: bold;
                width: 100%;
                height: 40px;
                cursor: pointer;
                transition: all 0.3s ease;
                
                /* Styling untuk label */
                text-align: center;             /* Posisi teks di tengah */
                font-size: 16px;                /* Ukuran teks */
                font-family: Arial, sans-serif;/* Jenis huruf */
                letter-spacing: 0.5px;          /* Jarak antar huruf */
                line-height: 1.2;               /* Tinggi baris */ 
            }

            div[data-testid="stDownloadButton"] > button:hover {
                transform: scale(1.05);
                box-shadow: 0 9px 20px rgba(100, 255, 100, 0.3);
            } 

            div[data-testid="stDownloadButton"] > button:active {
                background: green;  
                border-color: green;
                transform: scale(0.98); 
            }
            </style>
            """, unsafe_allow_html=True) 
        
        return st.button(
            label='Mulai Lakukan Pembacaan Form',
            icon="🔁",
            use_container_width=True,
            on_click = SessionManager().set_start_btn(tahun=tahun, bulan=bulan, tanggal=tanggal, form_type=form_type, btn_auto=True))


    def button_start_manual(self): 
        """ Display start processing button """ 
        st.markdown(""" 
            <style> 
            div[data-testid="stDownloadButton"] > button {
                background: #2B2B30; 
                color: white;
                border: 3px solid green; 
                border-radius: 10px;
                padding: 0.5rem 1.2rem;
                font-weight: bold;
                width: 100%;
                height: 40px;
                cursor: pointer;
                transition: all 0.3s ease;
                
                /* Styling untuk label */
                text-align: center;             /* Posisi teks di tengah */
                font-size: 16px;                /* Ukuran teks */
                font-family: Arial, sans-serif;/* Jenis huruf */
                letter-spacing: 0.5px;          /* Jarak antar huruf */
                line-height: 1.2;               /* Tinggi baris */ 
            }

            div[data-testid="stDownloadButton"] > button:hover {
                transform: scale(1.05);
                box-shadow: 0 9px 20px rgba(100, 255, 100, 0.3);
            } 

            div[data-testid="stDownloadButton"] > button:active {
                background: green;  
                border-color: green;
                transform: scale(0.98); 
            }
            </style>
            """, unsafe_allow_html=True) 
        
        return st.button(
            label='Mulai Lakukan Input Data',
            icon="🔁",
            use_container_width=True)
    
    def button_update_all(self):
        """ Display Update Processing Button """
        st.markdown("""
            <style>
            div[data-testid="stButton"] > button {
                background: #2B2B30; 
                color: white;
                border: 2px solid #ff0000; 
                border-radius: 10px;
                padding: 0.5rem 1.2rem; 
                font-weight: bold;
                width: 100%;
                height: 40px;  
                transition: all 0.3s ease;
            }
            
           .tooltip {
                position: relative;
                display: inline-block;
                border: 2px solid #ff4d4d;        /* warna border */
                border-radius: 20%;
                padding: 3px 5px;
                cursor: pointer;
                font-size: 20px;
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

            div[data-testid="stButton"] > button:hover {
                transform: scale(1.05);
                box-shadow: 0 9px 20px rgba(212, 157, 157, 0.4);
            }

            div[data-testid="stButton"] > button:active {
                background: #ff0000;
                border-color: #a00000;
                transform: scale(0.98);
            }
            </style>
        """, unsafe_allow_html=True)

        # Tampilkan tombol
        col1, col2 = st.columns([3, 0.2])
        with col1: 
            option1 = st.button("🔁 Perbarui Semua Data Hasil Pindai", key="update_button", use_container_width=True)
        
        with col2:
            st.markdown("""
                <div class="tooltip">❗
                    <span class="tooltiptext">
                        <b>Informasi Tombol Perbarui Semua Data Hasil Pindai</b><br><br>
                        • Anda dapat menekan tombol ini ketika anda sudah melakukan perubahan data hasil pindah (Mengubah isi data dalam tabel) <br>
                        • Anda wajib menekan tombol ini setelah anda melakukan perubahan data dalam tabel, agar semua perubahan yang anda lakukan tersimpan didalam sistem. <br>
                        • Gunakan tombol ini ketika <b>Persentase Data Valid kurang dari 100%<b>.
                        • Gunakan tombol ini ketika anda sudah mengubah <b>nilai Invalid di dalam tabel menjadi nilai Valid (Sesuai dengan form)<b>.
                    </span>
                </div>
                """, unsafe_allow_html=True)
    
        return option1  

