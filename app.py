import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="SIL.VER",
    layout="wide"
)

# 배경 및 텍스트 스타일 조정
st.markdown("""
    <style>
        /* 배경 스타일 */
        body {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            color: white;
        }
        .main-title {
            font-size: 5em;
            font-weight: 900;
            text-align: center;
            letter-spacing: 0.1em;
            color: #78d9ff; /* 더 부드러운 파란색 */
            text-shadow: 1px 1px 5px rgba(120, 217, 255, 0.5);
        }
        .subtitle {
            text-align: center;
            font-size: 1.6em;
            font-weight: 400;
            color: #c0d6df;  /* 회색 + 청록 계열로 부드럽게 */
            margin-top: -10px;
            margin-bottom: 30px;
        }
        .container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 80vh;
            flex-direction: column;
        }
    </style>
""", unsafe_allow_html=True)

# 메인 콘텐츠
st.markdown("""
    <div class="container">
        <div class="main-title">SIL.VER</div>
        <div class="subtitle">이 앱에 오신 것을 환영합니다</div>
    </div>
""", unsafe_allow_html=True)
