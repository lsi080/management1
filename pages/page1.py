# 1_auto_sort.py
import streamlit as st
from PIL import Image
import datetime
import os

st.title("📂 노트 자동 분류")

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
        st.success(f"📁 {folder}/{title}.png 으로 저장 완료!")
