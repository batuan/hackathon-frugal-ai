import streamlit as st

def bottom_text():
    st.markdown("""
    <div style='text-align:center; font-size:14px;'>
        <span style="color:black; font-weight:bold;">Notre IA analyse le contenu pour détecter les signes d'arnaques courantes</span><br>
        <span style="color:black; font-weight:bold;">Karnak est un project frugal et éthique créé pour protéger tous les utilisaterus contre les arnaques en ligne.</span>
        <span style="color:black; font-weight:bold;">Nous croyons en une technologie accessible, respectueuse de la vie privée et au service du bien commun.</span><br>
    </div>
    """, unsafe_allow_html=True)
