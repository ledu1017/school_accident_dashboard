import streamlit as st
import numpy as np
from data_analysis.analysis import *
from content.side_bar import *
from content.chart import *

# Page configuration
st.set_page_config(
    page_title="학교 안전사고 대시보드",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
    }
    .main-header h1 {
        margin: 0;
        font-size: 2.5rem;
        font-weight: bold;
    }
    .main-header p {
        margin: 0.5rem 0 0 0;
        font-size: 1.2rem;
        opacity: 0.9;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #4ECDC4;
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown("""
<div class="main-header">
    <h1>🏫 학교 안전사고 대시보드</h1>
    <p>2020-2022년 학교 안전사고 데이터 분석 및 시각화</p>
</div>
""", unsafe_allow_html=True)

# Layout setup
line_layer = st.columns(1)
map_layer, type_layer, gender_layer = st.columns([0.5, 0.25, 0.25])
map_layer, area_school_layer = st.columns([0.5, 0.5])
bottom_layer = st.columns(1)

def main():
    # Get selected content from sidebar
    select_content = menu()

    # Display chart
    with st.container():
        st.markdown("### 📊 사고 발생 추이 분석")
        line_chart(select_content)
    
    # Add some spacing
    st.markdown("---")
    
    # Footer
    st.markdown("""
    <div style="text-align: center; padding: 2rem; color: #666;">
        <p>🏫 학교 안전사고 대시보드 | 데이터 기반 안전 관리 시스템</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
