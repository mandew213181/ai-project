import streamlit as st

st.set_page_config(
    page_title="반려동물 인기 순위",
    page_icon="🐾",
    layout="wide"
)

st.title("🐾 한국인이 좋아하는 반려동물 순위")
st.write("궁금한 반려동물을 골라보자! 😎")

animal = st.radio(
    "무엇이 궁금해?",
    ["🐶 반려견", "🐱 반려묘"],
    horizontal=True
)

dogs = [
    {
        "rank": "1위",
        "name": "몰티즈",
        "desc": "가장 높은 선호도를 자랑하는 국민 반려견!",
        "image": "https://images.unsplash.com/photo-1591769225440-811ad7d6eab2?w=800"
    },
    {
        "rank": "2위",
        "name": "푸들",
        "desc": "지능이 높고 털 빠짐이 적어 인기 만점!",
        "image": "https://images.unsplash.com/photo-1517849845537-4d257902454a?w=800"
    },
    {
        "rank": "3위",
        "name": "믹스견",
        "desc": "다양한 매력과 건강함으로 인기 상승 중!",
        "image": "https://images.unsplash.com/photo-1587300003388-59208cc962cb?w=800"
    },
    {
        "rank": "4위",
        "name": "포메라니안",
        "desc": "작고 귀여운 외모로 많은 사랑을 받아!",
        "image": "https://images.unsplash.com/photo-1548199973-03cce0bbc87b?w=800"
    },
    {
        "rank": "5위",
        "name": "비숑 프리제",
        "desc": "솜사탕 같은 털이 매력 포인트!",
        "image": "https://images.unsplash.com/photo-1525253086316-d0c936c814f8?w=800"
    }
]

cats = [
    {
        "rank": "1위",
        "name": "코리안 숏헤어",
        "desc": "국내에서 가장 많이 기르는 친근한 반려묘!",
        "image": "https://images.unsplash.com/photo-1519052537078-e6302a4968d4?w=800"
    },
    {
        "rank": "2위",
        "name": "페르시안",
        "desc": "우아한 외모와 온순한 성격이 매력!",
        "image": "https://images.unsplash.com/photo-1574158622682-e40e69881006?w=800"
    },
    {
        "rank": "3위",
        "name": "러시안 블루",
        "desc": "푸른빛 털과 똑똑한 성격으로 인기!",
        "image": "https://images.unsplash.com/photo-1533738363-b7f9aef128ce?w=800"
    },
    {
        "rank": "4위",
        "name": "스코티시 폴드",
        "desc": "접힌 귀가 정말 귀여워!",
        "image": "https://images.unsplash.com/photo-1511044568932-338cba0ad803?w=800"
    },
    {
        "rank": "5위",
        "name": "샴",
        "desc": "파란 눈과 활발한 성격이 특징!",
        "image": "https://images.unsplash.com/photo-1513245543132-31f507417b26?w=800"
    }
]

if animal == "🐶 반려견":
    st.header("🐶 선호하는 반려견 순위")

    for pet in dogs:
        st.subheader(f"{pet['rank']} {pet['name']}")
        st.image(pet["image"], use_container_width=True)
        st.success(pet["desc"])
        st.divider()

else:
    st.header("🐱 선호하는 반려묘 순위")

    for pet in cats:
        st.subheader(f"{pet['rank']} {pet['name']}")
        st.image(pet["image"], use_container_width=True)
        st.success(pet["desc"])
        st.divider()

st.markdown("---")
st.caption("🐾 어떤 친구가 가장 마음에 들었어? 😄")
