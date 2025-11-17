import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Karnak - Détecteur d'Arnaques",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Styles CSS personnalisés
hide_st_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    div.embeddedAppMetaInfoBar_container__DxxL1 {visibility: hidden;}

    /* Styles personnalisés */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }

    .title-container {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        margin-bottom: 2rem;
    }

    .welcome-box {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        margin: 2rem auto;
        max-width: 800px;
    }

    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border-left: 4px solid #667eea;
        transition: transform 0.3s ease;
    }

    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 20px rgba(0,0,0,0.15);
    }

    .nav-button {
        display: inline-block;
        padding: 15px 30px;
        margin: 10px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        text-decoration: none;
        border-radius: 25px;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }

    .nav-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# En-tête principal
st.markdown("""
<div class="title-container">
    <h1 style='color: white; font-size: 3.5rem; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);'>
        🛡️ Karnak
    </h1>
    <p style='color: white; font-size: 1.3rem; margin: 0.5rem 0 0 0; opacity: 0.95;'>
        Détecteur d'Arnaques Intelligent
    </p>
</div>
""", unsafe_allow_html=True)

# Message de bienvenue
st.markdown("""
<div class="welcome-box">
    <h2 style='color: #483d8b; text-align: center; margin-bottom: 1rem;'>
        Bienvenue sur Karnak
    </h2>
    <p style='font-size: 1.1rem; text-align: center; color: #555; line-height: 1.6;'>
        Protégez-vous des arnaques en ligne grâce à notre intelligence artificielle <strong>frugale et éthique</strong>.
        Analysez vos messages suspects en quelques secondes et recevez des recommandations personnalisées.
    </p>
</div>
""", unsafe_allow_html=True)

# Navigation avec cartes
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3 style='color: #667eea; margin-top: 0;'>🏠 Accueil</h3>
        <p style='color: #666;'>Découvrez comment Karnak vous protège contre les arnaques en ligne</p>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("main.py", label="Aller à l'accueil", icon="🏠")

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3 style='color: #4CAF50; margin-top: 0;'>🔍 Détecter</h3>
        <p style='color: #666;'>Analysez un message ou une image pour détecter les tentatives d'arnaque</p>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/1_detecter.py", label="Analyser un message", icon="🔍")

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3 style='color: #FF6B6B; margin-top: 0;'>📚 Documentation</h3>
        <p style='color: #666;'>Apprenez à reconnaître les différents types d'arnaques</p>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/4_document.py", label="En savoir plus", icon="📚")

# Section "Comment ça marche"
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div class="welcome-box">
    <h2 style='color: #483d8b; text-align: center; margin-bottom: 1.5rem;'>
        Comment ça marche ?
    </h2>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card" style='border-left-color: #4CAF50;'>
        <h3 style='color: #4CAF50;'>1️⃣ Analysez</h3>
        <p style='color: #666;'>Collez le texte du message suspect ou uploadez une capture d'écran</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card" style='border-left-color: #2196F3;'>
        <h3 style='color: #2196F3;'>2️⃣ IA Frugale</h3>
        <p style='color: #666;'>Notre modèle léger analyse le contenu en quelques secondes</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card" style='border-left-color: #FF6B6B;'>
        <h3 style='color: #FF6B6B;'>3️⃣ Résultats</h3>
        <p style='color: #666;'>Recevez un score de suspicion et des recommandations claires</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
from utlis.footer import bottom_text
st.markdown("<br><br>", unsafe_allow_html=True)
bottom_text()