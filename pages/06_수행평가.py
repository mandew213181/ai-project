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

    

    # 1위 말mport streamlit as st







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



    



    # 1위 말티즈

    st.markdown("### 🥇 1위. 몰티즈")

    st.caption("가장 높은 선호도를 자랑하는 국민 반려견!")

    st.image("https://mblogthumb-phinf.pstatic.net/MjAyMzA4MTZfMiAg/MDAxNjkyMTc2MjA2MjU0.rLjr0YZ1kJv8CjGOW2tAe75X5LsIIl2w5EPPyPi7AAog.ILw7MJVfhAZoXClRWcob8kv1eAnuUYztPHo6p0-COo0g.JPEG.dodoroong/%EB%A7%90%ED%8B%B0%EC%A6%88%EC%84%B1%EA%B2%A9.jpeg?type=w800)

    

    # 2위 푸들

    st.markdown("### 🥈 2위. 푸들")

    st.caption("지능이 높고 털 빠짐이 적어 인기 만점!")

    st.image("https://images.mypetlife.co.kr/content/uploads/2022/08/10155702/wonder-kim-D5_HAWtY0zE-unsplash-edited-scaled.jpg)

    

    # 3위 믹스견

    st.markdown("### 🥉 3위. 믹스견")

    st.caption("다양한 매력과 건강함으로 최근 인기가 급상승 중!")

    st.image("https://dimg.donga.com/wps/NEWS/IMAGE/2015/11/23/74957404.2.jpg)

    

    # 4위 포메라니안

    st.markdown("### 4위. 포메라니안")

    st.caption("풍성한 털과 인형 같은 외모의 소유자!")

    st.image("https://i.namu.wiki/i/M1M-NN0KXK4kVzVuRzh9k92Dk2WRIcJ_LMMG1qx6o7m-Sk7SH5yVC01omAsqI6Nz-lEtx_MBxHPdcHnAeaipwQ.webp)

    

    # 5위 비숑 프리제

    st.markdown("### 5위. 비숑 프리제")

    st.caption("하이바를 쓴 것 같은 뽀송뽀송한 매력!")   st.image("https://www.yomidog.com/preSaleUpFile/240328_%E1%84%80%E1%85%A1%E1%86%BC%E1%84%82%E1%85%A1%E1%86%B7%E1%84%91%E1%85%A9%E1%84%86%E1%85%A6_63864.png)



else:

    st.subheader("🐱 한국인이 선호하는 반려묘 TOP 5")

    

    # 1위 코리안 숏헤어

    st.markdown("### 🥇 1위. 코리안 숏헤어")

    st.caption("국내에서 가장 많이 기르는 친근한 우리 길냥이 친구들!")

    st.image("https://mblogthumb-phinf.pstatic.net/MjAyMjAxMDlfNjEg/MDAxNjQxNzMwNDg1ODk3.xxITnHXFfWuxtKGKhq0ikQ7yB7pqPXt0y6FAh_NUfkEg.SUcnfgww-0esgfNZ4Se6bJHhq1eEQwgaScMU0peNU4gg.JPEG.sofun123456/SE-e5a59d76-713e-11ec-a689-479cbb60a438.jpg?type=w800)

    

    # 2위 페르시안

    st.markdown("### 🥈 2위. 페르시안")

    st.caption("풍성한 털과 우아한 분위기를 풍기는 고양이!")

    st.image("https://cdn.imweb.me/upload/S20220518fbea59f8e9828/fead60c58f4fd.jpg)

    

    # 3위 러시안 블루

    st.markdown("### 🥉 3위. 러시안 블루")

    st.caption("신비로운 은회색 털과 초록색 눈이 매력적이야!")

    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgWxAaniE-VCDKPA0mJm_Y4IK2l-ddNu0pOQ&s)

    

    # 4위 스코티시 폴드

    st.markdown("### 4위. 스코티시 폴드")

    st.caption("접힌 귀가 동글동글해서 너무 귀여운 친구!")

    st.image("https://img.segye.com/content/image/2017/05/11/20170511514641.jpg)

    

    # 5위 샴

    st.markdown("### 5위. 샴")

    st.caption("얼굴과 발끝의 포인트 색상이 멋진 수다쟁이 고양이!")

    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQsnK8K2QdswBWyvyi1nZb_1V_WtIRFvK9BZw&s)
