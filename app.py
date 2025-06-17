import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="SIL.VER",
    layout="wide"
)

# 배경 스타일 삽입
st.markdown("""
    <style>
        /* 배경 스타일 */
        body {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            color: white;
        }
        .main-title {
            font-size: 5em;
            font-weight: bold;
            text-align: center;
            letter-spacing: 0.2em;
            color: #00ffe5;
            text-shadow: 2px 2px 10px rgba(0,255,229,0.8);
        }
        .subtitle {
            text-align: center;
            font-size: 1.5em;
            color: #e0f7fa;
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
