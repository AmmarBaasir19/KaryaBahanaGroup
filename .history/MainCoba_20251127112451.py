import streamlit as st

# CSS tooltip
st.markdown("""
<style>
.tooltip {
  position: relative;
  display: inline-block;
  cursor: pointer;
  font-size: 22px;
}

.tooltip .tooltiptext {
  visibility: hidden;
  width: 430px;
  background-color: #F5AD9F;
  color: black;
  text-align: right; 
  border-radius: 6px;
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
    option1 = st.button(
        "🔁 Perbarui Semua Data Hasil Pindai",
        key="update_button",
        use_container_width=True
    )

with col2:
    st.markdown("""
        <div class="tooltip">ℹ️
            <span class="tooltiptext">
                <b>Informasi Tombol Simpan Data Hasil Pindai</b><br><br>
                • Menyimpan data hasil pindai ke penyimpanan data perusahaan.
            </span>
        </div>
    """, unsafe_allow_html=True) 
