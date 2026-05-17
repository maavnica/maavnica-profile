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
    portraits/           # SVG portraits
    style.css, app.js
```

## Ajouter un profil

1. Créer `backend/static/profile/data/mon-slug.json` (copier un JSON existant).
2. Optionnel : ajouter un portrait dans `portraits/`.
3. Ouvrir `/p/mon-slug`.

Le slug doit correspondre au nom du fichier (`^[a-z0-9-]+$`).

## CTA & liens (V0 démo)

- **E-mail** : `contact@maavnica.fr` (mailto fonctionnel).
- **WhatsApp / LinkedIn / Instagram / Behance** : liens de démonstration (info-bulle `title` sur les boutons concernés).
- **CV / book** : `cv-placeholder.pdf` (PDF minimal de démo).

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
