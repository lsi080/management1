# 4_auto_summary.py
import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

st.title("🧠 자동 요약 기능")

text_input = st.text_area("노트 내용을 입력하세요:", height=200)

if text_input.strip():
    lang = st.radio("언어 선택", ["한글", "영어"])

    if lang == "영어":
        words = word_tokenize(text_input)
        stop_words = set(stopwords.words('english'))
        filtered = [w for w in words if w.isalpha() and w.lower() not in stop_words]
    else:
        filtered = [word for word in text_input.split() if len(word) >= 2 and word.isalpha()]

    freq = {}
    for word in filtered:
        freq[word] = freq.get(word, 0) + 1

    sorted_keywords = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]

    st.subheader("🔑 요약 키워드")
    for word, count in sorted_keywords:
        st.markdown(f"- **{word}** ({count}회 등장)")
else:
    st.info("노트 내용을 입력하면 핵심 키워드를 추출해드립니다.")
