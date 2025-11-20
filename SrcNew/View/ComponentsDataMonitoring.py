import streamlit as st 

class ComponentsDataMonitoring:
    """"""
    def set_delta_value(self, delta):
        """"""
        if delta >= 0:
            arrow = "▲" 
            arrow_class = "arrow-up"
            delta_class = "delta-value-up"

        else:
            arrow = "▼"
            arrow_class = "arrow-down"
            delta_class = "delta-value-down"
        
        return arrow, arrow_class, delta_class
   
    def set_delta_format(self, delta): 
        """"""
        if type(delta) == float:
           formatted_delta = f"{abs(delta)}%"
    
        else :
           formatted_delta = f"{abs(delta)}"
        
        return formatted_delta
   
    def metric_html(self, label, value, delta_value, delta_format):
        """"""
        metric_html = f"""
            <style>
                .metric-box {{
                    background-color: #2B2B30;
                    padding: 1rem;
                    border-radius: 15px;
                    border: 2px solid #ff0000; 
                    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
                    text-align: center;
                    font-family: 'Segoe UI', sans-serif; 
                    margin-top: 10px;
                }}
                .metric-label {{
                    color: #FFFFFF;
                    font-size: 1rem;
                    font-weight: bold;
                }}
                .metric-value {{
                    font-size: 2.5rem;
                    font-weight: bold;
                    color: #FFFFFF;
                }}
                .arrow-up {{
                    color: green;
                    margin-left: 8px;
                    font-size: 1rem;
                }}
                .arrow-down {{
                    color: #ff0000;
                    margin-left: 8px;
                    font-size: 1rem;
                }}
                .delta-value-up {{
                    color: green;
                    font-size: 1rem;
                    font-weight: bold;
                }}
                .delta-value-down {{
                    color: #ff0000;
                    font-size: 1rem; 
                    font-weight: bold; 
                }}
            </style> 

            <div class="metric-box">
                <div class="metric-label">{label}</div>
                <div class="metric-value">{value}</div>
                <div>
                    <span class="{delta_value[2]}">{delta_format}</span>
                    <span class="{delta_value[1]}">{delta_value[0]}</span>
                </div>
            </div>
        """
       
        return metric_html
   
    def processing_value_metric(self, data1, data2):
        """"""
        denominator = data1 + data2
        if int(denominator) == 0 : 
            values = 0.00
        
        else : 
            values = round((data2/denominator * 100), 2) 

        return values 
       
    def run(self, data1, data2):
        """
        --------------------------
        Parameter : 
            - data1 : Is Total Data Invalid
            - data2 : Is Total Data Valid
        """
        metric_container = st.container()
        with st.container(): 
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown(self.metric_html("Jumlah Data Invalid", data1, self.set_delta_value(-data2), self.set_delta_format(data1)), unsafe_allow_html=True)
            
            with col2:
                st.markdown(self.metric_html("Jumlah Data Valid", data2, self.set_delta_value(data1), self.set_delta_format(data1)), unsafe_allow_html=True) 
            
            with col3:
                st.markdown(self.metric_html("Persentase Data Valid", self.set_delta_format(self.processing_value_metric(data1, data2)), self.set_delta_value(self.processing_value_metric(data1, data2) - 100), self.set_delta_format(round(100 - self.processing_value_metric(data1, data2), 2))), unsafe_allow_html=True)