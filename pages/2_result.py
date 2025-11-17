import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import json
from utlis.footer import bottom_text

# Configuration de la page
st.set_page_config(
    page_title="Résultat - Karnak",
    page_icon="🤖",
    layout="centered"
)

# Chargement des résultats
with open('results/result.json') as json_data:
    outputs = json.load(json_data)

score = round(float(outputs['score']), 4)
score_percentage = score * 100

# Déterminer le niveau de risque et les couleurs
if score_percentage >= 70:
    risk_level = "ÉLEVÉ"
    risk_emoji = "🔴"
    risk_color = "#f44336"
    gradient_color = "linear-gradient(135deg, #ff5252 0%, #f44336 100%)"
    message_bg = "#ffebee"
    recommendation_title = "⚠️ Attention : Forte probabilité d'arnaque"
elif score_percentage >= 40:
    risk_level = "MOYEN"
    risk_emoji = "🟡"
    risk_color = "#ff9800"
    gradient_color = "linear-gradient(135deg, #ffa726 0%, #ff9800 100%)"
    message_bg = "#fff3e0"
    recommendation_title = "⚡ Vigilance : Signes suspects détectés"
else:
    risk_level = "FAIBLE"
    risk_emoji = "🟢"
    risk_color = "#4CAF50"
    gradient_color = "linear-gradient(135deg, #66bb6a 0%, #4CAF50 100%)"
    message_bg = "#e8f5e9"
    recommendation_title = "✅ Risque faible : Message probablement légitime"

# Styles CSS personnalisés
st.markdown(f"""
<style>
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}

    .main {{
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }}

    .result-header {{
        text-align: center;
        padding: 2rem 0;
        background: {gradient_color};
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        margin-bottom: 2rem;
    }}

    .score-container {{
        background: white;
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        margin: 2rem 0;
        text-align: center;
        border: 3px solid {risk_color};
    }}

    .score-number {{
        font-size: 4rem;
        font-weight: bold;
        color: {risk_color};
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        margin: 0;
    }}

    .risk-badge {{
        display: inline-block;
        padding: 10px 30px;
        background: {gradient_color};
        color: white;
        border-radius: 25px;
        font-size: 1.2rem;
        font-weight: bold;
        margin-top: 1rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }}

    .recommendation-box {{
        background: {message_bg};
        padding: 2rem;
        border-radius: 15px;
        border-left: 5px solid {risk_color};
        margin: 2rem 0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }}

    .message-box {{
        background: #f5f5f5;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1.5rem 0;
        border-left: 4px solid #667eea;
        font-family: monospace;
        max-height: 200px;
        overflow-y: auto;
    }}

    .action-button {{
        width: 100%;
        max-width: 350px;
        height: 55px;
        font-size: 1.2rem;
        font-weight: bold;
        color: white;
        padding: 15px 35px;
        border-radius: 27px;
        border: none;
        box-shadow: 0 5px 20px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        cursor: pointer;
        margin: 0.5rem auto;
        display: block;
    }}

    .action-button-primary {{
        background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
    }}

    .action-button-primary:hover {{
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(76, 175, 80, 0.4);
    }}

    .action-button-secondary {{
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }}

    .action-button-secondary:hover {{
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }}

    .stButton>button {{
        width: 100%;
        max-width: 350px;
        height: 55px;
        font-size: 1.2rem;
        font-weight: bold;
        color: white;
        padding: 15px 35px;
        border-radius: 27px;
        border: none;
        box-shadow: 0 5px 20px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        cursor: pointer;
        margin: 0 auto;
        display: block;
    }}

    .stButton>button:hover {{
        transform: translateY(-3px);
    }}

    .info-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1rem;
        margin: 1.5rem 0;
    }}

    .info-card {{
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
        text-align: center;
    }}

    .stProgress > div > div > div > div {{
        background-color: {risk_color};
    }}
</style>
""", unsafe_allow_html=True)

# En-tête
st.markdown(f"""
<div class="result-header">
    <h1 style='color: white; font-size: 2.5rem; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);'>
        {risk_emoji} Résultat de l'Analyse
    </h1>
    <p style='color: white; font-size: 1.1rem; margin: 0.5rem 0 0 0; opacity: 0.95;'>
        Analyse terminée avec succès
    </p>
</div>
""", unsafe_allow_html=True)

# Score principal
st.markdown(f"""
<div class="score-container">
    <h2 style='color: #424242; margin-top: 0;'>Niveau de Suspicion</h2>
    <p class="score-number">{score_percentage:.1f}%</p>
    <div class="risk-badge">{risk_emoji} Risque {risk_level}</div>
</div>
""", unsafe_allow_html=True)

# Barre de progression
st.progress(score, text=None)

# Message analysé
st.markdown("### 📨 Message analysé")
st.markdown(f"""
<div class="message-box">
    {outputs.get('message', 'Aucun message disponible')[:500]}{'...' if len(outputs.get('message', '')) > 500 else ''}
</div>
""", unsafe_allow_html=True)

# Recommandations
st.markdown(f"""
<div class="recommendation-box">
    <h3 style='color: {risk_color}; margin-top: 0;'>{recommendation_title}</h3>
    <p style='font-size: 1.1rem; line-height: 1.8; color: #424242;'>
        {outputs['message_for_user']}
    </p>
</div>
""", unsafe_allow_html=True)

# Conseils de sécurité
if score_percentage >= 40:
    st.markdown(f"""
    <div style='background: #e3f2fd; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #2196F3; margin: 1.5rem 0;'>
        <h3 style='color: #1976d2; margin-top: 0;'>🛡️ Conseils de sécurité</h3>
        <ul style='color: #424242; line-height: 1.8;'>
            <li><strong>Ne partagez jamais</strong> vos informations personnelles (mots de passe, RIB, numéro de carte)</li>
            <li><strong>Vérifiez l'expéditeur</strong> : Les organismes officiels ne demandent jamais d'informations sensibles par SMS/email</li>
            <li><strong>Ne cliquez pas</strong> sur les liens suspects</li>
            <li><strong>En cas de doute</strong> : Contactez directement l'organisme via leurs canaux officiels</li>
            <li><strong>Signalez</strong> le message aux autorités compétentes (Pharos, 33700)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Boutons d'action
st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""<style>
        div[data-testid="column"]:nth-of-type(1) .stButton>button {
            background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
        }
        div[data-testid="column"]:nth-of-type(1) .stButton>button:hover {
            box-shadow: 0 8px 25px rgba(76, 175, 80, 0.4);
        }
    </style>""", unsafe_allow_html=True)
    if st.button("🔄 Nouvelle analyse"):
        switch_page("detecter")

with col2:
    st.markdown("""<style>
        div[data-testid="column"]:nth-of-type(2) .stButton>button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        div[data-testid="column"]:nth-of-type(2) .stButton>button:hover {
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
        }
    </style>""", unsafe_allow_html=True)
    if st.button("📚 En savoir plus"):
        switch_page("document")

# Retour à l'accueil
st.markdown("<br>", unsafe_allow_html=True)
st.page_link("main.py", label="← Retour à l'accueil", icon="🏠")

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
bottom_text()