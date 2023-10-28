import pandas as pd
import numpy as np

file_path = './dashboard_data/1. (raw) 사고 발생 데이터_수정.xlsx'  # 실제 엑셀 파일 경로로 변경해주세요.
cols = ['학교명', '지역', '교육청', '설립유형', '학교급', '사고자구분', '사고자성별', '사고자학년', 
        '사고접수일', '사고발생일', '사고발생요일', '사고발생시간', '사고시간', '사고장소', 
        '사고부위', '사고형태', '사고매개물', '사고당시활동']

# 시트 이름별로 데이터 가져오기
data_2020 = pd.read_excel(file_path, sheet_name='2020(수정)', usecols=cols)
data_2021 = pd.read_excel(file_path, sheet_name='2021', usecols=cols)
data_2022 = pd.read_excel(file_path, sheet_name='2022', usecols=cols)

data = pd.concat([data_2020, data_2021, data_2022], ignore_index=True)

data['학교급'] = data['학교급'].replace({
    '유': '유치원',
    '초': '초등학교',
    '중': '중학교',
    '고': '고등학교',
    '특수': '특수학교',
    '기타': '기타학교'
})
print("2222")
data['사고발생일'] = pd.to_datetime(data['사고발생일'])    # '사고발생일'을 datetime 형식으로 변환
data['연월'] = pd.to_datetime(data['사고발생일'].dt.strftime('%Y-%m'))
data['연도'] = data['사고발생일'].dt.year    # 연도 추출

def date_accident_count():
    # 연도와 월만 추출하여 새로운 문자열 생성 후 다시 datetime 형식으로 변환
    data['연월'] = pd.to_datetime(data['사고발생일'].dt.strftime('%Y-%m'))

    filtered_data = data[data['사고발생일'].dt.year >= 2019]    # 2019년 이후의 데이터만 선택

    # 2019년 이후의 데이터의 월별 사고 수 계산
    monthwise_accident_counts = filtered_data.groupby('연월').size().reset_index(name='사고수')

    return monthwise_accident_counts

def get_unique_accident_types(column):    # 사고형태 dropdown만들기 위함
    return_data = data[column].dropna().unique().tolist()
    return_data = np.append(['전체'], return_data)
    return return_data

def total_line_chart_data(selected_content):
    start_year, end_year = selected_content['date_slider']
    mask = (
        (data['연월'] >= pd.Timestamp(selected_content['start_date']))
        & (data['연월'] <= pd.Timestamp(selected_content['end_date']))
        & (data['연월'].dt.year >= start_year)
        & (data['연월'].dt.year <= end_year)
    )
    filtered_data = data[mask]
    filtered_data = filtered_data.groupby('연월').size().reset_index(name='사고수')
    filtered_data = filtered_data[['연월', '사고수']]
    
    return filtered_data

def content_line_chart_data(select_content):
    mask = custum_mask(select_content) 
    filtered_data = data[mask]
    filtered_data = filtered_data.groupby('연월').size().reset_index(name='사고수')
    filtered_data = filtered_data[['연월', '사고수']]
    return filtered_data

def custum_mask(selected_content):
    start_year, end_year = selected_content['date_slider']

    custum_mask = (
        (data['연월'] >= pd.Timestamp(selected_content['start_date']))
        & (data['연월'] <= pd.Timestamp(selected_content['end_date']))
        & (data['연월'].dt.year >= start_year)
        & (data['연월'].dt.year <= end_year)
    )

    if selected_content['school_level'] != "전체":  # 학교급 선택 시
        custum_mask = custum_mask & (data['학교급'] == selected_content['school_level'])
    if selected_content['school_grade'] != "전체":  # 학년 선택 시
        custum_mask = custum_mask & (data['사고자학년'] == selected_content['school_grade'])
    if selected_content['accident_type'] != "전체":
        custum_mask = custum_mask & (data['사고형태'] == selected_content['accident_type'])
    if selected_content['accident_time'] != "전체":
        custum_mask = custum_mask & (data['사고시간'] == selected_content['accident_time'])
    if selected_content['accident_place'] != "전체":
        custum_mask = custum_mask & (data['사고장소'] == selected_content['accident_place'])
    if selected_content['accident_part'] != "전체":
        custum_mask = custum_mask & (data['사고부위'] == selected_content['accident_part'])
    if selected_content['accident_act'] != "전체":
        custum_mask = custum_mask & (data['사고당시활동'] == selected_content['accident_act'])
    if selected_content['accident_area'] != "전체":
        custum_mask = custum_mask & (data['지역'] == selected_content['accident_area'])

    return custum_mask