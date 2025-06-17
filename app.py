# main.py
import streamlit as st
from PIL import Image
import datetime
import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# nltk 데이터 다운로드 (처음 1회)
nltk.download('punkt')
nltk.download('stopwords')

# -----------------------------
# 📂 자동 분류 기능
def auto_sort():
    st.subheader("📂 노트 자동 분류")

    uploaded_file = st.file_uploader("노트 사진을 업로드하세요", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="업로드한 노트 사진", use_column_width=True)

        today = datetime.date.today()
        subject = st.selectbox("과목 선택", ["수학", "과학", "영어", "국어", "기타"])
        title = st.text_input("노트 제목 입력", "예: 도형의 닮음")

        if st.button("저장"):
            folder = f"노트/{subject}/{today}"
            os.makedirs(folder, exist_ok=True)
            image.save(f"{folder}/{title}.png")
            st.success(f"✅ 저장 완료: {folder}/{title}.png")

# -----------------------------
# 🔍 검색 기능
def search_notes():
    st.subheader("🔍 노트 검색")

    # 샘플 노트 데이터
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

# -----------------------------
# 📅 시험 대비 기능
def exam_mode():
    st.subheader("📅 시험 대비 모드")

    exam_date = st.date_input("시험 날짜를 선택하세요")
    today = datetime.date.today()
    days_left = (exam_date - today).days

    st.markdown(f"⏰ 시험까지 **{days_left}일 남음**")

    st.subheader("📚 과목별 추천 노트")

    study_notes = {
        "수학": ["도형의 닮음", "이차함수"],
        "과학": ["화학 반응식", "전류와 자기장"],
        "국어": ["설명문", "비문학 독해"]
    }

    for subject, topics in study_notes.items():
        st.markdown(f"### {subject}")
        for topic in topics:
            st.markdown(f"- 📄 {topic}")

# -----------------------------
# 🧠 자동 요약 기능
def auto_summary():
    st.subheader("🧠 자동 요약")

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

# -----------------------------
# 🚀 메인 실행
st.set_page_config(page_title="NoteSyncer", layout="centered")
st.title("📚 NoteSyncer")
st.markdown("학생들을 위한 **사진 노트 정리 & 요약 앱**입니다. 아래 기능 중 하나를 선택해보세요!")

menu = st.sidebar.selectbox("기능 선택", ["📂 노트 자동 분류", "🔍 노트 검색", "📅 시험 대비 모드", "🧠 자동 요약"])

if menu == "📂 노트 자동 분류":
    auto_sort()
elif menu == "🔍 노트 검색":
    search_notes()
elif menu == "📅 시험 대비 모드":
    exam_mode()
elif menu == "🧠 자동 요약":
    auto_summary()
