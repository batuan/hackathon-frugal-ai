import streamlit as st
from utlis.utlis import fake_inputs
from streamlit_extras.switch_page_button import switch_page
import json
from machine_learning.predict import predict
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

if st.button("Analyser"):
    st.text("detecter encours")
    predicted, score = predict(str(input_text))

    with open('results/result.json', 'w') as file:
        data = {
            "score": score,
            "message": input_text,
        }
        json.dump(data, file)
    switch_page('result')


st.text("Notrre IA Analyse le contenu pour détecter les signes d'arnaques courantes")
st.text("Karnak est un project frugal et ethique creer pour proteger tous les utilisaterus contre les arnaques en ligne. "
        "Nous croyons en une technologie accessible, respectuese de la vie privee et au service du bien commun.")