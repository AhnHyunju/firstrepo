import streamlit as st

# 제목과 설명
st.title("🧬 Fun with MBTI! 🎉")
st.write("내 MBTI를 입력하고, 나이별 특성과 궁합이 맞는 유형을 확인해보세요! 🧠")

# MBTI 입력받기
mbti = st.text_input("당신의 MBTI를 입력하세요! 🧐", "").upper()

# MBTI별 특성
mbti_traits = {
    "INTJ": "🔍 **INTJ**는 전략적 사고와 독립성을 중시합니다. 어릴 때는 지식 탐구에 몰두하고, 나이가 들수록 목표 지향적이고 계획적인 삶을 추구합니다. 📚",
    "INFP": "🌼 **INFP**는 깊은 감성과 강한 가치관을 가진 유형입니다. 어릴 때는 상상력이 풍부하며, 나이가 들수록 내적 세계에 집중하고, 자기 표현에 힘씁니다. 🎨",
    "ENTP": "💡 **ENTP**는 혁신적이고 논쟁을 즐기는 성향입니다. 어릴 때는 호기심이 많고 모험을 즐기며, 나이가 들수록 새로운 아이디어와 변화를 추구합니다. 🚀",
    "ESFJ": "🤝 **ESFJ**는 따뜻하고 사교적인 성향으로 타인을 돕는 것을 좋아합니다. 어릴 때부터 주변 사람들과 잘 어울리며, 나이가 들수록 책임감이 강해지고 사회적 역할을 중시합니다. 🌍",
    # 여기에 다른 MBTI 유형에 대한 설명도 추가할 수 있습니다.
}

# MBTI 궁합
best_matches = {
    "INTJ": "❤️ INTJ와 잘 맞는 유형: ENFP, ENTJ",
    "INFP": "💞 INFP와 잘 맞는 유형: ENFJ, ENTJ",
    "ENTP": "✨ ENTP와 잘 맞는 유형: INFJ, INTJ",
    "ESFJ": "💖 ESFJ와 잘 맞는 유형: ISFP, ISTP",
}

worst_matches = {
    "INTJ": "⚠️ INTJ와 덜 맞는 유형: ESFP, ISFP",
    "INFP": "⚡ INFP와 덜 맞는 유형: ESTJ, ISTJ",
    "ENTP": "⚔️ ENTP와 덜 맞는 유형: ISFJ, ESFJ",
    "ESFJ": "🌀 ESFJ와 덜 맞는 유형: INTP, INTJ",
}

# 입력된 MBTI에 따른 결과 출력
if mbti in mbti_traits:
    st.subheader(f"📊 {mbti}의 나이별 특성")
    st.write(mbti_traits[mbti])
    
    st.subheader(f"👩‍❤️‍👨 {mbti}와 잘 맞는 유형")
    st.write(best_matches[mbti])
    
    st.subheader(f"💔 {mbti}와 덜 맞는 유형")
    st.write(worst_matches[mbti])
else:
    st.write("⚠️ 유효한 MBTI 유형을 입력해주세요! (예: INTJ, INFP, ENTP, ESFJ)")
