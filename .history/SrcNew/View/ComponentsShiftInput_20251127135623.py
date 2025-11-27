import streamlit as st 
from streamlit_extras.row import row 
from SrcNew.Model.SessionManager import SessionManager
from SrcNew.View.ComponentsStyle import ComponentsStyle 

class ComponentsShiftInput:
    def display_input(self, value, label, df=None):
        """
        ---------------------------------------
        Parameter : <br>
            - value : Dataframe Will be Edit Shift Columns <br>
            - label : Is label in Button <br>
        """
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
 
            </style>
            """, unsafe_allow_html=True)
        
        df = value['Halaman'].unique()
        col1, col2 = st.columns([3, 0.2])
        with col1:
            with st.expander(label="📤 Ubah Shift Berdasarkan Halaman"):
                rows = row([2,2,1], vertical_align="bottom")
                option1 = rows.selectbox(label='Pilih Halaman :',
                                         placeholder="Pilih Halaman", 
                                         options=["None"] + [f"{i}" for i in df], index=0, key='halaman_update',
                                         label_visibility="visible")
         
                option2 = rows.selectbox(label="Pilih Shift :", 
                                         options=["None"] + list(range(1, 3)), index=0, key='shift_update',
                                         label_visibility="visible")
        
                option3 = rows.button(f"{label}", use_container_width=True)
        
        with col2:
            st.markdown("""
                <div class="tooltip">❗
                    <span class="tooltiptext">
                        <b>Informasi Tombol Ubah Shift Berdasarkan Halaman</b><br><br>
                        • Gunakan tombol ini untuk memudahkan anda mengubah nilai shift berdasarkan halaman. <br>
                        • Anda wajib menekan tombol <b>Perbarui Shift<b> setelah anda melakukan perubahan nilai shift. <br>
                    </span>
                </div>
                """, unsafe_allow_html=True)
        
        ## Button Update Shift 
        if option3 :
            if SessionManager().get_setter_state(key='form_type') == "Final Defects" :
                SessionManager().update_shift(df='dataframe_inline', columns1='Halaman', value1=option1, columns2='Shift', value2=option2)
                SessionManager().update_shift(df='dataframe_noninline', columns1='Halaman', value1=option1, columns2='Shift', value2=option2)
                ComponentsStyle().warning_alert5(True)
            
            else : 
                SessionManager().update_shift(df='dataframe_fpd', columns1='Halaman', value1=option1, columns2='Shift', value2=option2)  
                ComponentsStyle().warning_alert5(True)
        
        return option1, option2, option3
         