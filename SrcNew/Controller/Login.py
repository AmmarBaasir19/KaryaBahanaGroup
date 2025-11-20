import streamlit as st 
import json 
from datetime import datetime
from SrcNew.Controller.ControllerPath import ControllerPath
from SrcNew.Model.SessionManager import SessionManager

class Login:   
    def login_main(self):
        try : 
            # Styling form (CSS)
            st.markdown("""
            <style>
            /* Container layout */
            .stForm {
                background-color: #2B2B30;
                padding: 2rem;
                border-radius: 15px;
                border: 3px solid #ff0000; /* Border transparan awal */
                box-shadow: 0 0 20px rgba(255, 0, 0, 0.1);
            }

            /* Input field */
            div[data-testid="stTextInput"] > div > div {
                background: #2B2B30 !important;
                color: white !important;
                border: 3px solid #ff0000 !important;
                border-radius: 10px !important;
                padding: 0.5rem 1.2rem !important;
                font-weight: bold !important;
                transition: all 0.3s ease-out;
                cursor: text;
            }
                        
            div[data-testid="stTextInput"] > div {
                transition: transform 0.3s ease;
            }

            div[data-testid="stTextInput"] > input:active {
                color: white;
                border: 3px solid #ff0000; /* Border transparan awal */
                transform: scale(0.8);
            }
            
            form button {
                background-color: #ff0000 !important;
                color: white !important;
                border: 3px solid #00ffff !important;  /* Ubah warna border di sini */
                border-radius: 12px !important;
                padding: 0.5rem 1.5rem !important;
                font-weight: bold !important;
                transition: all 0.3s ease !important;
            }

            /* Hover effect */
            form button:hover {
                background-color: #cc0000 !important;
                transform: scale(1.05);
                box-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
            }

            /* Klik (active) effect */
            form button:active {
                transform: scale(0.95);
                background-color: #a00000 !important;
                border-color: #ffffff !important;
            }
            </style>
            
            </style>
            """, unsafe_allow_html=True)

            # Form section
            st.markdown("<h2 style='text-align:center; color: white;'>🔐 Karya Bahana Super Apps</h2>", unsafe_allow_html=True)

            user_dict = {user["username"]: user for user in ControllerPath().users}
            with st.form(key="login_form", clear_on_submit=False):
                username = st.text_input("Username", placeholder="Contoh : admin@admin.com")
                password = st.text_input("Password", placeholder="Contoh : @1122AB", type="password")
                submit_button = st.form_submit_button("Login", use_container_width=True) 

                if submit_button: 
                    if username in user_dict and user_dict[username]["password"] == password: 
                        SessionManager().set_setter_state(key='login_condition', value=True)
                        SessionManager().set_setter_state(key='name', value=user_dict[username]['name'])
                        SessionManager().set_setter_state(key='username', value=user_dict[username]['username'])
                        SessionManager().set_setter_state(key='role', value=user_dict[username]['role'])
                        SessionManager().set_setter_state(key='location', value=user_dict[username]['location'])
                        SessionManager().set_setter_state(key='nik_nipm', value=user_dict[username]['nik_nipm'])
                        SessionManager().set_setter_state(key='login_id', value=f"LGN_{datetime.now().strftime('%Y-%m-%d_%H-%M')}_{user_dict[username]['location']}")
                        st.success(f"✅ Selamat datang, {username}!")

                    else:  
                        st.warning("⚠️ Mohon lengkapi username dan password.")


        except Exception as e :
            st.error(f"Error in Login (login_main) : {e}")