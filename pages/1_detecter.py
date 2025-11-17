import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import json
from machine_learning.predict import predict
from utlis.scam_classifier import ScamClassifier
from PIL import Image
import pytesseract
import numpy as np
from utlis.regex_text import check_all_patterns

# Configuration de la page
st.set_page_config(
    page_title="Détecter - Karnak",
    page_icon="🔍",
    layout="centered"
)

# Styles CSS personnalisés
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }

    .detection-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        margin-bottom: 2rem;
    }

    .info-box {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #2196F3;
        margin: 1.5rem 0;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
    }

    .upload-section {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        margin: 1.5rem 0;
    }

    .stTextArea textarea {
        border: 2px solid #667eea !important;
        border-radius: 10px !important;
        font-size: 1rem !important;
    }

    .stTextArea textarea:focus {
        border-color: #764ba2 !important;
        box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.2) !important;
    }

    .stButton>button {
        width: 100%;
        max-width: 400px;
        height: 60px;
        font-size: 1.3rem;
        font-weight: bold;
        color: white;
        background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
        padding: 18px 40px;
        border-radius: 30px;
        border: none;
        box-shadow: 0 5px 20px rgba(76, 175, 80, 0.4);
        transition: all 0.3s ease;
        cursor: pointer;
        margin: 0 auto;
        display: block;
    }

    .stButton>button:hover {
        background: linear-gradient(135deg, #45a049 0%, #4CAF50 100%);
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(76, 175, 80, 0.5);
    }

    .stButton>button:active {
        transform: translateY(-1px);
    }

    .image-preview {
        border: 3px dashed #667eea;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        margin-top: 1rem;
    }

    .analyzing-spinner {
        text-align: center;
        padding: 2rem;
        background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%);
        border-radius: 10px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# En-tête
st.markdown("""
<div class="detection-header">
    <h1 style='color: white; font-size: 2.5rem; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);'>
        🔍 Détection d'Arnaque
    </h1>
    <p style='color: white; font-size: 1.1rem; margin: 0.5rem 0 0 0; opacity: 0.95;'>
        Analysez vos messages suspects en quelques secondes
    </p>
</div>
""", unsafe_allow_html=True)

# Informations
st.markdown("""
<div class="info-box">
    <h3 style='margin-top: 0; color: #1976d2;'>💡 Comment utiliser</h3>
    <ul style='color: #424242; line-height: 1.8;'>
        <li><strong>Option 1 :</strong> Collez le texte d'un message suspect dans la zone ci-dessous</li>
        <li><strong>Option 2 :</strong> Uploadez une capture d'écran (notre OCR extraira le texte automatiquement)</li>
        <li><strong>Cliquez sur "Analyser"</strong> pour lancer la détection</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Section de saisie du texte
st.markdown("<div class='upload-section'>", unsafe_allow_html=True)
st.markdown("### 📝 Texte du message")
input_text = st.text_area(
    label="Texte du message",
    placeholder="Collez ici le message suspect (SMS, email, message WhatsApp, etc.)...",
    height=200,
    label_visibility="collapsed"
)
st.markdown("</div>", unsafe_allow_html=True)

# Section d'upload d'image
st.markdown("<div class='upload-section'>", unsafe_allow_html=True)
st.markdown("### 📸 Ou uploadez une capture d'écran")
image_text = ""
image = None
img_file_buffer = st.file_uploader(
    "Image ou capture d'écran",
    type=["png", "jpg", "jpeg"],
    label_visibility="collapsed"
)

if img_file_buffer is not None:
    image = Image.open(img_file_buffer)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(image, caption="Image uploadée", use_container_width=True)

    # Extraction du texte avec OCR
    with st.spinner("🔄 Extraction du texte de l'image..."):
        image_text = pytesseract.image_to_string(image)

    if image_text.strip():
        st.success(f"✅ Texte extrait ({len(image_text)} caractères)")
        with st.expander("👁️ Voir le texte extrait"):
            st.text(image_text)
    else:
        st.warning("⚠️ Aucun texte détecté dans l'image")

st.markdown("</div>", unsafe_allow_html=True)

# Bouton d'analyse
st.markdown("<br>", unsafe_allow_html=True)

scam_classifier = ScamClassifier()

if st.button("🚀 Analyser le message"):
    detect_text = str(input_text)
    if len(image_text) > len(detect_text):
        detect_text = str(image_text)

    if not detect_text or detect_text.strip() == "":
        st.error("❌ Veuillez entrer un message ou uploader une image avant d'analyser.")
    else:
        # Animation de chargement
        with st.spinner("🔍 Analyse en cours... Notre IA étudie le message..."):
            predicted, score = predict(detect_text)
            score = round(score, 4)

            result = scam_classifier.classify(detect_text)
            explain = scam_classifier.explain(result)
            message_for_user = check_all_patterns(detect_text)

            # Sauvegarde des résultats
            with open('results/result.json', 'w') as file:
                data = {
                    "score": 1 - score,
                    "message": detect_text,
                    "result": result,
                    "explain": explain,
                    "message_for_user": message_for_user
                }
                json.dump(data, file)

        # Redirection vers la page de résultats
        st.success("✅ Analyse terminée ! Redirection...")
        switch_page('result')

# Retour à l'accueil
st.markdown("<br>", unsafe_allow_html=True)
st.page_link("main.py", label="← Retour à l'accueil", icon="🏠")

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
from utlis.footer import bottom_text
bottom_text()