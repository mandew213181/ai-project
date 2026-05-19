import streamlit as st
import folium
from streamlit_folium import st_folium

# 1. 페이지 설정
st.set_page_config(
    page_title="Seoul Top 10 Tourist Attractions",
    page_icon="📌",
    layout="wide"
)

# 2. 타이틀 및 설명
st.title("🇰🇷 외국인이 좋아하는 서울 주요 관광지 Top 10")
st.markdown("외국인 관광객들에게 가장 인기 있는 서울의 명소 10곳을 지도에서 확인해 보세요!")

# 3. 서울 주요 관광지 Top 10 데이터 (명칭, 좌표, 설명)
attractions = [
    {"name": "경복궁 (Gyeongbokgung Palace)", "lat": 37.5796, "lng": 126.9770, "desc": "조선 왕조의 법궁이자 가장 웅장한 궁궐"},
    {"name": "N서울타워 (N Seoul Tower)", "lat": 37.5512, "lng": 126.9882, "desc": "남산 정상에서 서울 시내를 한눈에 내려다보는 전망대"},
    {"name": "명동 쇼핑거리 (Myeongdong)", "lat": 37.5635, "lng": 126.9846, "desc": "K-뷰티, 패션, 그리고 길거리 음식의 천국"},
    {"name": "북촌한옥마을 (Bukchon Hanok Village)", "lat": 37.5829, "lng": 126.9835, "desc": "실제 주민들이 거주하는 전통 한옥 보존 지역"},
    {"name": "인사동 (Insadong)", "lat": 37.5744, "lng": 126.9874, "desc": "한국의 전통 골동품, 필방, 전통 찻집이 모여있는 거리"},
    {"name": "홍대 거리 (Hongdae)", "lat": 37.5568, "lng": 126.9238, "desc": "젊은 예술가들의 버스킹과 트렌디한 클럽, 카페 문화의 중심지"},
    {"name": "광장시장 (Gwangjang Market)", "lat": 37.5701, "lng": 127.0010, "desc": "빈대떡, 육회 등 넷플릭스에도 소개된 유명 전통 먹거리 시장"},
    {"name": "동대문디자인플라자 (DDP)", "lat": 37.5668, "lng": 127.0094, "desc": "자하 하디드가 설계한 세계 최대 규모의 3차원 비정형 건축물"},
    {"name": "롯데월드타워 (Lotte World Tower)", "lat": 37.5126, "lng": 127.1025, "desc": "세계에서 5번째로 높은 빌딩이자 서울의 랜드마크"},
    {"name": "스타필드 코엑스몰 별마당도서관 (Starfield Library)", "lat": 37.5119, "lng": 127.0589, "desc": "코엑스몰 중심에 위치한 거대한 열린 문화 공간"}
]

# 4. 레이아웃 분할 (좌측: 리스트, 우측: 지도)
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📍 관광지 목록")
    # 사용자가 리스트에서 선택 시 지도 마커를 찾아갈 수 있도록 선택 박스 제공
    selected_place = st.selectbox("자세히 보고 싶은 명소를 선택하세요:", [p["name"] for p in attractions])
    
    # 선택된 명소의 상세 설명 출력
    for p in attractions:
        if p["name"] == selected_place:
            st.info(f"**{p['name']}**\n\n{p['desc']}")
            # 선택된 위치를 지도의 초기 중심점으로 설정하기 위함
            start_lat, start_lng = p["lat"], p["lng"]

# 5. Folium 지도 생성
# 선택된 명소가 있다면 그곳을 중심으로, 없다면 서울 중심부로 설정
m = folium.Map(location=[start_lat, start_lng], zoom_start=13, tiles="OpenStreetMap")

# 마커 추가
for p in attractions:
    popup_text = f"<b>{p['name']}</b><br>{p['desc']}"
    folium.Marker(
        location=[p["lat"], p["lng"]],
        popup=folium.Popup(popup_text, max_width=300),
        tooltip=p["name"],
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

# 6. 스트림릿 화면에 지도 렌더링
with col2:
    st.subheader("🗺️ 서울 관광 지도")
    st_folium(m, width="100%", height=600, returned_objects=[])
