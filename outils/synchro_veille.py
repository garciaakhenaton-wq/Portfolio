"""Vérifie veille.json, garde au maximum 10 articles par sujet (les plus récents)
et recopie les données dans index.html (copie de secours quand le fichier ne peut pas être chargé).

Utilisation : python3 outils/synchro_veille.py
"""
import json, os, re, sys
from datetime import date

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
FICHIER = os.path.join(RACINE, "veille.json")
PAGE = os.path.join(RACINE, "index.html")
SUJETS = {"ram", "act"}            # sujets connus du site (textes de présentation dans index.html)
LANGUES = ("fr", "en", "ja", "zh")

data = json.load(open(FICHIER, encoding="utf-8"))
maxi = int(data.get("max_par_sujet", 10))
erreurs, vus = [], set()
for a in data["articles"]:
    ref = a.get("id", "?")
    for champ in ("id", "topic", "date", "source", "lang", "title", "url", "summary"):
        if not a.get(champ):
            erreurs.append(f"{ref} : champ « {champ} » manquant")
    if a.get("topic") not in SUJETS:
        erreurs.append(f"{ref} : sujet inconnu « {a.get('topic')} »")
    try:
        date.fromisoformat(a.get("date", ""))
    except ValueError:
        erreurs.append(f"{ref} : date invalide « {a.get('date')} » (format AAAA-MM-JJ)")
    if not str(a.get("url", "")).startswith("https://"):
        erreurs.append(f"{ref} : le lien doit commencer par https://")
    for l in LANGUES:
        if not (a.get("summary") or {}).get(l):
            erreurs.append(f"{ref} : résumé « {l} » manquant")
    if ref in vus or a.get("url") in vus:
        erreurs.append(f"{ref} : article en double")
    vus.update([ref, a.get("url")])
if erreurs:
    print("Erreurs dans veille.json :\n- " + "\n- ".join(erreurs))
    sys.exit(1)

# Au maximum `maxi` articles par sujet : les plus anciens sont remplacés par les nouveaux
gardes, retires = [], []
for s in sorted(SUJETS):
    liste = sorted([a for a in data["articles"] if a["topic"] == s], key=lambda a: a["date"], reverse=True)
    gardes += liste[:maxi]
    retires += liste[maxi:]
gardes.sort(key=lambda a: (a["date"], a["id"]), reverse=True)
data["articles"] = gardes
json.dump(data, open(FICHIER, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
open(FICHIER, "a", encoding="utf-8").write("\n")

# Copie de secours dans la page
page = open(PAGE, encoding="utf-8").read()
bloc = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
motif = re.compile(r'(<script type="application/json" id="veille-data">)(.*?)(</script>)', re.S)
if not motif.search(page):
    print("Bloc veille-data introuvable dans index.html"); sys.exit(1)
page = motif.sub(lambda m: m.group(1) + bloc + m.group(3), page, count=1)
open(PAGE, "w", encoding="utf-8").write(page)

for s in sorted(SUJETS):
    print(f"{s} : {sum(1 for a in gardes if a['topic'] == s)} article(s)")
for a in retires:
    print(f"retiré (plus ancien) : {a['date']} {a['source']} — {a['title']}")
print("veille.json et index.html synchronisés.")
