import re

json_message = {
  "email_suspect": {
    "short": "Cadeau piégé",
    "long": "Aucune entreprise vous demandera de cliquer sur un lien pour recevoir vos gains."
  },
  "paiement_inattendu": {
    "short": "Demande de paiement suspect",
    "long": "Les entreprises légitimes ne demandent jamais de payer pour débloquer un colis ou maintenir un compte. C’est un signal d’arnaque très courant."
  },
  "faute_orthographe": {
    "short": "Fautes ou formulation incohérente",
    "long": "Les arnaques contiennent souvent fautes, tournures étranges ou traduction automatique. C’est un marqueur classique de fraude."
  },
  "demande_infos": {
    "short": "Demande d'informations sensibles",
    "long": "Les services officiels ne demandent jamais votre RIB, code 2FA, carte d'identité ou identifiants par message."
  },
    "colis": {
        "short": "Colis jamais commandé",
        "long": "Les livraisons de colis ne demandent jamais de confirmation ou de paiement supplémentaire. Vérifier directement sur le site sur lequel vous avez commandé",
    }
}

patterns_ortho = [
    re.compile(r'[a-z][!?:;] '),
    # re.compile(r'^[a-z]'),
    re.compile(r'\w[!?:;]{2,}'),
    re.compile(r'\b[A-Z][a-z]+[A-Z]\w+\b'),
    re.compile(r'\bvou\b(?!s)'),
    re.compile(r'\bvotre\b.*\beste\b'),
    re.compile(r'\bà\b.*\bétait\b')
]

patterns_gift = [
    re.compile(r'\bgagn[éeè]\b'),
    re.compile(r'\bcadeau\b'),
    re.compile(r'\bprix\b'),
    re.compile(r'\bloterie\b'),
    re.compile(r'\bfelicitation\b'),
    re.compile(r'\brécompense\b'),
    re.compile(r'\bgratuit\b'),
    re.compile(r'\bcliqu(ez|er)\b.*\blien\b'),
    re.compile(r'\bréclam(ez|er)\b'),
    re.compile(r'\bobten(ez|er)\b'),
    re.compile(r'\btirage au sort\b'),
    re.compile(r'\bheureux gagnant\b'),
]

patterns_paiement = [
    re.compile(r'\bpa(y|i)(ez|er|ement)\b'),
    re.compile(r'\bfrais\b'),
    re.compile(r'\bfacture\b'),
    re.compile(r'\brégl(ez|er)\b'),
    re.compile(r'\bdébloqu(ez|er)\b'),
    re.compile(r'\bsuspend(u|re)\b.*\bcompte\b'),
    re.compile(r'\bmaintenir.*\bcompte\b'),
    re.compile(r'\bactiv(ez|er).*\bcompte\b'),
    re.compile(r'\b\d+[€$£]\b.*\b(urgent|immédiat|maintenant)\b'),
    re.compile(r'\bamende\b'),
    re.compile(r'\bpr(eéè)l(éeè)vement\b'),
    re.compile(r'contravention')
]

patterns_colis = [
    re.compile(r'\bcolis\b'),
    re.compile(r'\blivraison\b.*\bpay'),
]

patterns_info = [
    re.compile(r'\bRIB\b'),
    re.compile(r'\bIBAN\b'),
    re.compile(r'\bcarte bancaire\b'),
    re.compile(r'\bcode\b.*\bcarte\b'),
    re.compile(r'\bcode secret\b'),
    re.compile(r'\bPIN\b'),
    re.compile(r'\bCVV\b'),
    re.compile(r'\bcryptogramme\b'),
    re.compile(r'\bidentifiant\b'),
    re.compile(r'\bmot de passe\b'),
    re.compile(r'\b2FA\b'),
    re.compile(r'\bOTP\b'),
    re.compile(r'\bcarte d.identit[ée]\b'),
    re.compile(r'\bpasseport\b'),
    re.compile(r'\bpièce d.identité\b'),
    re.compile(r'\bconfirm(ez|er).*\b(identité|compte|informations)\b'),
    re.compile(r'\bverifi(ez|er).*\b(identité|compte)\b'),
    re.compile(r'\bmettre à jour.*\b(coordonnées|informations)\b'),
]

def check_pattern(pattern, text):
    for p in pattern:
        if p.search(text, re.IGNORECASE):
            return True
    return False

def check_all_patterns(text):
    text = text.lower()
    if check_pattern(patterns_paiement, text):
        return json_message['paiement_inattendu']['long']
    if check_pattern(patterns_colis, text):
        return json_message['colis']['long']
    if check_pattern(patterns_info, text):
        return json_message['demande_infos']['long']
    if check_pattern(patterns_gift, text):
        return json_message['email_suspect']['long']
    if check_pattern(patterns_ortho, text):
        return json_message['faute_orthographe']['long']
    return None

if __name__ == "__main__":
    text =   "OrangeF 15:13 XOX al sl QD\n\u20ac 07 54 86 39 35 SS:\n\ns+) Enregistrer 07 54 86 39 35 ? x\n\nSi vous enregistrez ce num\u00e9ro, un\ncontact sera cr\u00e9\u00e9.\n\nSignaler comme spam Ajouter le contact\n\nEchange de SMS/MMS avec 07 54 86 39 35\n\nNon lus\n\n[Credit Mutuel] - QS\nGI Un d\u00e9bit de 1 446,28\n\nEUR est actuellement en cours\nsur votre espace, si vous n\u2019etes\npas a l\u2019origine de cette\nop\u00e9ration, veuillez\nimm\u00e9diatement contacter le\nservice d\u2019opposition au\n0189621294\n\n15:10 \u00ab Orange F\n\nOk merci Ok Ok merci beaucoup Parfai\n@\u00ae Message \u00a9 & th\n\nI O <\n"
    print(check_all_patterns(text))