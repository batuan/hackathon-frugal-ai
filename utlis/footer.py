import streamlit as st

def bottom_text():
    st.markdown("""
    <div style='
        text-align: center;
        padding: 2rem 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        margin-top: 3rem;
        box-shadow: 0 5px 20px rgba(0,0,0,0.15);
    '>
        <h3 style='color: white; margin-top: 0; margin-bottom: 1rem; font-size: 1.3rem;'>
            🛡️ À propos de Karnak
        </h3>
        <p style='color: white; font-size: 1rem; line-height: 1.8; margin: 0.5rem 0; opacity: 0.95;'>
            <strong>Notre IA analyse le contenu pour détecter les signes d'arnaques courantes</strong>
        </p>
        <p style='color: white; font-size: 1rem; line-height: 1.8; margin: 0.5rem 0; opacity: 0.95;'>
            Karnak est un projet <strong>frugal et éthique</strong> créé pour protéger tous les utilisateurs contre les arnaques en ligne.
        </p>
        <p style='color: white; font-size: 1rem; line-height: 1.8; margin: 0.5rem 0; opacity: 0.95;'>
            Nous croyons en une technologie <strong>accessible</strong>, <strong>respectueuse de la vie privée</strong> et <strong>au service du bien commun</strong>.
        </p>
        <hr style='border: none; border-top: 1px solid rgba(255,255,255,0.3); margin: 1.5rem 0;'>
        <p style='color: white; font-size: 0.9rem; margin: 0; opacity: 0.9;'>
            Made with ❤️ by the Karnak Team | 2025
        </p>
    </div>
    """, unsafe_allow_html=True)
