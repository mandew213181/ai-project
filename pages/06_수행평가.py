import streamlit as st

# 페이지 설정
st.set_page_config(page_title="댕냥이 순위 정복!", page_icon="🐾")

# 제목이랑 인사말
st.title("🐶🐱 한국인이 좋아하는 반려동물 TOP 5")
st.write("안녕 친구들! 이번엔 진짜 '찰떡' 같은 사진들로 다시 준비했어. 궁금한 동물을 골라봐! ✨")

# 선택창
choice = st.radio("어떤 친구들이 궁금해?", ("🐶 반려견 순위", "🐱 반려묘 순위"))

st.write("---")

if choice == "🐶 반려견 순위":
    st.subheader("🐶 한국인 선호 반려견 TOP 5")
    
    # 1위 몰티즈
    st.markdown("### 🥇 1위. 몰티즈")
    st.info("가장 높은 선호도를 자랑하는 국민 반려견!")
    st.image("https://images.unsplash.com/photo-1537151608828-ea2b11777ee8?q=80&w=800&auto=format&fit=crop", caption="하얀 천사 몰티즈", use_container_width=True)
    
    # 2위 푸들
    st.markdown("### 🥈 2위. 푸들")
    st.info("지능이 높고 털 빠짐이 적어서 인기가 정말 많아!")
    st.image("https://images.unsplash.com/photo-1516734212186-a967f81ad0d7?q=80&w=800&auto=format&fit=crop", caption="똑똑한 푸들", use_container_width=True)
    
    # 3위 믹스견
    st.markdown("### 🥉 3위. 믹스견")
    st.info("세상에 하나뿐인 매력과 튼튼한 건강함!")
    st.image("https://images.unsplash.com/photo-1543466835-00a7907e9de1?q=80&w=800&auto=format&fit=crop", caption="매력 만점 믹스견", use_container_width=True)
    
    # 4위 포메라니안
    st.markdown("### 4위. 포메라니안")
    st.info("복슬복슬한 털과 인형 같은 외모!")
    st.image("https://images.unsplash.com/photo-1587300003388-59208cc962cb?q=80&w=800&auto=format&fit=crop", caption="솜사탕 포메라니안", use_container_width=True)
    
    # 5위 비숑 프리제
    st.markdown("### 5위. 비숑 프리제")
    st.info("동글동글한 '하이바' 컷이 매력적인 친구!")
    st.image("https://images.unsplash.com/photo-1604916287784-c324202b3205?q=80&w=800&auto=format&fit=crop", caption="보송보송 비숑 프리제", use_container_width=True)

else:
    st.subheader("🐱 한국인 선호 반려묘 TOP 5")
    
    # 1위 코리안 숏헤어
    st.markdown("### 🥇 1위. 코리안 숏헤어")
    st.info("우리 주변에서 가장 흔히 볼 수 있는 친근한 길냥이 친구들!")
    st.image("https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?q=80&w=800&auto=format&fit=crop", caption="친근한 코숏", use_container_width=True)
    
    # 2위 페르시안
    st.markdown("### 🥈 2위. 페르시안")
    st.info("우아하고 긴 털이 특징인 고양이계의 귀족!")
    st.image("https://images.unsplash.com/photo-1618826411640-d6df44dd3f7a?q=80&w=800&auto=format&fit=crop", caption="우아한 페르시안", use_container_width=True)
    
    # 3위 러시안 블루
    st.markdown("### 🥉 3위. 러시안 블루")
    st.info("신비로운 회색 털과 초록색 눈이 정말 매력적이야.")
    st.image("https://images.unsplash.com/photo-1592194996308-7b43878e84a6?q=80&w=800&auto=format&fit=crop", caption="신비로운 러시안 블루", use_container_width=True)
    
    # 4위 스코티시 폴드
    st.markdown("### 4위. 스코티시 폴드")
    st.info("귀가 쏙 접혀서 얼굴이 동글동글해 보이는 게 포인트!")
    st.image("https://images.unsplash.com/photo-1574158622672-b690351a1f6d?q=80&w=800&auto=format&fit=crop", caption="동글이 스코티시 폴드", use_container_width=True)
    
    # 5위 샴
    st.markdown("### 5위. 샴")
    st.info("얼굴과 발에 포인트 색상이 있는 수다쟁이 고양이!")
    st.image("https://images.unsplash.com/photo-1557246565-8a3d3ab5d7f6?q=80&w=800&auto=format&fit=crop", caption="포인트가 매력적인 샴", use_container_width=True)

st.write("---")
st.write("도움이 됐길 바라! 궁금한 게 더 있으면 언제든 물어봐줘! 😊")
