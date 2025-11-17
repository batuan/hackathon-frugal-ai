# 🛡️ Karnak - Détecteur d'Arnaques Frugal et Éthique

<div align="center">

**Protégez-vous des arnaques en ligne grâce à l'intelligence artificielle frugale**

[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.43.0-FF4B4B.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

[Fonctionnalités](#-fonctionnalités) • [Installation](#-installation) • [Utilisation](#-utilisation) • [Technologies](#-technologies) • [Architecture](#-architecture)

</div>

---

## 📋 Table des Matières

- [À Propos](#-à-propos)
- [Fonctionnalités](#-fonctionnalités)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Technologies](#-technologies)
- [Architecture](#-architecture)
- [Comment ça Marche](#-comment-ça-marche)
- [Développement](#-développement)
- [Contribuer](#-contribuer)
- [License](#-license)

---

## 🎯 À Propos

**Karnak** est une application web de détection d'arnaques conçue pour protéger les utilisateurs francophones contre les fraudes en ligne. Notre mission est de rendre la protection contre les arnaques accessible à tous grâce à une approche **frugale et éthique** de l'intelligence artificielle.

### Pourquoi "Frugal" ?

- **Accessible** : Modèles légers qui fonctionnent sur du matériel modeste
- **Rapide** : Analyse en quelques secondes
- **Économique** : Pas besoin de serveurs puissants ou de GPU
- **Écologique** : Empreinte carbone réduite

### Notre Engagement Éthique

- 🔒 **Respect de la vie privée** : Aucune donnée personnelle n'est stockée
- 🌍 **Bien commun** : Technologie au service de tous
- 🎓 **Éducation** : Documentation et exemples pour sensibiliser
- 💚 **Open Source** : Code transparent et vérifiable

---

## ✨ Fonctionnalités

### 🔍 Détection Multi-Méthodes

1. **Machine Learning**
   - Classification par TF-IDF et modèles entraînés
   - Régression logistique et forêts aléatoires
   - Word2Vec pour l'analyse sémantique

2. **Analyse par Règles**
   - Détection de patterns de fraude connus
   - Identification des erreurs d'orthographe suspectes
   - Repérage des demandes d'informations sensibles

3. **OCR (Reconnaissance Optique)**
   - Extraction de texte à partir de captures d'écran
   - Analyse d'images de messages suspects
   - Support PNG, JPG, JPEG

### 🎯 Types d'Arnaques Détectés

- 🎁 **Cadeaux piégés** : Faux concours et prix miraculeux
- 📦 **Faux colis** : Notifications de livraison frauduleuses
- 🏦 **Fraude bancaire** : Demandes de coordonnées bancaires
- 💳 **Phishing** : Usurpation d'identité (Ameli, Netflix, CPF...)
- 💔 **Arnaques sentimentales** : Manipulation affective
- 📱 **SMS frauduleux** : Messages de services officiels falsifiés

### 📊 Résultats Clairs

- **Score de suspicion** : Pourcentage de probabilité d'arnaque (0-100%)
- **Barre de progression visuelle** : Visualisation intuitive du risque
- **Recommandations personnalisées** : Conseils adaptés au type d'arnaque
- **Explications détaillées** : Compréhension des signaux détectés

---

## 🚀 Installation

### Prérequis

- **Python 3.12 ou supérieur**
- **Tesseract OCR** (pour l'analyse d'images)

### Installation Rapide avec `uv`

Nous recommandons l'utilisation de [`uv`](https://docs.astral.sh/uv/), un gestionnaire de paquets Python ultra-rapide.

#### 1. Installer `uv`

**macOS / Linux :**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows :**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Avec pip :**
```bash
pip install uv
```

#### 2. Installer Python 3.12

```bash
uv python install 3.12
uv python pin 3.12
```

#### 3. Installer Tesseract OCR

**Ubuntu/Debian :**
```bash
sudo apt-get install tesseract-ocr tesseract-ocr-fra
```

**macOS (Homebrew) :**
```bash
brew install tesseract tesseract-lang
```

**Windows :**
Téléchargez depuis [GitHub Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)

#### 4. Cloner le Projet

```bash
git clone https://github.com/batuan/hackathon-frugal-ai.git
cd hackathon-frugal-ai
```

#### 5. Installer les Dépendances

```bash
uv sync
```

#### 6. Activer l'Environnement Virtuel

**Linux/macOS :**
```bash
source .venv/bin/activate
```

**Windows :**
```powershell
.venv\Scripts\activate
```

---

## 💻 Utilisation

### Lancer l'Application

```bash
python -m streamlit run main.py
```

ou

```bash
streamlit run main.py
```

L'application sera accessible à l'adresse : **http://localhost:8501**

### Interface Utilisateur

#### 1. **Page d'Accueil** 🏠
   - Navigation vers les différentes sections
   - Présentation du projet

#### 2. **Page de Détection** 📈
   - **Coller un message** : Texte SMS, email, ou message suspect
   - **Uploader une image** : Capture d'écran d'un message
   - **Cliquer sur "Analyser"** : Lancement de l'analyse

#### 3. **Page de Résultats** 🤖
   - **Score de suspicion** : Probabilité que le message soit une arnaque
   - **Recommandations** : Actions à prendre
   - **Nouvelle analyse** : Retour à la page de détection
   - **En savoir plus** : Documentation sur les arnaques

#### 4. **Documentation** 📚
   - Exemples d'arnaques réelles
   - Conseils de prévention
   - Images et captures d'écran

---

## 🛠️ Technologies

### Frontend
- **[Streamlit 1.43.0](https://streamlit.io)** - Framework web interactif
- **[Streamlit Extras](https://github.com/arnaudmiribel/streamlit-extras)** - Composants additionnels
- **HTML/CSS** - Personnalisation de l'interface

### Machine Learning
- **[scikit-learn 1.7.2](https://scikit-learn.org)** - Modèles de classification
  - Régression Logistique
  - Forêt Aléatoire (Random Forest)
  - Multinomial Naive Bayes
- **[sentence-transformers 5.1.2](https://www.sbert.net)** - Embeddings de texte
- **[gensim 4.4.0](https://radimrehurek.com/gensim/)** - Word2Vec et NLP
- **[NLTK 3.9.2](https://www.nltk.org)** - Traitement du langage naturel

### Traitement de Texte
- **[pytesseract 0.3.13](https://github.com/madmaze/pytesseract)** - OCR (Optical Character Recognition)
- **[Tesseract](https://github.com/tesseract-ocr/tesseract)** - Moteur OCR
- **[contractions 0.1.73](https://github.com/kootenpv/contractions)** - Normalisation de texte
- **[stopwords 1.0.2](https://github.com/Alir3z4/python-stopwords)** - Suppression des mots vides
- **[Pillow (PIL)](https://pillow.readthedocs.io)** - Traitement d'images

### Développement
- **[uv](https://github.com/astral-sh/uv)** - Gestionnaire de paquets Python ultra-rapide
- **[Dev Containers](https://containers.dev)** - Environnement de développement conteneurisé

---

## 📁 Architecture

```
hackathon-frugal-ai/
├── 📂 .devcontainer/           # Configuration Dev Container
│   └── devcontainer.json
│
├── 📂 documentation/           # Documentation et exemples
│   ├── images/                 # Captures d'écran d'arnaques (11 exemples)
│   ├── doc.md                  # Documentation utilisateur
│   └── screen.md               # Documentation des captures
│
├── 📂 machine_learning/        # Modèles et prédictions
│   ├── models/                 # Modèles pré-entraînés (.pkl, .h5)
│   │   ├── classification_model.pkl        (8.2 MB)
│   │   ├── classification_model_sender.pkl (279 KB)
│   │   ├── tfidf_vectorizer.pkl           (21.7 MB)
│   │   ├── vectorizer.pkl                 (35 KB)
│   │   ├── multinomialnb.pkl              (32 KB)
│   │   └── Word2vec_entraine.h5           (73 KB)
│   ├── hackathon.ipynb         # Notebook d'entraînement
│   ├── test.ipynb              # Notebook de tests
│   ├── predict.py              # Fonctions de prédiction
│   └── utlis.py                # Utilitaires ML
│
├── 📂 pages/                   # Pages Streamlit (multi-page app)
│   ├── 1_detecter.py           # Page de détection (UI principale)
│   ├── 2_result.py             # Page de résultats
│   ├── 3_email.py              # Page email (stub)
│   ├── 4_document.py           # Page de documentation
│   └── config.toml             # Configuration des pages
│
├── 📂 results/                 # Résultats temporaires
│   └── result.json             # Résultats de l'analyse
│
├── 📂 utlis/                   # Modules utilitaires
│   ├── footer.py               # Composant pied de page
│   ├── regex_text.py           # Détection par regex
│   ├── scam_classifier.py      # Classificateur basé sur règles
│   └── utlis.py                # Utilitaires généraux
│
├── 📄 main.py                  # Point d'entrée de l'application
├── 📄 pyproject.toml           # Dépendances du projet
├── 📄 uv.lock                  # Fichier de verrouillage
├── 📄 README.md                # Ce fichier
└── 📄 .python-version          # Version Python (3.12)
```

---

## 🧠 Comment ça Marche

### Pipeline de Détection

```
┌─────────────────────┐
│  Message Suspect    │  ← Texte ou Image
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   OCR (si image)    │  ← Extraction du texte
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Prétraitement      │  ← Nettoyage, normalisation
└──────────┬──────────┘
           │
           ├──────────────────────┬──────────────────────┐
           ▼                      ▼                      ▼
┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐
│ ML Classification│   │ Détection Regex  │   │ Analyse Règles   │
│  (TF-IDF + RF)   │   │  (Patterns)      │   │  (Heuristiques)  │
└────────┬─────────┘   └────────┬─────────┘   └────────┬─────────┘
         │                      │                      │
         └──────────────────────┼──────────────────────┘
                                ▼
                    ┌──────────────────────┐
                    │  Agrégation Scores   │
                    └──────────┬───────────┘
                               ▼
                    ┌──────────────────────┐
                    │  Résultat + Conseils │
                    └──────────────────────┘
```

### 1. Extraction du Texte

- **Texte direct** : Utilisé tel quel
- **Image** : Tesseract OCR extrait le texte de l'image

### 2. Prétraitement

```python
# utlis/utlis.py et machine_learning/utlis.py
- Expansion des contractions (j'ai → je ai)
- Suppression des stopwords (le, la, de, un...)
- Lemmatisation
- Nettoyage des caractères spéciaux
```

### 3. Classification Machine Learning

```python
# machine_learning/predict.py
- Vectorisation TF-IDF du texte
- Prédiction avec modèle de classification
- Score de confiance (0 = légitime, 1 = arnaque)
```

### 4. Détection par Règles

```python
# utlis/scam_classifier.py
- Règles basées sur des patterns connus
- Détection de mots-clés suspects
- Analyse de la structure du message
```

### 5. Analyse par Regex

```python
# utlis/regex_text.py
- Patterns d'arnaques spécifiques
- Détection de demandes d'argent
- Identification de fautes d'orthographe typiques
```

---

## 🔧 Développement

### Environnement Dev Container

Le projet inclut une configuration Dev Container pour VSCode :

```bash
# Ouvrir dans VSCode
code .

# Puis : "Reopen in Container" (Ctrl+Shift+P)
```

Le container :
- Installe automatiquement Python 3.11 (à mettre à jour vers 3.12)
- Configure l'environnement virtuel
- Lance Streamlit sur le port 8501
- Inclut les extensions VSCode (Python, Pylance)

### Entraîner les Modèles

```bash
# Lancer Jupyter
jupyter notebook

# Ouvrir machine_learning/hackathon.ipynb
# Suivre les étapes d'entraînement
```

### Tests

```bash
# Tests unitaires (à implémenter)
pytest

# Tester une prédiction
python -c "from machine_learning.predict import predict; print(predict('Gagnez 1000€ maintenant!'))"
```

### Structure du Code

#### Pages Streamlit

**`pages/1_detecter.py`** : Interface de détection
- Input texte et upload d'image
- Bouton d'analyse
- Navigation vers résultats

**`pages/2_result.py`** : Affichage des résultats
- Score de suspicion
- Barre de progression
- Recommandations

**`pages/4_document.py`** : Documentation
- Exemples d'arnaques
- Guide de prévention

#### Modules ML

**`machine_learning/predict.py`** : Prédictions
```python
def predict(text: str) -> tuple[str, float]:
    """
    Prédit si un texte est une arnaque

    Args:
        text: Texte à analyser

    Returns:
        (label, score): "spam" ou "ham", probabilité
    """
```

**`utlis/scam_classifier.py`** : Classification par règles
```python
class ScamClassifier:
    def classify(text: str) -> dict:
        """Classifie le texte selon des règles"""

    def explain(result: dict) -> str:
        """Génère une explication"""
```

**`utlis/regex_text.py`** : Détection par patterns
```python
def check_all_patterns(text: str) -> str:
    """
    Vérifie tous les patterns d'arnaques

    Returns:
        Message d'avertissement pour l'utilisateur
    """
```

---

## 🤝 Contribuer

Les contributions sont les bienvenues ! Voici comment participer :

### 1. Fork le Projet

```bash
git clone https://github.com/batuan/hackathon-frugal-ai.git
cd hackathon-frugal-ai
```

### 2. Créer une Branche

```bash
git checkout -b feature/amelioration-ui
```

### 3. Faire vos Modifications

- Respecter le style de code existant
- Ajouter des commentaires en français
- Tester vos changements

### 4. Commit

```bash
git add .
git commit -m "Amélioration: Description de vos changements"
```

### 5. Push et Pull Request

```bash
git push origin feature/amelioration-ui
```

Puis créez une Pull Request sur GitHub.

### Idées de Contributions

- 🎨 **Amélioration UI/UX** : Rendre l'interface plus intuitive
- 🧠 **Nouveaux modèles** : Ajouter des modèles de détection
- 🌍 **Internationalisation** : Support d'autres langues
- 📊 **Visualisations** : Graphiques et statistiques
- 🧪 **Tests** : Ajouter des tests unitaires et d'intégration
- 📚 **Documentation** : Améliorer la documentation
- 🔍 **Nouveaux patterns** : Ajouter des patterns d'arnaques

---

## 📄 License

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## 🙏 Remerciements

- **Streamlit** pour le framework web
- **scikit-learn** pour les outils de machine learning
- **Tesseract** pour l'OCR
- **La communauté open source** pour tous les packages utilisés

---

## 📞 Contact & Support

- **Issues** : [GitHub Issues](https://github.com/batuan/hackathon-frugal-ai/issues)
- **Discussions** : [GitHub Discussions](https://github.com/batuan/hackathon-frugal-ai/discussions)

---

<div align="center">

**Fait avec ❤️ pour protéger les utilisateurs francophones contre les arnaques en ligne**

⭐ **Si ce projet vous aide, donnez-lui une étoile !** ⭐

</div>
