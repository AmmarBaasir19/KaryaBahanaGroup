import streamlit as st 
from streamlit_option_menu import option_menu
from SrcNew.View.ComponentsStyle import ComponentsStyle
from SrcNew.Controller.WorkflowManagerPage import WorkflowManagerPage
from SrcNew.Model.MainCalender import MainCalender
from SrcNew.Controller.ControllerPath import ControllerPath
from SrcNew.Model.SessionManager import SessionManager

class WorkflowManagerMain:
    def __init__(self):
        with st.sidebar: 
            selected = option_menu("Menu Utama", ["Beranda", "Buat Reports", "Tambahkan Data"],
                               icons=['house', 'list-task', 'upc-scan'], menu_icon="cast", default_index=1)
            
            # Bagian Profil
            st.markdown(" ")
            st.markdown(" ") 
            st.markdown(" ") 
            st.markdown(" ") 
            st.markdown(" ") 
            st.markdown(" ") 
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ") 
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            st.markdown("---")
            ComponentsStyle().version() 
        
        if selected == "Beranda":
            SessionManager().set_setter_state(key='btn_click', value=SessionManager().get_setter_state(key='btn_click') + 1)
            ComponentsStyle().display_title("Hai!!, Selamat Siang Ammmar")
            MainCalender().run()
            if st.button("Tambahkan Data"): 
                st.page_link("pages/WorkflowManagerAddData.py", label="Ke Tambah") 

        elif selected == "Buat Reports" :
            SessionManager().set_setter_state(key='btn_click', value=SessionManager().get_setter_state(key='btn_click') + 1)
            ComponentsStyle().display_title("Buat Reports Secara Otomatis")
            WorkflowManagerPage().render_generate_reports()

        elif selected == "Tambahkan Data" :
            SessionManager().set_setter_state(key='btn_click', value=SessionManager().get_setter_state(key='btn_click') + 1)
            selected1 = option_menu(menu_title=None, 
                                    options=["Input Data Otomatis", "Input Data Manual"],
                                    icons=['upc-scan', 'bi bi-file-earmark-plus-fill'],
                                    menu_icon="cast",
                                    default_index=1,
                                    orientation='horizontal')
            
            if selected1 == "Input Data Otomatis" : 
                ComponentsStyle().display_title("Tambahkan Data Otomatis")
                st.write(" ")
                WorkflowManagerPage().render_add_data() 
            
            else : 
                st.write(f"Total Data : {SessionManager().get_setter_state(key='btn_click')}")
                ComponentsStyle().display_title("Tambahkan Data Manual")
                WorkflowManagerPage().render_manual_data() 

