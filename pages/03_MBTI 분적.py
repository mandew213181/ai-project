import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 1. 페이지 설정
st.set_page_config(
    page_title="국가별 MBTI 분포 분석기",
    page_icon="📊",
    layout="centered"
)

# 2. 데이터 불러오기 함수 (캐싱 적용으로 속도 향상)
@st.cache_data
def load_data():
    # 데이터셋 로드 (데이터 파일이 스크립트와 같은 경로에 있다고 가정)
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

try:
    df = load_data()
except Exception as e:
    st.error(f"데이터 파일을 불러오지 못했습니다. 파일명(`countriesMBTI_16types.csv`)을 확인해주세요. 오류: {e}")
    st.stop()

# 3. 앱 타이틀 및 설명
st.title("🌏 국가별 MBTI 비율 시각화 대시보드")
st.markdown("원하는 국가를 선택하면 16가지 MBTI 성격 유형의 분포 비율을 확인할 수 있습니다.")

# 4. 국가 선택 셀렉트박스
countries = sorted(df["Country"].unique())
selected_country = st.selectbox("분석할 국가를 선택하세요:", countries)

# 5. 선택된 국가의 데이터 추출 및 정렬
country_data = df[df["Country"] == selected_country].iloc[0]

# 국가 이름 제외한 MBTI 유형과 비율만 추출
mbti_types = df.columns[1:]  # 'Country'를 제외한 컬럼들
mbti_values = [country_data[mbti] for mbti in mbti_types]

# 데이터프레임으로 변환 후 비율 기준 내림차순(높은 순) 정렬
mbti_df = pd.DataFrame({
    "MBTI": mbti_types,
    "Percentage": mbti_values
}).sort_values(by="Percentage", ascending=False).reset_index(drop=True)

# 백분율(%) 표기를 위해 100을 곱함
mbti_df["Percentage_pct"] = mbti_df["Percentage"] * 100

# 6. 요청에 따른 조건별 색상 지정 (1등: 노란색, 나머지: 하늘색 그라데이션)
# 총 16개 유형이므로 1등을 제외한 15개 유형에 대해 하늘색(#00BFFF)에서 흐린 하늘색(#E0F7FA)으로 연해지는 그라데이션 컬럼 생성
num_items = len(mbti_df)
colors = []

# RGB 값 기준 그라데이션 계산 (진한 하늘색 DeepSkyBlue -> 매우 연한 하늘색)
start_rgb = (0, 191, 255)   # #00BFFF (DeepSkyBlue)
end_rgb = (224, 247, 250)   # #E0F7FA (Light Cyan)

for i in range(num_items):
    if i == 0:
        # 1등은 확연히 눈에 띄는 진한 노란색 (Gold)
        colors.append("#FFD700")
    else:
        # 2등(index 1)부터 마지막 등수(index 15)까지 보간(Interpolation) 비율 계산
        mix_ratio = (i - 1) / (num_items - 2) if num_items > 2 else 0
        r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * mix_ratio)
        g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * mix_ratio)
        b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * mix_ratio)
        colors.append(f"rgb({r}, {g}, {b})")

# 7. Plotly 막대그래프 그리기
fig = go.Figure(data=[
    go.Bar(
        x=mbti_df["MBTI"],
        y=mbti_df["Percentage_pct"],
        marker_color=colors,
        text=mbti_df["Percentage_pct"].round(2).astype(str) + "%", # 막대 위에 수치 표시
        textposition='auto',
        hovertemplate="<b>%{x}</b><br>비율: %{y:.2f}%<extra></extra>"
    )
])

fig.update_layout(
    title=f"<b>{selected_country}</b>의 MBTI 성격 유형 분포 (높은 순)",
    xaxis_title="MBTI 유형",
    yaxis_title="비율 (%)",
    yaxis=dict(ticksuffix="%"),
    template="plotly_white",
    margin=dict(l=40, r=40, t=60, b=40),
    height=500
)

# 8. 스트림릿 화면에 그래프 및 요약 출력
st.plotly_chart(fig, use_container_width=True)

# 요약 정보 카드 형태로 보여주기
st.markdown(f"### 💡 {selected_country} 분석 요약")
col1, col2 = st.columns(2)
with col1:
    st.success(f"**가장 많은 유형 (1위):** {mbti_df.iloc[0]['MBTI']} ({mbti_df.iloc[0]['Percentage_pct']:.2f}%)")
with col2:
    st.warning(f"**가장 희귀한 유형 (16위):** {mbti_df.iloc[-1]['MBTI']} ({mbti_df.iloc[-1]['Percentage_pct']:.2f}%)")
