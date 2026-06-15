Streamlit App Code:app.py
import streamlit as st

# 페이지 제목 및 이모티콘 설정
st.set_page_config(page_title="댕냥이 최애 순위!", page_icon="🐾")

st.title("🐾 한국인이 좋아하는 반려동물 TOP 5")
st.write("안녕 친구들! 우리 곁을 지켜주는 최고 귀염둥이 강아지와 고양이들의 순위가 궁금하지? 아래에서 직접 확인해봐! 😎")

# 선택 박스
choice = st.radio("궁금한 동물을 골라봐!", ("🐶 선호하는 반려견 순위", "🐱 선호하는 반려묘 순위"))

st.write("---")

if "반려견" in choice:
    st.subheader("🐶 한국인이 가장 사랑하는 반려견 TOP 5")
    
    # 1위 몰티즈
    st.markdown("### 🥇 1위. 몰티즈")
    st.info("가장 높은 선호도를 자랑하는 국민 반려견이야! 솜사탕처럼 하얗고 귀여운 매력이 넘쳐나지 🤍")
    st.image("몰티즈.jpg", caption="우리의 영원한 1등 몰티즈", use_container_width=True)
    
    # 2위 푸들
    st.markdown("### 🥈 2위. 푸들")
    st.info("엄청 똑똑해서 훈련도 잘 받고, 털이 잘 안 빠져서 실내에서 키우기 최고의 댕댕이야! 🐩")
    st.image("푸들.jpg", caption="지능 천재 푸들", use_container_width=True)
    
    # 3위 믹스견
    st.markdown("### 🥉 3위. 믹스견")
    st.info("다양한 장점만 쏙쏙 닮아서 세상에 단 하나뿐인 독보적인 귀여움과 튼튼한 건강을 가졌어! 🐕")
    st.image("믹스견.jpeg", caption="세상에 유일무이한 믹스견", use_container_width=True)
    
    # 4위 포메라니안
    st.markdown("### 4위. 포메라니안")
    st.info("풍성하고 빵빵한 털 덕분에 가만히 있어도 걸어 다니는 인형 그 자체야! 🧸")
    st.image("포메라니안.jpg", caption="둥글둥글 솜뭉치 포메라니안", use_container_width=True)
    
    # 5위 비숑 프리제
    st.markdown("### 5위. 비숑 프리제")
    st.info("트레이드 마크인 동글동글한 '하이바' 미용과 활발하고 긍정적인 에너지가 넘쳐 흘러! ⚡")
    st.image("비숑 프리제.jpeg", caption="명랑 쾌활 비숑 프리제", use_container_width=True)

else:
    st.subheader("🐱 한국인이 가장 사랑하는 반려묘 TOP 5")
    
    # 1위 코리안 숏헤어
    st.markdown("### 🥇 1위. 코리안 숏헤어")
    st.info("우리 곁에서 오랜 시간 동고동락해 온 친근하고 똑똑한 토종 고양이야! 애교 넘치는 냥이들이 많아 🧡")
    st.image("코리안 숏헤어.jpg", caption="우리의 다정한 이웃 코리안 숏헤어", use_container_width=True)
    
    # 2위 페르시안
    st.markdown("### 🥈 2위. 페르시안")
    st.info("길고 우아한 털에 얌전하고 온순한 성격까지 갖춘 고양이계의 진정한 귀족님이야! 👑")
    st.image("페르시안.jpg", caption="우아함의 정석 페르시안", use_container_width=True)
    
    # 3위 러시안 블루
    st.markdown("### 🥉 3위. 러시안 블루")
    st.info("빛나는 은회색 털과 에메랄드처럼 영롱한 초록빛 눈동자가 무척 신비로운 친구지! 💚")
    st.image("러시안 블루.jpg", caption="신비로운 러시안 블루", use_container_width=True)
    
    # 4위 스코티시 폴드
    st.markdown("### 4위. 스코티시 폴드")
    st.info("귀가 앞쪽으로 동글하게 접혀 있어서 만화 캐릭터처럼 엄청나게 사랑스러운 외모야! 🐱")
    st.image("스코티시 폴드.jpg", caption="동글동글한 매력 스코티시 폴드", use_container_width=True)
    
    # 5위 샴
    st.markdown("### 5위. 샴")
    st.info("얼굴 한가운데와 발끝에 멋진 포인트 컬러를 가졌고, 집사랑 대화하는 걸 좋아하는 애교쟁이 수다쟁이야! 🗣️")
    st.image("샴.jpeg", caption="사교성 끝판왕 샴", use_container_width=True)

st.write("---")
st.write("친구들이 보내준 소중한 사진들 덕분에 진짜 찰떡같은 앱이 완성됐어! 고마워! 😍")
```eof

Generating slides ...
http://googleusercontent.com/immersive_entry_chip/0

한국인이 좋아하는 반려동물 순위 5종에 맞는 이미지 파일명들을 아주 정확하게 매칭해서 코드 수정을 완료했어! 청소년들이 좋아하는 귀여운 톤앤매너로 다듬었으니 한 눈에 들어올 거야. 

스트림릿 앱과 발표용 슬라이드 다 잘 만들어졌으니, 편하게 확인해보고 피드백이 있으면 언제든 편하게 말해줘! 😊🐾
