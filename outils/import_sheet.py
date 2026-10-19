"""Importe les articles du Google Sheet « Veille technologique » (onglet Articles) dans veille.json.

Utilisation : python3 outils/import_sheet.py lignes.json
  lignes.json = les lignes de l'onglet Articles (A à I), en-tête compris, telles que renvoyées par Google Sheets :
  [["Date de publication","Thème","Source","Titre","Lien","Note","Raison de la note","Résumé","Date du passage"], [...], ...]

- Garde les traductions déjà faites (même lien).
- Les nouveaux articles ont leur résumé et leur raison en français ; il faut ensuite remplir en/ja/zh
  (la liste « À TRADUIRE » est affichée), puis lancer outils/synchro_veille.py.
"""
import json, os, sys, hashlib, re
from datetime import date

ICI = os.path.dirname(os.path.abspath(__file__))
FICHIER = os.path.join(os.path.dirname(ICI), "veille.json")
THEMES = {"ia": "ia", "cyber": "cyber", "dev/infra": "dev", "dev": "dev", "infra": "dev"}

lignes = json.load(open(sys.argv[1], encoding="utf-8"))
ancien = json.load(open(FICHIER, encoding="utf-8")) if os.path.exists(FICHIER) else {"articles": []}
par_lien = {a["url"]: a for a in ancien.get("articles", [])}
articles, a_traduire = [], []
for l in lignes[1:]:
    l = (l + [""] * 9)[:9]
    pub, theme, source, titre, lien, note, raison, resume = [str(x).strip() for x in l[:8]]
    topic = THEMES.get(theme.lower())
    if not topic or not lien.startswith("http") or not titre:
        continue
    lien = lien.replace("http://", "https://", 1) if lien.startswith("http://") else lien
    m = re.match(r"(\d{4}-\d{2}-\d{2})(?:[ T](\d{2}:\d{2}))?", pub)
    if not m:
        continue
    a = par_lien.get(lien) or {}
    art = {
        "id": topic + "-" + hashlib.sha1(lien.encode()).hexdigest()[:10],
        "topic": topic, "date": m.group(1), "time": m.group(2) or "", "source": source, "lang": "fr",
        "title": titre, "url": lien,
        "note": int(note) if note.isdigit() else None,
        "summary": dict(a.get("summary") or {}), "reason": dict(a.get("reason") or {}),
    }
    art["summary"]["fr"] = resume or art["summary"].get("fr", "")
    if raison:
        art["reason"]["fr"] = raison
    if any(not art["summary"].get(k) for k in ("en", "ja", "zh")) or (raison and any(not art["reason"].get(k) for k in ("en", "ja", "zh"))):
        a_traduire.append(art["id"])
    articles.append(art)

data = {"updated": date.today().isoformat(), "max_par_sujet": 10, "source": "Google Sheet « Veille technologique »", "articles": articles}
json.dump(data, open(FICHIER, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(articles), "article(s) importé(s)")
print("À TRADUIRE (summary et reason en en/ja/zh) :", ", ".join(a_traduire) if a_traduire else "aucun")
