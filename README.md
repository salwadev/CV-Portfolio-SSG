# CV/Portfolio avec Pelican et Docker

 un site web statique contenant un CV (type vitrine) en utilisant Pelican comme générateur de site statique et Docker pour gérer les phases de développement, de build et de run.

## 🚀 Fonctionnalités

- 📄  Personnalisation facile via Markdown (CV et Portfolio)
- 🔄 Hot reload en développement (Prévisualisation instantanée en temps réel)
- ✨ Configuration flexible via Pelican (Variables et Publication)
- 📊 Optimisation des performances (Génération de fichiers HTML statiques optimisés)


## 🛠️ Installation

1. Clonez le repository

```bash
git clone https://github.com/salwadev/CV-Portfolio-SSG.git
cd CV-Portfolio-SSG
```
## 📁 Structure du Projet

```
.
├── content/
│   ├── pages/           # Contenu Markdown (CV et Portfolio)
│   │   ├── mon-cv.md
│   │   └── portfolio.md
│   └── images/          # Images
├── themes/
│   └── cv-theme/
│       ├── static/      # Assets CSS, JS, images
│       └── templates/   # Templates HTML 
├── docker-compose.yml   # Configuration Docker (dev et prod)
├── Dockerfile.dev       # Build développement (hot reload)
├── Dockerfile.prod      # Build production (optimisé)
├── nginx.conf           # Configuration Nginx
├── pelicanconf.py       # Configuration Pelican (variables)
├── publishconf.py      # Configuration Pelican (publication)
└── requirements.txt    # Liste des dépendances (Python)

```

## 🔧 Configuration

### Pelican (`pelicanconf.py`)

```python
AUTHOR = 'Full Name'
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


## 📧 Contact
Hilali Salwa - [@salwaHilali](https://www.linkedin.com/in/salwa-hleli-806905113/)


