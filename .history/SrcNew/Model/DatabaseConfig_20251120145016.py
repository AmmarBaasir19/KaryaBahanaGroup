import pandas as pd
import streamlit as st 
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
            "halaman": String(10),
            "model": String(15),
            "part_no": String(12),
            "part_name": String(50),
            "ttd_kasie": String(3),
            "ttd_operator": String(3),
            "nik_nipm": String(15),
            "tahun": String(5),
            "bulan": String(5),
            "tanggal": String(5),
            "shift": String(5),
            "welding_check_points": String(5),
            "keropos": String(5),
            "kurang": String(5),
            "bolong": String(5),
            "undercut": String(5),
            "spatter": String(5),
            "tidak_tepat": String(5),
        }

        return dtype_fd_inline
    
    def mapping_fd_noninline(self):
        """"""
        dtype_fd_noninline = {
            "halaman": String(10),
            "model": String(15),
            "part_no": String(12),
            "part_name": String(50),
            "ttd_kasie": String(3),
            "ttd_operator": String(3),
            "nik_nipm": String(15),
            "tahun": String(5),
            "bulan": String(5),
            "tanggal": String(5),
            "shift": String(5),
            "checked": String(5),
            "ok": String(5),
            "repair": String(5),
            "scrap": String(5),
            "folding_Keras": String(5),
            "karat": String(5),
            "deformasi": String(5),
            "cat_coating": String(5),
            "tidak_masuk_gonogo": String(5),
            "step_loss": String(5),
            "step_loncat": String(5),
            "step_lebih": String(5),
            "step_kurang": String(5),
            "salah_pasang": String(5),
            "goresan": String(5),
            "noisy": String(5),
            "tidak_lengkap": String(5),
            "catatan": String(50),
            "title": String(25),
            "file_name_dataset": String(200),
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
            "halaman": String(10),
            "model": String(15),
            "part_no": String(12),
            "part_name": String(50),
            "part_group": String(6),
            "nik_nipm": String(15),
            "tahun": String(5),
            "bulan": String(5),
            "tanggal": String(5),
            "shift": String(5),
            "total_repair": String(5),
            "total_top": String(5),
            "total_middle": String(5),
            "total_bottom": String(5),
            "title": String(25),
            "file_name_dataset": String(200),
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
    
    def connect_to_db(self):
        """"""
        try:
            engine = create_engine('postgresql+psycopg2://adminkbbkbu:adminkbbkbu_io@localhost:5432/kb_group',
                                    connect_args={'options': '-c search_path=bronze_layer'})
            connection = engine.connect()
            print("Connection to the database was successful.")
            return connection

        except Exception as e:  
            st.error(f"An error occurred: {e}")
    
    def get_database(self, start_date: str, end_date: str, db_name: str, col_name: list) -> pd.DataFrame:
        """"""
        try : 
            if isinstance(col_name, list):
                columns = ", ".join(col_name)
            else : 
                columns = col_name

            template_query = text(f"""
                                SELECT 
                                    {columns},
                                    MAKE_DATE(tahun::INT, bulan::INT, tanggal::INT) AS production_date 
                                FROM 
                                    bronze_layer.{db_name}
                                WHERE
                                    MAKE_DATE(tahun::INT, bulan::INT, tanggal::INT) BETWEEN :start AND :end;
                                """)
            df = pd.read_sql_query(sql=template_query, con=self.connect_to_db(), params={'start' :start_date, 'end' :end_date})

            return df
    
        except Exception as e : 
            st.error(f"Error in class DatabaseConfig (get_database): {e}")    
    
    def get_calender_db(self):
        """"""
        try : 
            query = text("""
                         WITH combined_calender AS (
                            SELECT 
                                title, MAKE_DATE(tahun::INT, bulan::INT, tanggal::INT) AS production_date
                            FROM 
                                bronze_layer.fd_noninline
                            WHERE
                                title IS NOT NULL
        
                            UNION ALL

                            SELECT
                                title, MAKE_DATE(tahun::INT, bulan::INT, tanggal::INT) AS production_date
                            FROM
                                bronze_layer.fpd
                            WHERE
                                title IS NOT NULL
                         )

                        SELECT
                            DISTINCT title, production_date
                        FROM 
                            combined_calender;
                         """)
            
            df = pd.read_sql_query(sql=query, con=self.connect_to_db())

            return df
        
        except Exception as e : 
            st.error(f"Error in class DatabaseConfig (get_calender_db): {e}")
    