import re 
import pandas as pd 
from datetime import datetime
import streamlit as st 
from fuzzywuzzy import process
from SrcNew.Controller.DataValidation1 import DataValidation1
from SrcNew.Controller.ControllerPath import ControllerPath

class DataValidation2:
    """"""
    def convert_to_int(self, value: str) -> int:
        """
        This function will be convert value to integer, 
        if value is not integer will return 0
        """ 
        try :
            try :
                return int(value)
            except (ValueError, TypeError): 
                return 0 
            
        except Exception as e:
            st.error(f"Error in class DataValidation2 (_convert_to_int) : {e}")
     
    def invalid_convert_int(self, value: str) -> str :
        """
        This function will be convert value to integer, 
        if value is not integer will return 0
        """
        try :
            try :
                return int(value)
            except (ValueError, TypeError): 
                return "Invalid Converted to INT" 
            
        except Exception as e:
            st.error(f"Error in class DataValidation2 (_invalid_convert_int) : {e}")
    
    def invalid_shift(self, value: str) -> str : 
        """
        This function will be validate shift (result ocr), 
        if value is not integer or value is greater than 3 will return "Invalid Shift"
        """
        try :
            try :
                if int(value) > 3 or int(value) == 0:
                    return "Invalid Type Shift"
            except:
                return value
            return value
        
        except Exception as e:
            st.error(f"Error in class DataValidation2 (invalid_type_4) : {e}")
    

    def invalid_type_1(self, value: str) -> str:
        """
        This function will be validate years (result ocr), 
        if value is not integer or value is greater than years now will return "Invalid Type 1"
        """
        try :
            try : 
                if int(value) > int(datetime.now().year):
                    return "Invalid Type 1"
                elif int(value) < int(datetime.now().year): 
                    return "Invalid Type 1" 
                elif len(str(value)) != 4:
                    return "Invalid Type 1"
            except ValueError: 
                return value
            return value
        
        except Exception as e:
            st.error(f"Error in class DataValidation2 (invalid_type_1) : {e}") 
    
    def invalid_type_2(self, value: str) -> str:
        """
        This function will be validate months (result ocr), 
        if value is not integer or value is greater than months now will return "Invalid Type 2"
        """
        try :
            try : 
                if int(value) > int(datetime.now().month):
                    return "Invalid Type 2"
                elif int(value) < 1 and int(value) > 12:
                    return "Invalid Type 2"
            except ValueError:
                return value
            return value
        
        except Exception as e: 
            st.error(f"Error in class DataValidation2 (invalid_type_2) : {e}") 
    
    def invalid_type_3(self, value: str) -> str:
        """
        This function will be validate days (result ocr),
        if value is not integer or value is greater than days now will return "Invalid Type 3"
        """
        try :
            try : 
                if int(value) > int(datetime.now().day):
                    return "Invalid Type 3"
                elif int(value) < 1 and int(value) > 31:
                    return "Invalid Type 3" 
            except ValueError:
                return value 
            return value
        
        except Exception as e:
            st.error(f"Error in class DataValidation2 (invalid_type_3) : {e}") 
    
    def invalid_type_4(self, value: str) -> str : 
        """
        This function will be validate shift (result ocr), 
        if value is not integer or value is greater than 3 will return "Invalid Shift"
        """
        try :
            try:
                return int(value) 
            except (ValueError, TypeError): 
                return 'Invalid Type 4' 
        except Exception as e : 
            st.error(f"Error in DataValidation2 (invalid_type_4) : {e}") 
    
    def invalid_type_5(self, value: str) -> str : 
        """"""
        try : 
            for i in range(6):
                if int(value[i]) > int(value[-1]):
                    value[i] = 'Invalid Type 5' 
            return value 

        except Exception as e : 
            st.error(f"Error in DataValidation2 (invalid_type_5) : {e}")  
    
    def invalid_type_6(self, data: str) -> str:
        """
        This function will be validate value welding check points (KEROPOS, KURANG, BOLONG, UNDERCUT, SPATTER, TIDAK TEPAT), 
        IF value is greater than quantity repair will return "Invalid Type 5"
        """
        try : 
            for i in range(6):
                if int(data[i]) > int(data[-1]):
                    data[i] = 'Invalid Type 6' 
            return data 

        except Exception as e : 
            st.error(f"Error in class DataValidation2 (invalid_type_6) : {e}")  
     
    def invalid_type_7(self, data: str) -> str:
        """ 
        This function will be validate value non welding (KASAR, RETAK, DEFORMASI, PENYOK, DIMENSI, FUNGSI, KARAT, SALAH PASANG, GORESAN, TIDAK LENGKAP),
        IF value is greater than quantity repair will return "Invalid Type 7 (for Type Form Final Defects)"
        """
        try :
            for col in DataValidation1().list_spot6: 
                if int(data[col]) > int(data["REPAIR"]):
                    data[col] = 'Invalid Type 7'
            return data
        
        except Exception as e : 
            st.error(f"Error in class DataValidation2 (invalid_type_7) : {e}")
    
    def validation_qty(self, value, type_form):
        """"""
        try :
            ## Convertion Data to INT Type.
            def parse_int(x):
                if isinstance(x, int):
                    return x
                elif isinstance(x, str):  
                    return int(x) if x.isdigit() else "Invalid Scanning"
                else:
                    return "Invalid Scanning" 
                
            if type_form == "Final Defects" :
                quantity_value = parse_int(value[0])

                data_int = [parse_int(x) for x in value[1:]]

                if quantity_value == "Invalid Scanning":
                    data_return = ["Invalid Scanning"] + data_int
                    return data_return 
        
                try: 
                    if sum(data_int) != quantity_value:
                        data_return = [quantity_value] + ["Invalid Type 8"] * len(data_int)
                        return data_return
                    else :
                        data_return = [quantity_value] + data_int
                        return data_return
            
                except Exception as e:
                    data_return = [quantity_value] + data_int

                return data_return
            
            else : 
                quantity_value = parse_int(value[0])

                data_int = [parse_int(x) for x in value[1:]]

                if quantity_value == "Invalid Scanning": 
                    data_return = ["Invalid Scanning"] + data_int
                    return data_return 
                try :
                    if any(x > quantity_value for x in data_int[:3]):
                        return [quantity_value] + ["Invalid Type 8"] * len(data_int)
                
                except Exception as e : 
                    data_return = [quantity_value] + data_int
                
                return data_return

        except Exception as e :
            st.error(f"Error in class DataValidation2 (validate_qty) : {e}")
    
    def dataframe_result_validation(self, data, a, b, c):
        try :
            value_filter = [val for val in data[a:b]]
            value_filter.append(data[c]) 
            value_int = [self.convert_to_int(val) for val in value_filter]
            invalid_type_4_df = [self.invalid_type_4(val) for val in value_filter]
            invalid_type_5_df = self.invalid_type_5(value_int)
            dataframe_final = self.invalid_grouping(invalid_type_4_df, invalid_type_5_df) 
            return dataframe_final

        except Exception as e:
            st.error(f"")

    def invalid_grouping(self, value1, value2):
        """"""
        try : 
            combined_data = []
            for val_1, val_2 in zip(value1, value2):
                if val_1 != val_2:
                    if "Invalid" in str(val_1) and "Invalid" in str(val_2):
                        combined_data.append(f"{val_1} & {val_2}")
                    elif "Invalid" in str(val_1):
                        combined_data.append(val_1)
                    else:
                        combined_data.append(val_2)
                else: 
                    combined_data.append(val_2)
            return combined_data
        
        except Exception as e: 
            st.error(f"Error in class DataValidation2 (invalid_grouping) : {e}")
        
    def validate_quantity(self, data):
        try :
            ## Convertion Data to INT Type.
            def parse_int(x):
                if isinstance(x, int):
                    return x
                elif isinstance(x, str):  
                    return int(x) if x.isdigit() else "Invalid Scanning"
                else:
                    return "Invalid Scanning" 
        
            quantity_value = parse_int(data[0])

            data_int = [parse_int(x) for x in data[1:]]

            if quantity_value == "Invalid Scanning":
                data_return = ["Invalid Scanning"] + data_int
                return data_return 
        
            try: 
                if sum(data_int) != quantity_value:
                    data_return = [quantity_value] + ["Invalid Type 5"] * len(data_int)
                    return data_return
                else :
                    data_return = [quantity_value] + data_int
                    return data_return
            
            except Exception as e:
                data_return = [quantity_value] + data_int

            return data_return

        except Exception as e :
            st.error(f"Error in DataValidation2 (validate_quantity) : {e}")
    
    def data_regex1(self, data, a, b):
        """"""
        try : 
            regex = {'£' : '0', '00' : '0', '000' : '0', '#' : '0',  '0000' : '0', '0.0' : '0', '0.00' : '0', '.' : '0'}

            pattern_regex = re.compile('|'.join(map(re.escape, regex.keys())))
            cleaned_data = [pattern_regex.sub(lambda match: regex[match.group()], str(row)) for row in data[-a:-b]] 
            data[-a:-b] = cleaned_data 
            return data

        except Exception as e :
            st.error(f"Error in class DataValidation2 (data_regex1) : {e}")
    
    def data_regex2(self, data, a, b):
        """"""
        try : 
            regex = {'£' : '', '!' : '', '$' : '', '%': '', '*' : '', '^' : ''}

            pattern_regex = re.compile('|'.join(map(re.escape, regex.keys())))
            cleaned_data = [pattern_regex.sub(lambda match: regex[match.group()], str(row)) for row in data[-a:-b]] 
            data[-a:-b] = cleaned_data 
            return data

        except Exception as e :
            st.error(f"Error in class DataValidation2 (data_regex2) : {e}")
    
    def fuzzy_matching1(self, value: str, threshold=95) -> str:
        """"""
        try :
            match, score = process.extractOne(value, ControllerPath().part_no) 
            if score <= threshold: 
                return match
            else: 
                return value
        
        except Exception as e :
            st.error(f"Error in class DataValidation2 (fuzzy_matching1) : {e}")
    
    def fuzzy_matching2(self, value: str, threshold=95) -> str : 
        """"""
        try :
            match, score = process.extractOne(value, ControllerPath().part_name)
            if score <= threshold:
                return match
            else:
                return value 
        
        except Exception as e : 
            st.error(f"Error in DataValidation2 (fuzzy_matching2) : {e}")