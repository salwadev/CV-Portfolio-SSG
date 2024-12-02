# CV/Portfolio avec Pelican et Docker

Un site web statique élégant combinant CV et Portfolio, construit avec Pelican et déployé via Docker.

## 🚀 Fonctionnalités

- 📱 Design responsive
- 🌓 Mode sombre/clair
- ✨ Animations fluides
- 📊 Portfolio interactif
- 🎨 Design moderne
- 🔄 Hot reload en développement



## 🛠️ Installation

1. Clonez le repository

```bash
git clone https://github.com/salwadev/CV-Portfolio-SSG.git
cd cv-portfolio
```
## 📁 Structure du Projet

```
.
├── content/
│   ├── pages/           # Contenu Markdown
│   │   ├── mon-cv.md
│   │   └── portfolio.md
│   └── images/          # Images
├── themes/
│   └── cv-theme/
│       ├── static/      # Assets
│       └── templates/   # Templates HTML
├── docker-compose.yml   # Configuration Docker
├── Dockerfile.dev       # Build développement
├── Dockerfile.prod      # Build production
└── pelicanconf.py      # Configuration Pelican
```

## 🔧 Configuration

### Pelican (`pelicanconf.py`)

```python
AUTHOR = 'Votre Nom'
SITENAME = 'Mon CV'
THEME = 'themes/cv-theme'
```

### Docker Compose

```yaml
services:
  dev:
    ports: "8000:8000"
    volumes: [...]
  prod:
    ports: "80:80"
```



## 🚀 Utilisation

### Mode Développement

```bash
docker-compose up dev
```
📝 Accès : http://localhost:8000
- Hot reload activé
- Modifications en temps réel
- Logs détaillés

### Mode Production

```bash
docker-compose up prod
```
🌐 Accès : http://localhost:80
- Version optimisée
- Servi via Nginx
- Performance maximale

## 📝 Personnalisation

### Contenu
1. Modifiez les fichiers Markdown dans `content/pages/`
2. Modifiez les images dans `content/images/`


### Style
1. Modifiez `themes/cv-theme/static/css/style.css`
2. Personnalisez les templates dans `themes/cv-theme/templates/`
2. Modifier le contenu dans `content/pages/`

```markdown
# Exemple mon-cv.md
Title: Mon CV
Template: cv
Image: images/profile.jpg
```

3. Personnalisez les styles dans `themes/cv-theme/static/css/`




