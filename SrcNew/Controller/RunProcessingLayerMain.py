import streamlit as st 
import pandas as pd 
from SrcNew.Controller.RunProcessingLayer1 import RunProcessingLayer1
from SrcNew.Controller.RunProcessingLayer2 import RunProcessingLayer2
from SrcNew.Model.SessionManager import SessionManager

class RunProcessingLayerMain:
    """"""
    def run(self, uploaded_file, type_form):
        """"""
        try : 
            ## Initialize Default 
            df_inline, df_noninline, df_fpd, df_polygon = None, None, None, None

            ## run Processing Layer 1 for Final Defects and First Pass Defects
            list_inline, list_noninline, list_fpd, df_polygon, error_page = RunProcessingLayer1().run(uploaded_file, type_form=type_form)
            print(f"Ini RunProcessLayerMain list_inline : {list_inline}")
            print(f"Ini RunProcessLayerMain list_noninline : {list_noninline}")
            print(f"Ini RunProcessLayerMain list_fpd : {list_fpd}")
            print(f"Ini RunProcessLayerMain df_polygon : {df_polygon}") 
            print(f"Ini RunProcessLayerMain error_page : {error_page}") 


            ## Looping Value 
            list_inlinerepair = [item1 for sublist1 in list_inline for item1 in sublist1]
            list_data_fpd = [item1 for sublist1 in list_fpd for item1 in sublist1]
            list_polygon = [item1 for sublist1 in df_polygon for item1 in sublist1]
            RunProcessingLayer2().run(df1=list_inlinerepair, df2=list_noninline, df3=list_data_fpd, df4=list_polygon, type_form=type_form)
            print(f"Ini Before if else RunProcessingLayerMain") 

            if type_form == "Final Defects" : 
                df_inline = SessionManager().get_setter_state('dataframe_inline') 
                df_noninline = SessionManager().get_setter_state('dataframe_noninline') 
                
                #df_inline = df_inline.drop(columns=['Repair'], axis=1)  
                df_noninline['page_num'] = df_noninline['Halaman'].str.extract(r'(\d+)').astype(int) 
                df_noninline = df_noninline.sort_values('page_num', ascending=True).reset_index(drop=True).drop(columns=['page_num']) 
            
            else : 
                print(f"Ini RunProcessingLayerMain") 
                df_fpd = SessionManager().get_setter_state('dataframe_fpd') 

            print(f"Done RunProcessingLayerMain")
            return df_inline, df_noninline, df_fpd, error_page
            
        except Exception as e : 
            st.error(f"Error in class RunProcessLayerMain (run) : {e}") 