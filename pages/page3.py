# 3_exam_mode.py
import streamlit as st
import datetime

st.title("📅 시험 대비 노트 모음")

exam_date = st.date_input("시험 날짜를 선택하세요")
today = datetime.date.today()
days_left = (exam_date - today).days

st.markdown(f"⏰ 시험까지 **{days_left}일 남음**")

st.subheader("📚 자동 추천 과목별 노트")

# 샘플 자료
study_notes = {
    "수학": ["도형의 닮음", "이차함수"],
    "과학": ["화학 반응식", "전류와 자기장"],
    "국어": ["설명문", "비문학 독해"]
}

for subject, topics in study_notes.items():
    st.markdown(f"### {subject}")
    for topic in topics:
        st.markdown(f"- 📄 {topic}")
