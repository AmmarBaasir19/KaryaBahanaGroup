import os 
import yaml
import requests
import streamlit as st 
from typing import Dict, Any
from SrcNew.Controller.ControllerPath import ControllerPath
from azure.core.credentials import AzureKeyCredential 
from azure.ai.documentintelligence import DocumentIntelligenceClient 
from azure.ai.documentintelligence.models import AnalyzeResult, AnalyzeDocumentRequest, DocumentAnalysisFeature 

class Model:
    """"""
    def __init__(self, path_document):
        """"""
        try : 
            self.keys1 = ControllerPath().api_keys 
            self.endpoint = ControllerPath().api_endpoint

            self.result_dict = self.run(path_document)
        
        except Exception as e :
            st.error(f"Error in class Model (__init__) : {e}")
    
    def run(self, path_document):
        """"""
        try : 
            document_intelligence_client = DocumentIntelligenceClient(endpoint=self.endpoint, credential=AzureKeyCredential(self.keys1)) 

            ## Confirm Correct Path 
            if not os.path.exists(path_document):
                print(f"File tidak ditemukan di path: {path_document}")
                return None 

            try:
                with open(path_document, "rb") as f:
                    poller = document_intelligence_client.begin_analyze_document(
                        model_id="prebuilt-layout",
                        body=f,
                        content_type="application/octet-stream",
                        # features=[DocumentAnalysisFeature.OCR_HIGH_RESOLUTION],  # Jika perlu fitur tambahan
                    )
                    result: AnalyzeResult = poller.result()
                
                    ## Process result analysis from model OCR and return data in dictionary format 
                    result_dict = { 
                        'tables': [{'cells': [{'rowIndex': cell.row_index, 'columnIndex': cell.column_index, 'content': cell.content}
                                          for cell in table.cells]} for table in result.tables],
                        'pages': [{'words': [{'content': word.content} for word in page.words]} for page in result.pages],
                        'polygon' : [
                            {
                                f"Table_{index+1}" : region['polygon']
                            }
                            for index, table in enumerate(result.tables) for region in table['boundingRegions']]
                    }

                    return result_dict
                
            except Exception as e: 
                print(f"Terjadi Kesalahan Pada Model OCR Saat Memproses Dokumen : {e}")
                return None
        
        except Exception as e : 
            st.error(f"Error in class Model (config_model) : {e}") 
    
    def __call__(self):
        try : 
            return self.result_dict 
        
        except Exception as e : 
            st.error(f"Error in class Model (__call__) : {e}")