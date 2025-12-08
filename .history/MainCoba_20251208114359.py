import pandas as pd 
import numpy as np 
import base64
import streamlit as st

if st.button("Generate & Auto Download"):
    content = pd.read_csv("Book1.xlsx")
    st.write(type(content))

    b64 = base64.b64encode(content.encode()).decode()
    href = f'''
        <a href="data:file/txt;base64,{b64}" download="report.txt" id="download"></a>
        <script>
            document.getElementById("download").click();
        </script>
    '''
    st.markdown(href, unsafe_allow_html=True)