import pandas as pd 
import numpy as np 
import base64
import streamlit as st

if st.button("Generate & Auto Download"):
    content = pd.read_csv("Data.csv")
    st.dataframe(content)
    
    # Ubah DataFrame ke string
    text_data = content.to_csv(index=False)

    # Encode ke base64
    b64 = base64.b64encode(text_data.encode()).decode()

    # HTML auto download
    href = f"""
        <a href="data:text/plain;base64,{b64}" download="report.txt" id="download"></a>
        <script>
            document.getElementById("download").click();
        </script>
    """
    st.markdown(href, unsafe_allow_html=True)