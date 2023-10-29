import streamlit as st
from data_analysis.analysis import *
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd

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
    
    # Reset index to make 연월 a column
    chart_data = chart_data.reset_index()
    
    # Create beautiful interactive chart with Plotly
    fig = go.Figure()
    
    # Add traces with beautiful styling
    fig.add_trace(
        go.Scatter(
            x=chart_data['연월'],
            y=chart_data['전체 데이터'],
            mode='lines+markers',
            name='전체 데이터',
            line=dict(
                color='#FF6B6B',
                width=3,
                shape='spline'
            ),
            marker=dict(
                size=6,
                color='#FF6B6B',
                line=dict(width=2, color='white')
            ),
            fill='tonexty',
            fillcolor='rgba(255, 107, 107, 0.1)'
        )
    )
    
    fig.add_trace(
        go.Scatter(
            x=chart_data['연월'],
            y=chart_data['선택한 항목'],
            mode='lines+markers',
            name='선택한 항목',
            line=dict(
                color='#4ECDC4',
                width=3,
                shape='spline'
            ),
            marker=dict(
                size=6,
                color='#4ECDC4',
                line=dict(width=2, color='white')
            ),
            fill='tonexty',
            fillcolor='rgba(78, 205, 196, 0.1)'
        )
    )
    
    # Update layout for beautiful design
    fig.update_layout(
        title={
            'text': '📊 학교 안전사고 발생 추이',
            'x': 0.5,
            'xanchor': 'center',
            'font': {
                'size': 24,
                'color': '#2C3E50',
                'family': 'Arial, sans-serif'
            }
        },
        xaxis_title={
            'text': '📅 날짜',
            'font': {
                'size': 16,
                'color': '#34495E',
                'family': 'Arial, sans-serif'
            }
        },
        yaxis_title={
            'text': '📈 사고 발생 건수',
            'font': {
                'size': 16,
                'color': '#34495E',
                'family': 'Arial, sans-serif'
            }
        },
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family='Arial, sans-serif'),
        hovermode='x unified',
        hoverlabel=dict(
            bgcolor='white',
            font_size=12,
            font_family='Arial, sans-serif'
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='rgba(0,0,0,0.1)',
            borderwidth=1
        ),
        margin=dict(l=50, r=50, t=80, b=50),
        height=500
    )
    
    # Update axes styling
    fig.update_xaxes(
        gridcolor='rgba(128,128,128,0.2)',
        showgrid=True,
        zeroline=False,
        tickfont=dict(size=12, color='#7F8C8D')
    )
    
    fig.update_yaxes(
        gridcolor='rgba(128,128,128,0.2)',
        showgrid=True,
        zeroline=False,
        tickfont=dict(size=12, color='#7F8C8D')
    )
    
    # Display the chart
    st.plotly_chart(fig, use_container_width=True)
    
    # Add summary statistics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_accidents = chart_data['전체 데이터'].sum()
        st.metric(
            label="📊 총 사고 건수",
            value=f"{total_accidents:,}건",
            delta=None
        )
    
    with col2:
        selected_accidents = chart_data['선택한 항목'].sum()
        st.metric(
            label="🎯 선택 항목 건수",
            value=f"{selected_accidents:,}건",
            delta=None
        )
    
    with col3:
        avg_monthly = chart_data['전체 데이터'].mean()
        st.metric(
            label="📅 월평균 사고",
            value=f"{avg_monthly:.1f}건",
            delta=None
        )
    
    with col4:
        if total_accidents > 0:
            percentage = (selected_accidents / total_accidents) * 100
            st.metric(
                label="📈 비율",
                value=f"{percentage:.1f}%",
                delta=None
            )
        else:
            st.metric(
                label="📈 비율",
                value="0%",
                delta=None
            )
    