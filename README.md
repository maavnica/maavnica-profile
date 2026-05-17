# Maavnica Profile — V0

Profils professionnels vivants, compacts et partageables.  
**Sans base de données** : contenu en JSON local, rendu SSR avec FastAPI + Jinja2.

## Démarrage local

```bash
python -m pip install -r requirements.txt
python -m uvicorn backend.app.main:app --reload --port 8090
```

- Accueil : [http://127.0.0.1:8090/](http://127.0.0.1:8090/) → redirige vers `/p/arnaud`
- Santé : [http://127.0.0.1:8090/health](http://127.0.0.1:8090/health)

## Profils démo

| URL | Persona |
|-----|---------|
| `/p/arnaud` | Fondateur Maavnica — produit & relation client |
| `/p/justine` | Assistante polyvalente — accueil & organisation (présence humaine) |
| `/p/terapeuta` | Thérapeute bien-être (ES, LATAM) |
| `/p/designer` | Designer freelance |
| `/p/consultant` | Consultant organisation terrain |

## Structure

```
backend/
  app/
    main.py              # Routes FastAPI
    templates/           # SSR Jinja2
  static/profile/
    data/*.json          # Un fichier par slug
    portraits/           # SVG + photos (ex. justine.jpg)
    cv/                  # CV HTML/CSS + PDF (Justine)
    style.css, app.js
```

## Ajouter un profil

1. Créer `backend/static/profile/data/mon-slug.json` (copier un JSON existant).
2. Optionnel : ajouter un portrait dans `portraits/`.
3. Ouvrir `/p/mon-slug`.

Le slug doit correspondre au nom du fichier (`^[a-z0-9-]+$`).

Sections éditoriales (JSON) : `quotes`, `milestones` (style `narrative` sans dates), `signals` (signaux humains), `projects`, `availability`. Titres libres (« Parcours en clair », « Disponible pour », etc.).

## CTA & liens (V0 démo)

- **E-mail** : `contact@maavnica.fr` (mailto fonctionnel).
- **WhatsApp / LinkedIn / Instagram / Behance** : liens de démonstration (info-bulle `title` sur les boutons concernés).
- **CV / book** : `cv-placeholder.pdf` (PDF minimal de démo) ; profil **Justine** : CV dédié (voir ci-dessous).

## Profil Justine (V0.6) — photo & CV

Exemple complet : profil vivant sur `/p/justine`, CV en complément.

### Photo

1. Déposer la vraie photo (JPEG ou PNG) sous :
   `backend/static/profile/portraits/justine.jpg`
   (ou mettre à jour le champ `hero.portrait` dans `data/justine.json`).
2. Tant que le fichier est absent ou invalide, le navigateur bascule sur le fallback SVG :
   `portraits/justine-photo.svg` (via `portrait_fallback` dans le JSON).

### CV PDF

1. Ouvrir dans le navigateur (serveur local lancé) :
   [http://127.0.0.1:8090/static/profile/cv/justine-vaillard-cv.html](http://127.0.0.1:8090/static/profile/cv/justine-vaillard-cv.html)
2. **Imprimer** → **Enregistrer au format PDF** (format A4, marges par défaut ou minimales).
3. Remplacer le fichier :
   `backend/static/profile/cv/justine-vaillard-cv.pdf`

Le bouton **Voir le CV** du profil pointe vers ce PDF. Source HTML + styles :
`backend/static/profile/cv/justine-vaillard-cv.html` et `cv-style.css`.

## Déploiement Render

Fichier `render.yaml` inclus. Commande de démarrage :

```bash
uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT
```

Variables : aucune obligatoire pour la V0.

## Partage

- `navigator.share` si disponible (mobile).
- Sinon copie du lien dans le presse-papiers + message « Lien copié » / « Enlace copiado ».

## 404

`/p/inconnu` affiche une page sobre avec liens vers les profils démo.
