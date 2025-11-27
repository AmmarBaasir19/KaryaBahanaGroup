import streamlit as st 
from datetime import datetime
from SrcNew.Model.SessionManager import SessionManager
from SrcNew.WorkflowManagerMain import WorkflowManagerMain
from SrcNew.View.ComponentsStyle import ComponentsStyle
from streamlit_option_menu import option_menu
from SrcNew.View.ComponentsStyle import ComponentsStyle
from SrcNew.Controller.WorkflowManagerPage import WorkflowManagerPage
from SrcNew.Controller.ControllerPath import ControllerPath
from SrcNew.Controller.Login import Login

if __name__ == "__main__":
    ComponentsStyle().page_setup("Assets/Karya Bahana Group.png") 
    if SessionManager().get_setter_state(key='login_condition') == False : 
        Login().login_main()
    
    else : 
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
            hour = datetime.now().hour
            if 5 <= hour < 12 :
                waktu = "Pagi"
            elif 12 <= hour < 15 :
                waktu = "Siang"
            elif 15 <= hour < 18 :
                waktu = "Sore"
            else :  
                waktu = "Malam" 

            ComponentsStyle().display_title(f"Hai!!, Selamat {waktu} {SessionManager().get_setter_state(key='name')}")
            WorkflowManagerPage().render_beranda()

        elif selected == "Buat Reports" :
            ComponentsStyle().display_title("Buat Reports Secara Otomatis")
            WorkflowManagerPage().render_generate_reports()

        elif selected == "Tambahkan Data" :
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
                ComponentsStyle().display_title("Tambahkan Data Manual")
                WorkflowManagerPage().render_manual_data()     