import streamlit as st

# 페이지 제목 설정 (귀여운 이모티콘은 필수!)
st.set_page_config(page_title="최애 반려동물 순위 TOP 5", page_icon="🐾")

st.title("🐾 한국인이 사랑하는 반려견 & 반려묘 TOP 5")
st.write("친구들 안녕! 한국 사람들에게 가장 사랑받는 댕댕이와 냥냥이 순위가 궁금하지? 아래에서 하나를 골라봐! 👇")

# 1. 반려견/반려묘 선택 라디오 버튼
choice = st.radio(
    "어떤 동물의 순위가 보고 싶어?",
    ("🐶 선호하는 반려견 순위", "🐱 선호하는 반려묘 순위")
)

st.write("---") # 구분선

# 2. 선택에 따른 조건문 처리
if "반려견" in choice:
    st.subheader("🐶 한국인이 선호하는 반려견 TOP 5")
    
    # 1위 몰티즈
    st.markdown("### 🥇 1위. 몰티즈")
    st.caption("가장 높은 선호도를 자랑하는 국민 반려견!")
    st.image("https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?q=80&w=600&auto=format&fit=crop", caption="귀염뽀짝 몰티즈", use_container_width=True)
    
    # 2위 푸들
    st.markdown("### 🥈 2위. 푸들")
    st.caption("지능이 높고 털 빠짐이 적어 인기 만점!")
    st.image("https://images.unsplash.com/photo-1591382589366-267b9477169d?q=80&w=600&auto=format&fit=crop", caption="똑똑이 푸들", use_container_width=True)
    
    # 3위 믹스견
    st.markdown("### 🥉 3위. 믹스견")
    st.caption("다양한 매력과 건강함으로 최근 인기가 급상승 중!")
    st.image("https://images.unsplash.com/photo-1543466835-00a7907e9de1?q=80&w=600&auto=format&fit=crop", caption="매력 만점 믹스견", use_container_width=True)
    
    # 4위 포메라니안
    st.markdown("### 4위. 포메라니안")
    st.caption("풍성한 털과 인형 같은 외모의 소유자!")
    st.image("https://images.unsplash.com/photo-1598134493179-51332e56807f?q=80&w=600&auto=format&fit=crop", caption="솜뭉치 포메라니안", use_container_width=True)
    
    # 5위 비숑 프리제
    st.markdown("### 5위. 비숑 프리제")
    st.caption("하이바를 쓴 것 같은 뽀송뽀송한 매력!")
    st.image("https://images.unsplash.com/photo-1604916287784-c324202b3205?q=80&w=600&auto=format&fit=crop", caption="동글동글 비숑 프리제", use_container_width=True)

else:
    st.subheader("🐱 한국인이 선호하는 반려묘 TOP 5")
    
    # 1위 코리안 숏헤어
    st.markdown("### 🥇 1위. 코리안 숏헤어")
    st.caption("국내에서 가장 많이 기르는 친근한 우리 길냥이 친구들!")
    st.image("https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?q=80&w=600&auto=format&fit=crop", caption="친근한 코숏", use_container_width=True)
    
    # 2위 페르시안
    st.markdown("### 🥈 2위. 페르시안")
    st.caption("풍성한 털과 우아한 분위기를 풍기는 고양이!")
    st.image("https://images.unsplash.com/photo-1618826411640-d6df44dd3f7a?q=80&w=600&auto=format&fit=crop", caption="우아한 페르시안", use_container_width=True)
    
    # 3위 러시안 블루
    st.markdown("### 🥉 3위. 러시안 블루")
    st.caption("신비로운 은회색 털과 초록색 눈이 매력적이야!")
    st.image("https://images.unsplash.com/photo-1592194996308-7b43878e84a6?q=80&w=600&auto=format&fit=crop", caption="매혹적인 러시안 블루", use_container_width=True)
    
    # 4위 스코티시 폴드
    st.markdown("### 4위. 스코티시 폴드")
    st.caption("접힌 귀가 동글동글해서 너무 귀여운 친구!")
    st.image("https://images.unsplash.com/photo-1574158622672-b690351a1f6d?q=80&w=600&auto=format&fit=crop", caption="귀여운 스코티시 폴드", use_container_width=True)
    
    # 5위 샴
    st.markdown("### 5위. 샴")
    st.caption("얼굴과 발끝의 포인트 색상이 멋진 수다쟁이 고양이!")
    st.image("https://images.unsplash.com/photo-1557246565-8a3d3ab5d7f6?q=80&w=600&auto=format&fit=crop", caption="매력쟁이 샴", use_container_width=True)
