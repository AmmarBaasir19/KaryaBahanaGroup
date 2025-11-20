import pandas as pd 
import streamlit as st
from streamlit_calendar import calendar

class MainCalender:
    def run(self):
        # Custom CSS untuk desain yang lebih modern dan responsif
        st.markdown("""
            <style>
            /* Main container styling */
            .main {
                padding: 1rem;
            }
    
            /* Header styling */
            .calendar-header {
                text-align: center;
                padding: 1.5rem 0;
                margin-bottom: 2rem;
                background: black;
                    /* linear-gradient(135deg, #667eea 0%, #764ba2 100%); */
                border: 4px solid red;
                border-radius: 15px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            }
    
            .calendar-header h1 {
                color: white;
                margin: 0;
                font-size: 2.5rem;
                font-weight: 700;
            }

            /* Responsive adjustments */
            @media (max-width: 768px) {
                .calendar-header h1 {
                    font-size: 1.8rem;
                }
                .calendar-container {
                    padding: 1rem;
                }
            }
    
            @media (max-width: 480px) {
                .calendar-header h1 {
                    font-size: 1.5rem;
                }
                .calendar-container {
                    padding: 0.5rem;
                }
            }
            </style>
        """, unsafe_allow_html=True)

        # Header
        st.markdown("""
            <div class="calendar-header">
                <h1>📅 Tugas Harian</h1>
            </div>
        """, unsafe_allow_html=True)

        # Calendar options dengan responsive view
        calendar_options = {
            "editable": False,
            "selectable": True,
            "headerToolbar": {
                "left": "today prev,next",
                "center": "title",
                "right": "dayGridMonth",
            },
            "navLinks": True,
            "dayMaxEvents": True,
            "height": "auto",
            "contentHeight": "auto", 
            "aspectRatio": 1.0,
        }

        # Custom CSS yang ditingkatkan
        custom_css = """
            /* Calendar styling */
            .fc {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
    
            /* Header toolbar */
            .fc-toolbar-title {
                text-align: center;
                font-size: 1.8rem !important;
                font-weight: 700 !important;
                color: white !important;
            }

            /* Buttons */
            .fc-button {
                background-color: black !important;
                border: 3px solid red !important; 
                border-radius: 10px !important;
                padding: 0.5rem 1.2rem !important;
                font-weight: 700 !important; 
                transition: all 0.3s ease !important;
            }

            .fc-button:hover {
                background-color: red !important;
                font-weight: 700 !important;
                color: white !important /* Hitam */;
                border: 3px solid red !important;  
                border-radius: 10px !important;
                transform: translateY(-2px) !important;
                box-shadow: 0 9px 20px rgba(100, 255, 100, 0.3); 
            }

            .fc-button-active {
                background-color: black !important;
            }

            /* Day headers */
            .fc-col-header-cell {
                background: black;
                border: 3px solid #FF0000; !important;
                color: white !important;
                font-weight: 700 !important;
                padding: 1rem 0.5rem !important;
            }
    
            /* Day cells */
            .fc-daygrid-day {
                transition: background-color 0.3s ease !important;
            }

            .fc-daygrid-day:hover {
                background-color: red !important; 
            }
    
            .fc-day-today {
                background-color: red !important;
            }

            /* Events */
            .fc-event {
                border: 3px solid white; 
                border-radius: 6px !important;
                padding: 4px 8px !important;
                margin: 2px 4px !important;
                font-weight: 600 !important;
                background-color: black;
                transition: all 0.2s ease !important;
            }

            .fc-event:hover {
                border: 3px solid white;
                transform: translateY(-2px) !important;
                box-shadow: 0 4px 10px rgba(0,0,0,0.2) !important;
            }

            .fc-event-past {
                opacity: 0.7;
            }
    
            .fc-event-time {
                font-style: italic;
                font-weight: 500;
            }

            .fc-event-title {
                font-weight: 700 !important;
                color: white;
            }

            /* Grid lines */
            .fc-scrollgrid {
                border: 3px solid red !important;
                border-radius: 10px !important;
                overflow: hidden !important;
            }
    
            .fc-theme-standard td, 
            .fc-theme-standard th {
                border: 2px solid red !important;
                border-radius: 10px !important;
            }

            /* Responsive */
            @media (max-width: 768px) {
                .fc-toolbar-title {
                    font-size: 1.4rem !important;
                }

                .fc-button {
                    padding: 0.4rem 0.8rem !important;
                    font-size: 0.85rem !important;
                }
        
                .fc-event {
                    font-size: 0.85rem !important;
                }
            }

            @media (max-width: 480px) {
                .fc-toolbar-title {
                    font-size: 1.2rem !important;
                }

                .fc-button {
                    padding: 0.3rem 0.6rem !important;
                    font-size: 0.75rem !important;
                }

                .fc-toolbar {
                    flex-direction: column !important;
                    gap: 0.5rem !important;
                }
            }
        """

        ## Connect To Database to Get Calender Data 
        df = pd.read_csv("home/cortex/Medallion_Hub/Karya_Bahana_Apps/Calender_DB/Data_Calender.csv")
        df['start'] = pd.to_datetime(df['production_date']).dt.strftime('%Y-%m-%d')

        calender_events = df.to_dict(orient="records") 
        for event in calender_events:
            event['title'] = f"✅ {event.get('title', '')}"  
        

        # Calendar dalam container 
        with st.container():
            st.markdown('<div class="calendar-container">', unsafe_allow_html=True)

            calendar_result = calendar(
                events=calender_events,
                options=calendar_options, 
                custom_css=custom_css,
                key='calendar',
            )
    
            st.markdown('</div>', unsafe_allow_html=True)