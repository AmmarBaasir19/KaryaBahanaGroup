import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.types import Integer, String, Float, Date, DateTime, Boolean

class DatabaseConfig:
    def connect_to_db(self):
        """"""
        try:
            engine = create_engine('postgresql+psycopg2://adminkbbkbu:adminkbbkbu_io@localhost:5432/kb_group',
                                    connect_args={'options': '-c search_path=bronze_layer'})
            connection = engine.connect()
            print("Connection to the database was successful.")
            return connection

        except Exception as e:  
            print(f"An error occurred: {e}")
    
    def mapping_fd_inline(self):
        """"""
        dtype_fd_inline = {
            "model": String(15),
            "part_no": String(12),
            "part_name": String(50),
            "ttd_kasie": String(3),
            "ttd_operator": String(3),
            "nik_operator": String(15),
            "tahun": Integer,
            "bulan": Integer,
            "tanggal": Integer,
            "shift": Integer,
            "welding_check_points": Integer,
            "keropos": Integer,
            "kurang": Integer,
            "bolong": Integer,
            "undercut": Integer,
            "spatter": Integer,
            "tidak_tepat": Integer
        }

        return dtype_fd_inline
    
    def mapping_fd_noninline(self):
        """"""
        dtype_fd_noninline = {
            "model": String(15),
            "part_no": String(12),
            "part_name": String(50),
            "ttd_kasie": String(3),
            "ttd_operator": String(3),
            "nik_operator": String(15),
            "tahun": Integer,
            "bulan": Integer,
            "tanggal": Integer,
            "shift": Integer,
            "checked": Integer,
            "ok": Integer,
            "repair": Integer,
            "scrap": Integer,
            "folding_Keras": Integer,
            "karat": Integer,
            "deformasi": Integer,
            "cat_coating": Integer,
            "tidak_masuk_gonogo": Integer,
            "step_loss": Integer,
            "step_loncat": Integer,
            "step_lebih": Integer,
            "step_kurang": Integer,
            "salah_pasang": Integer,
            "goresan": Integer,
            "noisy": Integer,
            "tidak_lengkap": Integer,
            "catatan": String(50),
            "title": String(25),
            "file_name_dataset": String(50),
            "start_processing": String(50),
            "end_processing": String(50),
            "time_processing_all": String(20),
            "time_processing_page": String(20),
            "login_id": String(30),
            "table_1": String(50),
            "table_2": String(50), 
            "table_3": String(50),
            "table_4": String(50),
            "table_5": String(50),
            "table_6": String(50),
        }

        return dtype_fd_noninline
    
    def mapping_fpd(self):
        """"""
        dtype_fpd = {
            "model": String(15),
            "part_no": String(12),
            "part_name": String(50),
            "part_group": String(6),
            "nik_nipm": String(15),
            "tahun": Integer,
            "bulan": Integer,
            "tanggal": Integer,
            "shift": Integer,
            "total_repair": Integer,
            "total_top": Integer,
            "total_middle": Integer,
            "total_bottom": Integer,
            "title": String(25),
            "file_name_dataset": String(50),
            "start_processing": String(50),
            "end_processing": String(50),
            "time_processing_all": String(20),
            "time_processing_page": String(20),
            "login_id": String(30),
            "table_1": String(50),
            "table_2": String(50)
        }

        return dtype_fpd
        
    def mapping_users_activity(self):
        """"""
        dtype_users_activity = {
            "username": String(10),
            "name": String(25),
            "nik_nipm": String(15),
            "role": String(15),
            "location": String(6),
            "login_id": String(30)
        }

        return dtype_users_activity