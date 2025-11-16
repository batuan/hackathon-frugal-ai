import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import json
from utlis.footer import bottom_text


with open('results/result.json') as json_data:
    outputs = json.load(json_data)

st.markdown("## Niveau de suspicion")
st.markdown(f"### {outputs['score'] * 100} %")
st.progress(outputs['score'], text=None)


st.markdown("### Recommandation")
st.text(f"{outputs['explain']}")

center_container = st.container()
with center_container:
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.markdown(
            """<style>
            .stButton>button {
                width: 300px;
                height: 40px;
                font-size: 22px;
                color: white;
                background-color: #4CAF50;   /* green */
                padding: 18px 40px;          /* bigger button */
                border-radius: 12px;         /* rounded corners */
                border: none;
            }
            </style>""",
            unsafe_allow_html=True
        )
        if st.button("Nouvelle analyse"):
            switch_page("analyser")

st.markdown("<br><br><br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
bottom_text()