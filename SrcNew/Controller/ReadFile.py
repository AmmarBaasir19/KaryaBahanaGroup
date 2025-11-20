import os 
import cv2
import streamlit as st
from typing import Any 
from datetime import datetime, timedelta 
from pdf2image import convert_from_path

class ReadFile:
    """
    This class will be process to transform OCR Data to Dataframe Format
    """
    def __init__(self, data): 
        """
        This Function will be define path for folder upload and images
        """

        try : 
            ## Define Path Folder
            self.upload_folder = "apps/storage/PDF_Temporary"
            self.images_folder = "apps/storage/Images_Temporary"

            ## Check Folder and Make Folder
            os.makedirs(self.upload_folder, exist_ok=True)
            os.makedirs(self.images_folder, exist_ok=True)

            self.images_convert, self.read_file = self.Main(data)

        except Exception as e :
            st.error(f"Error in class ReadFile (__init__) : {e}")

    def saved_uploaded_file(self, uploaded_file): 
        """
        This function to save file pdf from uploaded user to specific folder
        """
        print(f"Ini saved_uploaded_file : {uploaded_file}")
        print(f"Ini saved_uploaded_file name : {uploaded_file}")
        try :
            ## Save File PDF 
            file_path = os.path.join(self.upload_folder, uploaded_file)
            with open(file_path, "wb") as f: 
                f.write(uploaded_file.getbuffer()) 
            return file_path  
        
        except Exception as e : 
            st.error(f"Error in class ReadFile (saved_uploaded_file) : {e}")
    
    def read_pdf(self, file_path: str): 
        """
        This function will be read file pdf and convert from pdf format to png format
        """

        try :
            print(f"Ini read_pdf : {file_path}") 
            images = convert_from_path(file_path)  

            images_list = []  

            ## Run Process Convert PDF to PNG
            for i, image in enumerate(images):
                image_path = os.path.join(self.images_folder, f'page_{i + 1}.png')
                image.save(image_path, 'PNG', optimize=True)
                images_list.append(image_path)
        
            return images_list

        except Exception as e :
            st.error(f"Error in class ReadFile (read_pdf) : {e}") 
    
    def convert_grayscale(self, images: Any):
        """
        This function will be convert images RGB in folder Images_Temporary(self.images_folder) to GrayScale
        """

        try : 
            images_list = []

            ## Run Process Convert Grayscale
            for i, image in enumerate(images):
                img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
                image_path = os.path.join(self.images_folder, f'page_{i + 1}.png')
                images_list.append(image_path)
        
            return images_list
        
        except Exception as e : 
            st.error(f"Error in class ReadFile (convert_grayscale) : {e}")
    
    def Main(self, data):
        """
        This Function will be run (process) several function above :
        1. Function saved_uploaded_file
        2. Function read_pdf
        3. Function convert_grayscale 
        """

        try :
            ## Call Several Function
            #read_file = self.saved_uploaded_file(data)
            read_file = "File_PDF.pdf" 
            read_images = self.read_pdf("Temporary/File_PDF.pdf")
            images_convert = self.convert_grayscale(read_images)

            return images_convert, read_file
        
        except Exception as e : 
            st.error(f"Error in class ReadFile (Main) : {e}")


    def __call__(self): 
        try :
            ## Return File After Processing
            return self.images_convert, self.read_file
        
        except Exception as e : 
            st.error(f"Error in class ReadFile (__call__) : {e}") 