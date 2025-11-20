import streamlit as st 


class ComponentsDataFrame:
    def table_inline(self):
        """"""
        column_configs = {
            "Halaman" : st.column_config.Column(
                label="Halaman",
                pinned=True
            ),

            "Welding Check Points" : st.column_config.Column(
                label="Welding Check Points",
                pinned=True
            )
        }

        return column_configs
    
    def table_noninline(self): 
        """"""
        column_configs = {
            "Halaman" : st.column_config.Column(
                label="Halaman",
                pinned=True
            ), 

            "Checked" : st.column_config.Column(
                label="Checked",
                pinned=True
            ), 
            "Ok" : st.column_config.Column(
                label="Ok",
                pinned=True 
            ),

            "Repair" : st.column_config.Column(
                label="Repair",
                pinned=True
            ), 

            "Scrap" : st.column_config.Column(
                label="Scrap",
                pinned=True
            )
        }

        return column_configs
    
    def table_firstpass(self):
        """"""
        column_configs = {
            "Halaman" : st.column_config.Column(
                label="Halaman",
                pinned=True
            ),

            "Total Repair" : st.column_config.Column(
                label="Total Repair",
                pinned=True
            ),

            "Total Top" : st.column_config.Column(
                label="Total Top",
                pinned=True
            ),

            "Total Middle" : st.column_config.Column(
                label="Total Middle",
                pinned=True
            ), 

            "Total Bottom" : st.column_config.Column(
                label="Total Bottom",
                pinned=True
            )
        }

        return column_configs 

    def display_dataframe(self, value, column_configs):
        """
        -------------------------
        Parameter : 
            - value : Dataframe
            - column_configs :
        """
        st.markdown("""
                    <style>
                    /* Styling untuk container utama */
                    .stDataFrame {
                        border: 2px solid #ff0000; 
                        border-radius: 10px;
                        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
                        overflow: hidden;
                        background: #ff0000;
                        padding: 0.01rem;
                    }
                    </style>
            """, unsafe_allow_html=True)
        df_edited = st.data_editor(value, column_config=column_configs, use_container_width=True)

        return df_edited  
    
