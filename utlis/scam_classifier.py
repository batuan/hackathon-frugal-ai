import re
from typing import Dict, List, Tuple


class ScamClassifier:
    """Classificateur frugal pour détecter 4 types d'arnaques"""

    def __init__(self):
        # Définition des patterns pour chaque classe
        self.patterns = {
            "email_suspect": {
                "keywords": [
                    r'\bgagn[éeè]\b', r'\bcadeau\b', r'\bprix\b',
                    r'\bloterie\b',
                    r'\bfelicitation\b', r'\brécompense\b', r'\bgratuit\b',
                    r'\bcliqu(ez|er)\b.*\blien\b', r'\bréclam(ez|er)\b',
                    r'\btirage au sort\b', r'\bheureux gagnant\b'
                ],
                "response": {
                    "short": "Cadeau piégé",
                    "long": "Aucune entreprise vous demandera de cliquer sur un lien pour recevoir vos gains."
                }
            },
            "paiement_inattendu": {
                "keywords": [
                    r'\bpay(ez|er|ement)\b', r'\bfrais\b', r'\bfacture\b',
                    r'\brégl(ez|er)\b', r'\bdébloqu(ez|er)\b', r'\bcolis\b',
                    r'\blivraison\b.*\bpay', r'\bsuspend(u|re)\b.*\bcompte\b',
                    r'\bmaintenir.*\bcompte\b', r'\bactiv(ez|er).*\bcompte\b',
                    r'\b\d+[€$£]\b.*\b(urgent|immédiat|maintenant)\b'
                ],
                "response": {
                    "short": "Demande de paiement suspect",
                    "long": "Les entreprises légitimes ne demandent jamais de payer pour débloquer un colis ou maintenir un compte. C'est un signal d'arnaque très courant."
                }
            },
            "faute_orthographe": {
                "indicators": [
                    # Répétition de lettres
                    r'(.)\1{2,}',
                    # Espaces manquants avant ponctuation
                    r'\w[!?:;]{2,}',
                    # Mélange majuscules/minuscules anormal
                    r'\b[A-Z][a-z]+[A-Z]\w+\b',
                    # Fautes courantes
                    r'\bvou\b(?!s)', r'\bvotre\b.*\beste\b', r'\bà\b.*\bétait\b'
                ],
                "response": {
                    "short": "Fautes ou formulation incohérente",
                    "long": "Les arnaques contiennent souvent fautes, tournures étranges ou traduction automatique. C'est un marqueur classique de fraude."
                }
            },
            "demande_infos": {
                "keywords": [
                    r'\bRIB\b', r'\bIBAN\b', r'\bcarte bancaire\b',
                    r'\bcode\b.*\bcarte\b',
                    r'\bcode secret\b', r'\bPIN\b', r'\bCVV\b',
                    r'\bcryptogramme\b',
                    r'\bidentifiant\b', r'\bmot de passe\b', r'\b2FA\b',
                    r'\bOTP\b',
                    r'\bcarte d.identit[ée]\b', r'\bpasseport\b',
                    r'\bpièce d.identité\b',
                    r'\bconfirm(ez|er).*\b(identité|compte|informations)\b',
                    r'\bverifi(ez|er).*\b(identité|compte)\b',
                    r'\bmettre à jour.*\b(coordonnées|informations)\b'
                ],
                "response": {
                    "short": "Demande d'informations sensibles",
                    "long": "Les services officiels ne demandent jamais votre RIB, code 2FA, carte d'identité ou identifiants par message."
                }
            }
        }

    def classify(self, text: str) -> Dict:
        """
        Classifie un texte comme scam ou non

        Args:
            text: Le texte à analyser

        Returns:
            Dict avec is_scam (bool), detected_types (list), et responses (list)
        """
        text_lower = text.lower()
        detected = []

        # Vérifier chaque type d'arnaque
        for scam_type, config in self.patterns.items():
            score = 0

            # Pour faute_orthographe, on utilise 'indicators'
            keywords = config.get('keywords') or config.get('indicators', [])

            for pattern in keywords:
                if re.search(pattern, text_lower):
                    score += 1

            # Seuil: au moins 1 match pour les 3 premiers types
            # Pour faute_orthographe: au moins 2 indicateurs
            threshold = 2 if scam_type == "faute_orthographe" else 1

            if score >= threshold:
                detected.append({
                    "type": scam_type,
                    "score": score,
                    "response": config["response"]
                })

        # Résultat final
        is_scam = len(detected) > 0

        return {
            "is_scam": is_scam,
            "confidence": "high" if len(detected) >= 2 else "medium" if len(
                detected) == 1 else "low",
            "detected_types": [d["type"] for d in detected],
            "responses": [d["response"] for d in detected],
            "details": detected
        }

    def explain(self, result: Dict) -> str:
        """Génère une explication lisible du résultat"""
        if not result["is_scam"]:
            return "✅ Aucun signe d'arnaque détecté."

        explanation = f"⚠️  ARNAQUE DÉTECTÉE (confiance: {result['confidence']})\n\n"

        for response in result["responses"]:
            explanation += f"• {response['short']}\n"
            explanation += f"  {response['long']}\n\n"

        return explanation


# Exemples d'utilisation
if __name__ == "__main__":
    classifier = ScamClassifier()

    # Tests
    tests = [
        "Félicitations! Vous avez gagné un iPhone. Cliquez sur ce lien pour réclamer votre prix.",
        "Votre colis est bloqué. Payez 2,99€ de frais pour débloquer la livraison.",
        "Bonjour, votre compte Amazon a ete suspendu. Confirmez votre identité en envoyant votre RIB.",
        "Rendez-vous demain à 14h pour la réunion.",
        "URGENT!!! Vou devez payyer maintenan pour gardé votre compte actif! Donnez votre IBAN"
    ]

    for i, text in enumerate(tests, 1):
        print(f"\n{'=' * 60}")
        print(f"TEST {i}: {text[:50]}...")
        print('=' * 60)
        result = classifier.classify(text)
        print(classifier.explain(result))