import streamlit as st
import numpy as np
from data_analysis.analysis import *

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

    menu = st.sidebar.radio('메뉴', ['차트', '사례'])
    if menu == '차트':
        content_data = select_box_chart()

    return content_data

def select_box_chart():
    content_data = {}
    school_level = st.sidebar.selectbox(
        '학교급',
        unique_school_levels,
        key = 'school_level_select'
    )
    content_data['school_level'] = school_level

    school_grade_options = school_grades_category.get(school_level, [])
    school_grade = st.sidebar.selectbox(
        '학년',
        school_grade_options,
        key='school_grade_select'
    )
    content_data['school_grade'] = school_grade

    accident_type = st.sidebar.selectbox(
        '사고 유형',
        unique_accident,
    )
    content_data['accident_type'] = accident_type

    accident_time = st.sidebar.selectbox(
        '시간',
        unique_accident_time
    )
    content_data['accident_time'] = accident_time

    accident_place = st.sidebar.selectbox(
        '장소',
        unique_accident_place
    )
    content_data['accident_place'] = accident_place

    accident_part = st.sidebar.selectbox(
        '부위',
        unique_accident_part
    )
    content_data['accident_part'] = accident_part

    accident_act = st.sidebar.selectbox(
        '당시 활동',
        unique_accident_act
    )
    content_data['accident_act'] = accident_act

    accident_area = st.sidebar.selectbox(
        '사고 지역',
        unique_accident_area
    )
    content_data['accident_area'] = accident_area

    date_slider = st.sidebar.slider(
        '기간 설정:', 
        min_value=data['연월'].min().year,
        max_value=data['연월'].max().year,
        value=(data['연월'].min().year, data['연월'].max().year), 
    )
    content_data['date_slider'] = date_slider

    start_date, end_date = st.sidebar.date_input(
        '날짜 범위 선택:',
        [pd.Timestamp(data['연월'].min()), pd.Timestamp(data['연월'].max())]
    )
    content_data['start_date'] =start_date
    content_data['end_date'] =end_date

    return content_data