import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 1. 페이지 설정
st.set_page_config(
    page_title="국가별 & MBTI별 분포 분석기",
    page_icon="🌏",
    layout="centered"
)

# 2. 데이터 불러오기 함수
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

try:
    df = load_data()
except Exception as e:
    st.error(f"데이터 파일을 불러오지 못했습니다. 파일명(`countriesMBTI_16types.csv`)을 확인해주세요. 오류: {e}")
    st.stop()

# 3. 앱 타이틀
st.title("📊 글로벌 MBTI 데이터 시각화 대시보드")
st.markdown("국가별 MBTI 비율과 MBTI별 국가 순위를 한눈에 확인해 보세요.")

# 4. 탭 구성을 통해 두 가지 기능 분리
tab1, tab2 = st.tabs(["📌 국가별 MBTI 비율 조회", "🧬 MBTI별 국가 순위 (Top 10)"])

# 전체 16개 MBTI 유형 목록 추출
mbti_types = df.columns[1:]

# 그라데이션 색상 생성 함수 (1등: 노란색, 나머지: 초록색 그라데이션)
def get_gradient_colors(num_items):
    colors = []
    # 초록색 그라데이션 (진한 초록색 ForestGreen -> 연한 연두색/초록색)
    start_rgb = (34, 139, 34)    # #228B22 (ForestGreen)
    end_rgb = (220, 245, 220)    # 연한 파스텔 초록색
    
    for i in range(num_items):
        if i == 0:
            colors.append("#FFD700")  # 1등은 노란색 (Gold)
        else:
            # 2등부터 마지막 등수까지 색상 보간
            mix_ratio = (i - 1) / (num_items - 2) if num_items > 2 else 0
            r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * mix_ratio)
            g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * mix_ratio)
            b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * mix_ratio)
            colors.append(f"rgb({r}, {g}, {b})")
    return colors


# ==========================================
# TAB 1: 국가별 MBTI 비율 조회 (1등부터 정렬)
# ==========================================
with tab1:
    st.header("국가별 조회")
    countries = sorted(df["Country"].unique())
    selected_country = st.selectbox("분석할 국가를 선택하세요:", countries, key="country_select")
    
    # 선택된 국가 데이터 추출
    country_data = df[df["Country"] == selected_country].iloc[0]
    mbti_values = [country_data[mbti] for mbti in mbti_types]
    
    # 데이터프레임 빌드 후 1등부터 내림차순 정렬
    country_mbti_df = pd.DataFrame({
        "MBTI": mbti_types,
        "Percentage": mbti_values
    }).sort_values(by="Percentage", ascending=False).reset_index(drop=True)
    
    # 백분율 변환
    country_mbti_df["Percentage_pct"] = country_mbti_df["Percentage"] * 100
    
    # 그래프 그리기
    fig_country = go.Figure(data=[
        go.Bar(
            x=country_mbti_df["MBTI"],
            y=country_mbti_df["Percentage_pct"],
            marker_color=get_gradient_colors(len(country_mbti_df)),
            text=country_mbti_df["Percentage_pct"].round(2).astype(str) + "%",
            textposition='auto',
            hovertemplate="<b>%{x}</b><br>비율: %{y:.2f}%<extra></extra>"
        )
    ])
    
    fig_country.update_layout(
        title=f"<b>{selected_country}</b>의 MBTI 비율 순위 (1등부터)",
        xaxis_title="MBTI 유형",
        yaxis_title="비율 (%)",
        yaxis=dict(ticksuffix="%"),
        template="plotly_white",
        height=500
    )
    st.plotly_chart(fig_country, use_container_width=True)


# ==========================================
# TAB 2: MBTI별 국가 순위 조회 (Top 10)
# ==========================================
with tab2:
    st.header("MBTI별 국가 순위 (Top 10)")
    selected_mbti = st.selectbox("조회할 MBTI 유형을 선택하세요:", mbti_types, key="mbti_select")
    
    # 해당 MBTI 비율 기준으로 전체 국가 정렬 후 상위 10개 추출
    top10_countries = df[["Country", selected_mbti]].sort_values(
        by=selected_mbti, ascending=False
    ).head(10).reset_index(drop=True)
    
    # 백분율 변환
    top10_countries["Percentage_pct"] = top10_countries[selected_mbti] * 100
    
    # 그래프 그리기 (상위 10개 항목에 맞는 색상 부여)
    fig_mbti = go.Figure(data=[
        go.Bar(
            x=top10_countries["Country"],
            y=top10_countries["Percentage_pct"],
            marker_color=get_gradient_colors(len(top10_countries)),
            text=top10_countries["Percentage_pct"].round(2).astype(str) + "%",
            textposition='auto',
            hovertemplate="<b>%{x}</b><br>비율: %{y:.2f}%<extra></extra>"
        )
    ])
    
    fig_mbti.update_layout(
        title=f"전 세계 <b>{selected_mbti}</b> 비율이 가장 높은 국가 Top 10",
        xaxis_title="국가",
        yaxis_title="비율 (%)",
        yaxis=dict(ticksuffix="%"),
        template="plotly_white",
        height=500
    )
    st.plotly_chart(fig_mbti, use_container_width=True)
