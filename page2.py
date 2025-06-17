# 2_search_notes.py
import streamlit as st

st.title("🔍 노트 검색 기능 데모")

# 샘플 텍스트 데이터
notes = {
    "수학": ["도형의 닮음", "이차함수", "확률"],
    "과학": ["화학 반응", "전자기 유도", "소화 작용"],
    "영어": ["to부정사", "관계대명사", "수동태"]
}

query = st.text_input("검색어를 입력하세요")

if query:
    st.subheader("📑 검색 결과")
    found = False
    for subject, titles in notes.items():
        results = [t for t in titles if query in t]
        if results:
            st.markdown(f"**{subject}** 과목:")
            for r in results:
                st.write(f"- {r}")
            found = True

    if not found:
        st.warning("검색 결과가 없습니다.")
