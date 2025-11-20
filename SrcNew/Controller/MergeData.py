import streamlit as st 
import os 
import shutil
from PyPDF2 import PdfMerger
from datetime import datetime, timedelta
from SrcNew.View.ComponentsStyle import ComponentsStyle
from SrcNew.Controller.ControllerPath import ControllerPath


class MergeData:
    def __init__(self):
        """"""
        self.timestamp = datetime.now().strftime("%d-%B-%Y")
        self.yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d") 
        self.now = datetime.now().strftime("%Y-%m-%d")

    def _merge_pdfs(self, pdf_file):
        """ Menggabungkan daftar file PDF menjadi satu file """
        try : 
            merger = PdfMerger()    
            for pdf_file in pdf_file:
                merger.append(pdf_file) 
            output_filename = "gabungan.pdf"
            with open(output_filename, "wb") as output_pdf:
                merger.write(output_pdf) 
            merger.close()
            return output_filename 

        except Exception as e : 
            st.error(f"Error in class MergeData (_merge_pdfs) : {e}")
    
    def run(self):
        try : 
            ## Upload File PDF From Users
            uploaded_files = ComponentsStyle().display_uploaded(True) 

            print(uploaded_files)

            ## Check Len Upload File
            if uploaded_files:
                if len(uploaded_files) < 2:
                    st.warning("Mohon unggah setidaknya dua file PDF untuk digabungkan.")
                
                else :   
                    with st.popover(label="Pilih Tipe Form", use_container_width=True ):
                        st.markdown("Mohon Pilih Tipe Form Yang Ingin Digabungkan 👋")
                        name = st.selectbox(label="Tipe Form?", options=["First Pass Yield", "Final Yield"], index=0)
                        output_pdf_path = self._merge_pdfs(uploaded_files)

                        with open(output_pdf_path, "rb") as f: 
                            if name == "First Pass Yield" : 
                                if st.download_button( 
                                    label="Unduh PDF Gabungan",
                                    data=f.read(), 
                                    file_name=f"FRM-QC-026_rev3_{self.timestamp}_Merge_File.pdf", 
                                    mime="application/pdf",
                                    use_container_width=True 
                                    ) : 
                                    save_path = os.path.join(ControllerPath().directory_12['path'], f"FRM-PRD-XXX_SCAN_{self.now}_PROD_{self.yesterday}.pdf")
                                    shutil.copy(output_pdf_path, save_path)

                            else : 
                                if st.download_button( 
                                    label="Unduh PDF Gabungan",
                                    data=f.read(), 
                                    file_name=f"FRM-QC-026_rev3_{self.timestamp}_.pdf", 
                                    mime="application/pdf",
                                    use_container_width=True 
                                    ) :
                                    save_path = os.path.join(ControllerPath().directory_11['path'], f"FRM-QC-026_SCAN_{self.now}_CHECKED_{self.yesterday}.pdf") 
                                    shutil.copy(output_pdf_path, save_path)
        
        except Exception as e : 
            st.error(f"Error in class MergeData (run) : {e}") 