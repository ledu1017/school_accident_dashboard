import streamlit as st
import numpy as np
from data_analysis.analysis import *
from content.side_bar import *
from content.chart import *

st.set_page_config(layout="wide")
line_layer = st.columns(1)
map_layer , type_layer , gender_layer = st.columns([0.5, 0.25, 0.25])
map_layer , area_school_layer = st.columns([0.5 , 0.5])
bottom_layer = st.columns(1)

def main():
    select_content = menu()

    line_chart(select_content)

    print('수정 끝')
    
if __name__ == "__main__":
    main()
