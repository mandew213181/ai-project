import base64
import streamlit as st

# 페이지 제목 및 이모티콘 설정
st.set_page_config(page_title="댕냥이 최애 순위!", page_icon="🐾")

st.title("🐾 한국인이 좋아하는 반려동물 TOP 5")
st.write("안녕 친구들! 우리 곁을 지켜주는 최고 귀염둥이 강아지와 고양이들의 순위가 궁금하지? 아래에서 직접 확인해봐! 😎")

# 선택 박스
choice = st.radio("궁금한 동물을 골라봐!", ("🐶 선호하는 반려견 순위", "🐱 선호하는 반려묘 순위"))

st.write("---")

# [보안 및 에러 방지] 로컬 파일 경로 문제를 해결하기 위한 안전한 이미지 로드 함수
def load_image(file_name):
    """
    스트림릿 클라우드의 경로 에러(MediaFileStorageError)를 방지하기 위해
    상대 경로와 pages/ 경로를 둘 다 찾아보고 안전하게 불러오는 함수야!
    """
    import os
    # 1. 일반적인 현재 폴더 경로 확인
    if os.path.exists(file_name):
        return file_name
    # 2. pages 폴더 하위에 있을 경우를 대비한 경로 확인
    possible_path = os.path.join("pages", file_name)
    if os.path.exists(possible_path):
        return possible_path
    
    # 3. 만약 파일이 정말 없을 때 에러로 앱이 터지는 걸 막기 위한 예외 처리!
    return None

if "반려견" in choice:
    st.subheader("🐶 한국인이 가장 사랑하는 반려견 TOP 5")
    
    # 1위 몰티즈
    st.markdown("### 🥇 1위. 몰티즈")
    st.info("가장 높은 선호도를 자랑하는 국민 반려견이야! 솜사탕처럼 하얗고 귀여운 매력이 넘쳐나지 🤍")
    img = load_image("몰티즈.jpg")
    if img: st.image(img, caption="우리의 영원한 1등 몰티즈", use_container_width=True)
    else: st.warning("⚠️ '몰티즈.jpg' 파일을 찾을 수 없어! 깃허브 저장소에 파일이 잘 올라갔는지 확인해줘.")
    
    # 2위 푸들
    st.markdown("### 🥈 2위. 푸들")
    st.info("엄청 똑똑해서 훈련도 잘 받고, 털이 잘 안 빠져서 실내에서 키우기 최고의 댕댕이야! 🐩")
    img = load_image("푸들.jpg")
    if img: st.image(img, caption="지능 천재 푸들", use_container_width=True)
    else: st.warning("⚠️ '푸들.jpg' 파일을 찾을 수 없어!")
    
    # 3위 믹스견
    st.markdown("### 🥉 3위. 믹스견")
    st.info("다양한 장점만 쏙쏙 닮아서 세상에 단 하나뿐인 독보적인 귀여움과 튼튼한 건강을 가졌어! 🐕")
    img = load_image("믹스견.jpeg")
    if img: st.image(img, caption="세상에 유일무이한 믹스견", use_container_width=True)
    else: st.warning("⚠️ '믹스견.jpeg' 파일을 찾을 수 없어!")
    
    # 4위 포메라니안
    st.markdown("### 4위. 포메라니안")
    st.info("풍성하고 빵빵한 털 덕분에 가만히 있어도 걸어 다니는 인형 그 자체야! 🧸")
    img = load_image("포메라니안.jpg")
    if img: st.image(img, caption="둥글둥글 솜뭉치 포메라니안", use_container_width=True)
    else: st.warning("⚠️ '포메라니안.jpg' 파일을 찾을 수 없어!")
    
    # 5위 비숑 프리제
    st.markdown("### 5위. 비숑 프리제")
    st.info("트레이드 마크인 동글동글한 '하이바' 미용과 활발하고 긍정적인 에너지가 넘쳐 흘러! ⚡")
    img = load_image("비숑 프리제.jpeg")
    if img: st.image(img, caption="명랑 쾌활 비숑 프리제", use_container_width=True)
    else: st.warning("⚠️ '비숑 프리제.jpeg' 파일을 찾을 수 없어!")

else:
    st.subheader("🐱 한국인이 가장 사랑하는 반려묘 TOP 5")
    
    # 1위 코리안 숏헤어
    st.markdown("### 🥇 1위. 코리안 숏헤어")
    st.info("우리 곁에서 오랜 시간 동고동락해 온 친근하고 똑똑한 토종 고양이야! 애교 넘치는 냥이들이 많아 🧡")
    img = load_image("코리안 숏헤어.jpg")
    if img: st.image(img, caption="우리의 다정한 이웃 코리안 숏헤어", use_container_width=True)
    else: st.warning("⚠️ '코리안 숏헤어.jpg' 파일을 찾을 수 없어!")
    
    # 2위 페르시안
    st.markdown("### 🥈 2위. 페르시안")
    st.info("길고 우아한 털에 얌전하고 온순한 성격까지 갖춘 고양이계의 진정한 귀족님이야! 👑")
    img = load_image("페르시안.jpg")
    if img: st.image(img, caption="우아함의 정석 페르시안", use_container_width=True)
    else: st.warning("⚠️ '페르시안.jpg' 파일을 찾을 수 없어!")
    
    # 3위 러시안 블루
    st.markdown("### 🥉 3위. 러시안 블루")
    st.info("빛나는 은회색 털과 에메랄드처럼 영롱한 초록빛 눈동자가 무척 신비로운 친구지! 💚")
    img = load_image("러시안
