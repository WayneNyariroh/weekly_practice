import pandas as pd
import datetime
import streamlit as st
import streamlit_extras
from streamlit_extras.metric_cards import style_metric_cards

data = "FB_data.csv"
df = pd.read_csv(data)

st.set_page_config(
    page_title="Timeseries Analysis",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: visible;}
            """, unsafe_allow_html=True)

st.markdown("""
            <style>
            .block-container {padding-top: 1rem;}
            </style>
            """, unsafe_allow_html=True)

with st.sidebar:
    st.subheader("Timeseries Analysis")
    
with st.container():
    st.caption("Timeseries Analysis Metrics")
    metric1, metric2, metric3, metric4, metric5 = st.columns(5)
    
    with metric1:
        st.metric(label="Volume",
                  value=(f"${df.Volume.max()}"),
                  delta=(f"${df.Volume.min()}"))
    with metric2:
        st.metric(label="High",
                  value=(f"${df.High.max()}"),
                  delta=(f"${df.High.min()}"))
    with metric3:
        st.metric(label="Low",
                  value=(f"${df.Low.max()}"),
                  delta=(f"${df.Low.min()}"))
    with metric4:
        st.metric(label="Open",
                  value=(f"${df.Open.max()}"),
                  delta=(f"${df.Open.min()}"))
    with metric5:
        st.metric(label="Close",
                  value=(f"${df.Close.max()}"),
                  delta=(f"${df.Close.min()}"))
        
    style_metric_cards(background_color="#E4E4E4",
                       border_size_px=0.05,
                       border_radius_px=9,
                       border_left_color="green",
                    )
 
with st.container():
    st.write(df, use_container_width=True)