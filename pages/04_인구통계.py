import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os
import urllib.request
import re

# 페이지 기본 설정
st.set_page_config(page_title="연령별 인구수 분석", layout="wide")
st.title("행정구역별 연령 인구수 분석")

# 1. 스트림릿 클라우드 환경을 위한 한글 폰트 자동 다운로드 및 설정
@st.cache_data
def load_korean_font():
    # 구글 폰트 저장소에서 나눔고딕 다운로드
    font_url = "https://github.com/google/fonts/raw/main/ofl/nanumgothic/NanumGothic-Regular.ttf"
    font_path = "NanumGothic-Regular.ttf"
    
    if not os.path.exists(font_path):
        urllib.request.urlretrieve(font_url, font_path)
    return font_path

try:
    font_path = load_korean_font()
    font_prop = fm.FontProperties(fname=font_path)
    font_name = font_prop.get_name()
    
    # Matplotlib 전역 폰트 설정
    plt.rc('font', family=font_name)
    # 마이너스 기호 깨짐 방지
    plt.rcParams['axes.unicode_minus'] = False
except Exception as e:
    st.warning(f"한글 폰트 로드 중 오류가 발생했습니다: {e}")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv('population.csv')
    return df

try:
    df = load_data()
    
    # 2. 행정구역 선택창
    district = st.selectbox("행정구역을 선택하세요:", df['행정구역'].unique())
    
    if district:
        # 선택한 행정구역의 데이터 추출
        row = df[df['행정구역'] == district].iloc[0]
        
        # 연령별 세부 인구 컬럼만 필터링
        age_cols = [col for col in df.columns if '거주자_' in col and '총인구수' not in col and '연령구간인구수' not in col]
        
        ages = []
        populations = []
        
        # 3. 데이터 전처리 (콤마 제거 및 숫자 변환)
        for col in age_cols:
            age_str = col.split('거주자_')[-1]
            
            if '이상' in age_str:
                age_num = 100
            else:
                age_num = int(re.sub(r'[^0-9]', '', age_str))
                
            pop_num = int(str(row[col]).replace(',', ''))
            
            ages.append(age_num)
            populations.append(pop_num)
            
        # 4. 꺾은선 그래프 그리기 (Matplotlib)
        fig, ax = plt.subplots(figsize=(12, 5))
        
        # 핫핑크 색상 지정
        ax.plot(ages, populations, color='hotpink', linewidth=2, marker='o', markersize=3)
        
        # 그래프 제목 및 축 레이블 설정 (폰트 프로퍼티 명시)
        ax.set_title(f"[{district}] 연령별 인구 분포", fontsize=14, fontweight='bold', fontproperties=font_prop, pad=15)
        ax.set_xlabel("나이 (세)", fontsize=11, fontproperties=font_prop)
        ax.set_ylabel("인구수 (명)", fontsize=11, fontproperties=font_prop)
        
        # 5. 가로축 10살 단위 설정 및 세로 구분선(Grid) 추가
        max_age = max(ages) if ages else 100
        ax.set_xticks(range(0, max_age + 1, 10))
        ax.grid(True, axis='x', linestyle='--', alpha=0.5, color='gray')
        
        # 스트림릿 화면에 그래프 출력
        st.pyplot(fig)
        
except FileNotFoundError:
    st.error("'population.csv' 파일이 같은 폴더에 있어야 합니다. 깃허브 레포지토리에 파일을 함께 올려주세요.")
