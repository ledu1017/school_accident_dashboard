import streamlit as st
import numpy as np
from data_analysis.analysis import *

# Custom CSS for better styling
st.markdown("""
<style>
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
    .stSelectbox > div > div > div > div {
        background-color: white;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
    }
    .stSlider > div > div > div > div {
        background-color: #4ECDC4;
    }
    .stDateInput > div > div > div > div {
        background-color: white;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
    }
    .metric-container {
        background-color: white;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        margin: 5px 0;
    }
</style>
""", unsafe_allow_html=True)

data = date_accident_count()    # 날짜별 사고수 데이터

school_grades_category = {
    '전체' : ['전체', '유아', '1학년', '2학년', '3학년', '4학년', '5학년', '6학년'],
    '유치원' : ['유아'],
    '초등학교' : ['전체', '1학년', '2학년', '3학년', '4학년', '5학년', '6학년'],
    '중학교' : ['전체', '1학년', '2학년', '3학년'],
    '고등학교' : ['전체', '1학년', '2학년', '3학년'],
    '특수학교' : ['전체', '1학년', '2학년', '3학년', '4학년', '5학년', '6학년'],
    '기타학교' : ['전체', '1학년', '2학년', '3학년', '4학년', '5학년', '6학년'],
}

# 각 형태의 유니크값 가져오기
unique_school_levels = get_unique_accident_types('학교급')
unique_grades = get_unique_accident_types('사고자학년')
unique_accident = get_unique_accident_types('사고형태')
unique_accident_time = get_unique_accident_types('사고시간')
unique_accident_place = get_unique_accident_types('사고장소')
unique_accident_part = get_unique_accident_types('사고부위')
unique_accident_act= get_unique_accident_types('사고당시활동')
unique_accident_area = get_unique_accident_types('지역')

def menu():
    # Add header with icon
    st.sidebar.markdown("""
    <div style="text-align: center; padding: 20px 0;">
        <h2 style="color: #2C3E50; margin: 0;">🏫</h2>
        <h3 style="color: #2C3E50; margin: 0;">학교 안전사고 대시보드</h3>
        <hr style="margin: 10px 0;">
    </div>
    """, unsafe_allow_html=True)

    menu = st.sidebar.radio('📋 메뉴 선택', ['📊 차트 분석', '📋 사례 보기'])
    if menu == '📊 차트 분석':
        content_data = select_box_chart()
    else:
        st.sidebar.info("📋 사례 보기 기능은 준비 중입니다.")
        content_data = select_box_chart()  # 임시로 차트 데이터 반환

    return content_data

def select_box_chart():
    content_data = {}
    
    # School level selection
    st.sidebar.markdown("### 🏫 학교급 선택")
    school_level = st.sidebar.selectbox(
        '학교급을 선택하세요',
        unique_school_levels,
        key = 'school_level_select'
    )
    content_data['school_level'] = school_level

    # Grade selection
    st.sidebar.markdown("### 📚 학년 선택")
    school_grade_options = school_grades_category.get(school_level, [])
    school_grade = st.sidebar.selectbox(
        '학년을 선택하세요',
        school_grade_options,
        key='school_grade_select'
    )
    content_data['school_grade'] = school_grade

    # Accident type selection
    st.sidebar.markdown("### ⚠️ 사고 유형")
    accident_type = st.sidebar.selectbox(
        '사고 유형을 선택하세요',
        unique_accident,
    )
    content_data['accident_type'] = accident_type

    # Time selection
    st.sidebar.markdown("### 🕐 시간대")
    accident_time = st.sidebar.selectbox(
        '사고 발생 시간을 선택하세요',
        unique_accident_time
    )
    content_data['accident_time'] = accident_time

    # Place selection
    st.sidebar.markdown("### 🏢 장소")
    accident_place = st.sidebar.selectbox(
        '사고 발생 장소를 선택하세요',
        unique_accident_place
    )
    content_data['accident_place'] = accident_place

    # Body part selection
    st.sidebar.markdown("### 🦴 부위")
    accident_part = st.sidebar.selectbox(
        '사고 발생 부위를 선택하세요',
        unique_accident_part
    )
    content_data['accident_part'] = accident_part

    # Activity selection
    st.sidebar.markdown("### 🏃 당시 활동")
    accident_act = st.sidebar.selectbox(
        '사고 당시 활동을 선택하세요',
        unique_accident_act
    )
    content_data['accident_act'] = accident_act

    # Area selection
    st.sidebar.markdown("### 🗺️ 지역")
    accident_area = st.sidebar.selectbox(
        '사고 발생 지역을 선택하세요',
        unique_accident_area
    )
    content_data['accident_area'] = accident_area

    # Date range selection
    st.sidebar.markdown("### 📅 기간 설정")
    date_slider = st.sidebar.slider(
        '연도 범위를 선택하세요:', 
        min_value=data['연월'].min().year,
        max_value=data['연월'].max().year,
        value=(data['연월'].min().year, data['연월'].max().year), 
    )
    content_data['date_slider'] = date_slider

    start_date, end_date = st.sidebar.date_input(
        '정확한 날짜 범위를 선택하세요:',
        [pd.Timestamp(data['연월'].min()), pd.Timestamp(data['연월'].max())]
    )
    content_data['start_date'] = start_date
    content_data['end_date'] = end_date

    # Add a separator
    st.sidebar.markdown("---")
    
    # Add reset button
    if st.sidebar.button("🔄 필터 초기화", type="secondary"):
        st.rerun()

    return content_data