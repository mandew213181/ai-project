import streamlit as st
import pandas as pd
import plotly.express as px
import re

# 페이지 기본 설정
st.set_page_config(page_title="연령별 인구수 분석", layout="wide")
st.title("행정구역별 연령 인구수 분석")

# 데이터 불러오기 (캐싱을 통해 속도 향상)
@st.cache_data
def load_data():
    df = pd.read_csv('population.csv')
    return df

try:
    df = load_data()
    
    # 1. 행정구역 선택창
    district = st.selectbox("행정구역을 선택하세요:", df['행정구역'].unique())
    
    if district:
        # 2. 선택한 행정구역의 데이터만 추출
        row = df[df['행정구역'] == district].iloc[0]
        
        # '거주자_'가 포함된 나이 컬럼만 필터링 (총인구수 등 제외)
        age_cols = [col for col in df.columns if '거주자_' in col and '총인구수' not in col and '연령구간인구수' not in col]
        
        ages = []
        populations = []
        
        # 3. 데이터 전처리 (콤마 제거, 숫자 변환)
        for col in age_cols:
            # 컬럼명에서 나이 숫자만 추출 (예: '2026년04월_거주자_0세' -> 0)
            age_str = col.split('거주자_')[-1]
            
            if '이상' in age_str:
                age_num = 100 # '100세 이상'은 그래프 X축을 위해 100으로 표기
            else:
                age_num = int(re.sub(r'[^0-9]', '', age_str))
                
            # 인구수에 포함된 콤마(,) 제거 후 정수로 변환
            pop_str = str(row[col]).replace(',', '')
            pop_num = int(pop_str)
            
            ages.append(age_num)
            populations.append(pop_num)
            
        # 그래프용 데이터프레임 생성
        plot_df = pd.DataFrame({
            '나이': ages,
            '인구수': populations
        })
        
        # 4. Plotly를 활용한 꺾은선 그래프 생성 (한글 깨짐 없음)
        fig = px.line(
            plot_df, 
            x='나이', 
            y='인구수', 
            color_discrete_sequence=['hotpink'] # 핫핑크 색상 적용
        )
        
        # 5. 가로축 10살 단위 구분선 및 레이블 설정
        fig.update_xaxes(
            dtick=10,
            title_text='나이 (세)'
        )
        fig.update_yaxes(title_text='인구수 (명)')
        
        # 화면에 그래프 출력
        st.plotly_chart(fig, use_container_width=True)
        
except FileNotFoundError:
    st.error("'population.csv' 파일이 같은 경로에 존재하지 않습니다. GitHub 레포지토리에 데이터 파일을 함께 업로드해주세요.")
