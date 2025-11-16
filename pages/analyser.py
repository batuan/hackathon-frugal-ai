import streamlit as st
from utlis.utlis import fake_inputs
from streamlit_extras.switch_page_button import switch_page
import json
from machine_learning.predict import predict
from utlis.scam_classifier import ScamClassifier


scam_classifier = ScamClassifier()
st.markdown("<h1 style='text-align: center; color: #483d8b;'>Karnak</h1>", unsafe_allow_html=True)
text = '''

'''
st.markdown(f"", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'> <p style='text-align: center; color: black;'>Protger-vous des arnaques en ligne. \n\n Analyser vos messages en quelques secondes</p></div>", unsafe_allow_html=True)

input_text = st.text_area(label="Texte du message",placeholder="Collez ici le message suspect ...", height=200, )

uploaded_files = st.file_uploader(
    "Image ou capture d'écran", accept_multiple_files=True, type="csv"
)

for uploaded_file in uploaded_files:
    text = fake_inputs

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


        if st.button("Analyser"):
            st.text("detecter encours")
            detect_text = str(input_text)

            predicted, score = predict(detect_text)
            score = round(score, 4)

            result = scam_classifier.classify(detect_text)
            explain = scam_classifier.explain(result)

            with open('results/result.json', 'w') as file:
                data = {
                    "score": score,
                    "message": input_text,
                    "result": result,
                    "explain": explain,
                }
                json.dump(data, file)
            switch_page('result')


from utlis.footer import bottom_text
bottom_text()