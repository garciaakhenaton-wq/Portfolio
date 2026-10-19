# Portfolio — GARCIA Akhenaton · BTS SIO SLAM

Portfolio personnel réalisé pendant mon BTS SIO option SLAM à NEXA, en travaillant avec une IA.
Thème spatial en 3D : une planète qui change (Mars, Terre, Vénus, Jupiter), des astéroïdes qui explosent au contact du curseur, et un vaisseau qui accompagne la visite.

👉 **Voir le site :** https://garciaakhenaton-wq.github.io/portfolio/ *(une fois GitHub Pages activé, voir plus bas)*

## Contenu

| Partie | Ce qu'on y trouve |
| --- | --- |
| Accueil | Présentation et planète 3D interactive (clic = cratère) |
| À propos | Mon parcours : un vaisseau voyage d'étape en étape quand on fait défiler la page, et mon CV à télécharger |
| Compétences | HTML, CSS, terminal, machine virtuelle, IA : chaque carte ouvre une petite fenêtre interactive (éditeur HTML en direct, réglages CSS, mini-terminal, configurateur de VM, démo IA) |
| Projets | Ma première page web, création d'un réseau LAN, ce portfolio |
| Veille technologique | Mission spatiale vers la Terre : chaque point du globe est un article de veille sur mes deux sujets (prix de la RAM et IA, AI Act européen), avec un grand écran de présentation |
| Contact | E-mail et LinkedIn |

Le site est disponible en **4 langues** (français, anglais, japonais, chinois) et en **mode jour / nuit**.

## Veille automatique

Les articles affichés sur la Terre sont dans [`veille.json`](veille.json) : **10 articles au maximum par sujet**.
Chaque semaine, une tâche programmée cherche les nouveaux articles, les ajoute (titre, source, date, lien et résumé en 4 langues)
et remplace les plus anciens quand un sujet en a déjà 10. Le script [`outils/synchro_veille.py`](outils/synchro_veille.py)
vérifie le fichier, applique la limite et met à jour la copie de secours dans `index.html`.

## Technologies

- **HTML et CSS** (commentés), dans un seul fichier `index.html`
- **JavaScript** sans framework
- **Three.js r128** pour la 3D (planètes générées par shaders, vaisseau modélisé en code)
- Accessibilité : navigation au clavier, version sans 3D si l'appareil ne la supporte pas ou si les animations sont réduites

## Lancer le site

Aucune installation : ouvrir `index.html` dans un navigateur récent (une connexion Internet est nécessaire pour charger Three.js et les polices).

## Mettre le site en ligne avec GitHub Pages

1. Dans ce dépôt : **Settings → Pages**
2. **Source** : *Deploy from a branch*, branche `main`, dossier `/ (root)`, puis **Save**
3. Après une ou deux minutes, le site est en ligne à l'adresse `https://garciaakhenaton-wq.github.io/portfolio/`

## Auteur

**GARCIA Akhenaton** — étudiant en BTS SIO option SLAM à NEXA
garcia.akhenaton@outlook.com
