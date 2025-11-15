import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import json

with open('results/result.json') as json_data:
    fake_outputs = json.load(json_data)

st.text("Niveau de suspicion")
st.title(f"{fake_outputs['score'] * 100} %")


st.progress(fake_outputs['score'], text=None)
st.text("Recommandation")
st.text(f"{fake_outputs['message']}")

if st.button("Nouvelle analyse"):
    switch_page("analyser")






st.text("Notrre IA Analyse le contenu pour détecter les signes d'arnaques courantes")
st.text("Karnak est un project frugal et ethique creer pour proteger tous les utilisaterus contre les arnaques en ligne. "
        "Nous croyons en une technologie accessible, respectuese de la vie privee et au service du bien commun.")


