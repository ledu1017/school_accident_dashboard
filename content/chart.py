import streamlit as st
from data_analysis.analysis import *
import matplotlib.pyplot as plt

def line_chart(selected_content):
    # Entire data
    entire_data = total_line_chart_data(selected_content)
    entire_line = entire_data.groupby('연월').size()

    # Filtered data based on user's selection
    filtered_data = content_line_chart_data(selected_content)
    filtered_line = filtered_data.groupby('연월').size()

    chart_data = pd.DataFrame({
        '전체 데이터': entire_line,
        '선택한 항목': filtered_line
    }).fillna(0)

    # Plotting using matplotlib
    plt.figure(figsize=(10, 6))
    plt.plot(chart_data['전체 데이터'], color='red', label='Total')
    plt.plot(chart_data['선택한 항목'], color='blue', label='Selected')
    plt.legend()
    plt.title("Date Accident")
    plt.xlabel("Date")
    plt.ylabel("Date_Accident")
    st.pyplot(plt)
    