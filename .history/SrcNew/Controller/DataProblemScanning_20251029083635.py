import os  
from io import BytesIO
from PIL import Image
import streamlit as st 
from PyPDF2 import PdfReader, PdfWriter, PdfMerger
from SrcNew.View.ComponentsButton import ComponentsButton


class DataProblemScanning:
    def __split_pdf(self, input_path, output_path, error_page):
        """"""
        try : 
            os.makedirs(output_path, exist_ok=True)
            reader = PdfReader(input_path)
            total_pages = len(reader.pages) 

            for i in error_page:
                i = i - 1
                if 0 <= i < total_pages:
                    writer = PdfWriter()
                    writer.add_page(reader.pages[i])
                    output_path = os.path.join(output_path, f"Error_Scanning_Page_{i+1}.pdf")
                    with open(output_path, "wb") as f:
                        writer.write(f)

                
                else : 
                    st.warning(f"⚠️ Index {i} di luar jangkauan. Total halaman hanya {total_pages}.")

        except Exception as e :
            st.error(f"Error in class DataProblemScanning (__split_pdf) : {e}") 
    
    def __merge_pdf_folder(self, input_folder):
        """"""
        try :
            merger = PdfMerger()
            pdf_files = sorted([f for f in os.listdir(input_folder) if f.endswith('.pdf')])

            for pdf_file in pdf_files:
                merger.append(os.path.join(input_folder, pdf_file))
            
            merged_bytes = BytesIO()
            merger.write(merged_bytes)
            merger.close()
            merged_bytes.seek(0)
            return merged_bytes

        except Exception as e :
            st.error(f"Error in class DataProblemScanning (__merge_pdf_folder) : {e}") 
    
    def run(self, input_pdf, error_page, file_name, type_form):
        """
        ------------------------------
        Parameter :
            - input_pdf : Path or Input PDF Users
            - error_page : The number of Error Page (Page Can't Scanning)
            - file_name : The Name of File Problem
        """
        try : 
            split_output_folder = "apps/storage/PDF_Problem"
            self.__split_pdf(input_pdf, split_output_folder, error_page) 

            ## Merged PDF
            merged_pdf = self.__merge_pdf_folder(split_output_folder) 

            ## Download File Problem 
            if ComponentsButton().button_error(merged_pdf, file_name, type_form): 
                st.write(f"Done Download")
        
        except Exception as e : 
            st.error(f"Error in class DataProblemScanning (run) : {e}")