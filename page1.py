import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# nltk 데이터 다운로드 (최초 1회만 실행됨)
nltk.download('punkt')
nltk.download('stopwords')

st.set_page_config(page_title="NoteSyncer Demo", layout="centered")
st.title("📚 NoteSyncer - 노트 정리 앱 (Streamlit 전용 데모)")
st.markdown("학생들을 위한 **노트 요약 정리 도우미**입니다. 사진이 없어도 텍스트로 직접 입력해 연습할 수 있어요.")

st.subheader("1️⃣ 노트 내용 입력")
text_input = st.text_area("노트 사진에서 복사한 내용이나 직접 입력한 필기를 여기에 붙여넣으세요:", height=200)

if text_input.strip() != "":
    st.subheader("2️⃣ 자동 키워드 요약")

    lang = st.radio("언어 선택", ['한글', '영어'])

    if lang == '영어':
        words = word_tokenize(text_input)
        stop_words = set(stopwords.words('english'))
        filtered_words = [w for w in words if w.isalpha() and w.lower() not in stop_words]
    else:
        filtered_words = [word for word in text_input.split() if len(word) >= 2 and word.isalpha()]

    freq = {}
    for word in filtered_words:
        freq[word] = freq.get(word, 0) + 1

    sorted_keywords = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]

    if sorted_keywords:
        for word, count in sorted_keywords:
            st.markdown(f"- **{word}** ({count}회 등장)")
        st.success("🎉 요약 완료! 이 키워드를 중심으로 복습해보세요.")
    else:
        st.warning("유의미한 키워드를 찾지 못했어요. 입력을 확인해보세요.")

else:
    st.info("노트 내용을 입력하면 자동으로 키워드를 추출해드립니다.")
