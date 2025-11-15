import streamlit as st

st.page_link("main.py", label="Home", icon="🏠")
st.page_link("pages/analyser.py", label="Analyser", icon="📈")
st.page_link("pages/result.py", label="Result", icon="🤖")


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            div.embeddedAppMetaInfoBar_container__DxxL1 {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)