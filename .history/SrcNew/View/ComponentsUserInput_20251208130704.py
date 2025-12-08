import streamlit as st  
from streamlit_extras.row import row
from datetime import datetime, date, timedelta 
from SrcNew.Controller.ControllerPath import ControllerPath

class ComponentsUserInput:
    def date_input(self):
        """"""
        st.markdown("""
            <style>
            /* --- Desain Expander --- */
            div[data-testid="stExpander"] {
                background: #2B2B30;
                color: white;
                border: 2px solid #ff0000;
                height: 100%;
                border-radius: 10px;
                transition: all 0.3s ease; 
            }
            div[data-testid="stExpander"]:hover {
                border-color: #ff0000;
                box-shadow: 0 9px 20px rgba(212, 157, 157, 0.5);
            }
                    
            div[data-testid="stExpander"] summary {
                color: white;
                background: none;
                font-weight: bold; /* Tambahkan baris ini */
                font-size: 15px;
            } 
                    
            /* --- Pengaturan Jarak (Margin) --- */
            /* Menambahkan jarak di atas dan di bawah setiap komponen agar tidak bertumpuk */
            div[data-testid="stSelectbox"], 
            div[data-testid="stButton"] {
                margin-top: 0rem;
                margin-bottom: 0rem; 
            }

            /* --- Desain Selectbox --- */
            div[data-testid="stSelectbox"] > div {
                background: #2B2B30;
                color: white;
                border: 2px solid #ff0000;
                height: 100%;
                border-radius: 10px;
                transition: all 0.3s ease;
            }
            div[data-testid="stSelectbox"] > div:hover {
                border-color: #f95d5d;
                box-shadow: 0 9px 20px rgba(212, 157, 157, 0.5);
            }
            div[data-testid="stSelectbox"] svg {
                fill: white; /* Warna panah dropdown */
            }
            /* Opsi pada dropdown list */
            li[data-baseweb="select-option"] {
                background-color: #2B2B30;
                color: white;
            }
            li[data-baseweb="select-option"]:hover {
                background-color: #4a4a52;
            }
            li[data-baseweb="select-option"][aria-selected="true"] {
                background-color: #ff0000;
            }
            

            div[data-testid="stButton"] > button {
                background: #2B2B30; 
                color: white;
                border: 2px solid #ff0000;
                border-radius: 10px;
                padding: 0.5rem 1.2rem;
                font-weight: bold;
                height: 100%;
                width: 100%; 
                cursor: pointer;
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
            }0
 
            </style>
            """, unsafe_allow_html=True)
        
        rows = row([2,2,2,2], vertical_align="bottom")
        option1 = rows.selectbox(label='Pilih Tahun :',
                                 placeholder="Pilih Tahun", 
                                 options=["2025"], index=0, key='tahun_input',
                                 label_visibility="visible")
        
        option2 = rows.selectbox(label="Pilih Bulan :",
                                 placeholder="Pilih Bulan", 
                                 options=["None"] + list(range(1, 13)), index=0, key='bulan_input',
                                 label_visibility="visible")
        
        option3 = rows.selectbox(label="Pilih Tanggal :",
                                placeholder="Pilih Tanggal", 
                                options=["None"] + list(range(1, 32)), index=0, key='tanggal_input',
                                label_visibility="visible")
        
        option4 = rows.selectbox(label="Pilih Tipe Form :", 
                                options=["None"] + ["Final Defects", "First Pass Defects"], index=0, key='type_form',
                                label_visibility="visible") 
        
        return option1, option2, option3, option4
    
    def reports_input(self, label):
        """"""
        st.markdown("""
            <style>
            /* --- Desain Expander --- */
            div[data-testid="stExpander"] {
                background: #2B2B30;
                color: white;
                border: 2px solid #ff0000;
                height: 100%;
                border-radius: 10px;
                transition: all 0.3s ease;
            }
            div[data-testid="stExpander"]:hover {
                border-color: #ff0000;
                box-shadow: 0 9px 20px rgba(212, 157, 157, 0.5);
            }
            div[data-testid="stExpander"] summary {
                color: white;
                background: none;
                font-weight: bold; /* Tambahkan baris ini */
                font-size: 15px;
            }
            /* --- Pengaturan Jarak (Margin) --- */
            /* Menambahkan jarak di atas dan di bawah setiap komponen agar tidak bertumpuk */
            div[data-testid="stSelectbox"],
            div[data-testid="stButton"] {
                margin-top: 0rem;
                margin-bottom: 0rem;
            }
            /* --- Desain Selectbox --- */
            div[data-testid="stSelectbox"] > div {
                background: #2B2B30;
                color: white;
                border: 2px solid #ff0000;
                height: 100%;
                border-radius: 10px;
                transition: all 0.3s ease;
            }
            /* --- Desain Selectbox --- */
            div[data-testid="stDateInput"] > div {
                background: #2B2B30;
                color: white;
                border: 2px solid #ff0000;
                height: 100%;
                border-radius: 10px;
                transition: all 0.3s ease;
            }
            
            div[data-testid="stSelectbox"] > div:hover {
                border-color: #f95d5d;
                box-shadow: 0 9px 20px rgba(212, 157, 157, 0.5);
            }
            div[data-testid="stSelectbox"] svg {
                fill: white; /* Warna panah dropdown */
            }
            /* Opsi pada dropdown list */
            li[data-baseweb="select-option"] {
                background-color: #2B2B30;
                color: white;
            }
            li[data-baseweb="select-option"]:hover {
                background-color: #4a4a52;
            }
            li[data-baseweb="select-option"][aria-selected="true"] {
                background-color: #ff0000;
            }

            div[data-testid="stButton"] > button {
                background: #2B2B30;
                color: white;
                border: 2px solid #ff0000;
                border-radius: 10px;
                padding: 0.5rem 1.2rem;
                font-weight: bold;
                height: 100%;
                width: 100%;
                cursor: pointer;
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
                    
            </style>
            """, unsafe_allow_html=True)
       
        col1, col2 = st.columns([3, 0.2])
        with col1:
            with st.expander(label="📤 Tekan Untuk Membuat Reports Otomatis Berdasarkan Tanggal"):
                rows = row([2,2,2,2], vertical_align="bottom")
                btn_format = rows.selectbox(label='Pilih Format Reports :',
                                    options=["None"] + ["Format 1", "Format 2"],
                                    index=0,
                                    key='format',
                                    label_visibility="visible")
 
                btn_start = rows.date_input(
                                    label="Tanggal Mulai :",
                                    value = date.today(),
                                    key = "start_date")

                btn_end = rows.date_input(
                                    "Tanggal Selesai :",
                                    value = date.today() + timedelta(days=7),
                                    key = "end_date")

                btn_generate = rows.button(f"{label}", use_container_width=True)
                btm = st.download_button()
        
        with col2:
            st.markdown("""
                <div class="tooltip">❗
                    <span class="tooltiptext">
                        <b>Informasi Tombol Membuat Reports Otomatis Berdasarkan Tanggal</b><br><br>
                        • Anda dapat menekan tombol ini ketika anda ingin membuat reports secara otomatis.<br>
                        • Pilih Tanggal Mulai dan Tanggal Selesai untuk menentukan reports akan dibuat pada rentang tanggal tertentu. <br>
                        • Pilih Format reports sesaui yang anda butuhkan. <br>
                            • <b>Format 1 : <b>Report Summary (Reports dibuat dengan tidak memperdulikan Shift) <br>
                            • <b>Format 2 : <b> Report Detail (Reports dibuat dengan memperdulikan Shift) <br>
                        • Tekan tombol <b>Buat Reports<b> untuk mulai membuat reports secara otomatsi.
                    </span>
                </div>
                """, unsafe_allow_html=True)

        return btn_format, btn_start, btn_end, btn_generate 

    def manual_input(self):
        """"""
        st.markdown("""
            <style>
            /* --- Desain Expander --- */
            div[data-testid="stExpander"] {
                background: #2B2B30;
                color: white;
                border: 2px solid #ff0000;
                height: 100%;
                border-radius: 10px;
                transition: all 0.3s ease; 
            }
            div[data-testid="stExpander"]:hover {
                border-color: #ff0000;
                box-shadow: 0 9px 20px rgba(212, 157, 157, 0.5);
            }
                    
            div[data-testid="stExpander"] summary {
                color: white;
                background: none;
                font-weight: bold; /* Tambahkan baris ini */
                font-size: 15px;
            } 
                
                    
            /* --- Pengaturan Jarak (Margin) --- */
            /* Menambahkan jarak di atas dan di bawah setiap komponen agar tidak bertumpuk */
            div[data-testid="stSelectbox"], 
            div[data-testid="stButton"] {
                margin-top: 0rem;
                margin-bottom: 0rem; 
            }

            /* --- Desain Selectbox --- */
            div[data-testid="stSelectbox"] > div {
                background: #2B2B30;
                color: white;
                border: 2px solid #ff0000;
                height: 100%;
                border-radius: 10px;
                transition: all 0.3s ease;
            }
            div[data-testid="stSelectbox"] > div:hover {
                border-color: #f95d5d;
                box-shadow: 0 9px 20px rgba(212, 157, 157, 0.5);
            }
            div[data-testid="stSelectbox"] svg {
                fill: white; /* Warna panah dropdown */
            }
            /* Opsi pada dropdown list */
            li[data-baseweb="select-option"] {
                background-color: #2B2B30;
                color: white;
            }
            li[data-baseweb="select-option"]:hover {
                background-color: #4a4a52;
            }
            li[data-baseweb="select-option"][aria-selected="true"] {
                background-color: #ff0000;
            }
            

            div[data-testid="stButton"] > button {
                background: #2B2B30; 
                color: white;
                border: 2px solid #ff0000;
                border-radius: 10px;
                padding: 0.5rem 1.2rem;
                font-weight: bold;
                height: 100%;
                width: 100%; 
                cursor: pointer;
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
                    
            /* --- Desain Selectbox --- */
            div[data-testid="stDateInput"] > div {
                background: #2B2B30;
                color: white;
                border: 2px solid #ff0000;
                height: 100%;
                border-radius: 10px;
                transition: all 0.3s ease;
            }
            div[data-testid="stDateInput"] > div:hover {
                border-color: #f95d5d;
                box-shadow: 0 9px 20px rgba(212, 157, 157, 0.5);
            }
            </style>
            """, unsafe_allow_html=True)
        
        rows = row([2,2,2,1,2], vertical_align="bottom")
        option1 = rows.selectbox(label='Pilih Model :',
                                 placeholder="Pilih Model", 
                                 options=list(ControllerPath().database_part_check.keys()), index=0, key='model_input',
                                 label_visibility="visible")
         
        option2 = rows.selectbox(label='Pilih Part No :',
                                 placeholder="Pilih Part No", 
                                 options=["None"] + list(ControllerPath().database_part_check[option1].keys()), index=0, key='part_no_manual_input',
                                 label_visibility="visible")
        
        option3 = rows.date_input(label="Pilih Tanggal:",
                                  value=None,                 # atau bisa default ke tanggal tertentu
                                  min_value=None,             # bisa ditentukan range-nya
                                  max_value=None,
                                  key='tanggal_input'
                                  )
        
        option4 = rows.selectbox(label="Pilih Shift :", 
                                options=["None", "1", "2"], index=0, key='type_shift',
                                label_visibility="visible") 
        
        option5 = rows.selectbox(label="Pilih Tipe Form :", 
                                options=["None"] + ["Final Defects", "First Pass Defects"], index=0, key='type_form',
                                label_visibility="visible") 
        
        return option1, option2, option3, option4, option5