# CV/Portfolio avec Pelican et Docker

Un site web statique élégant combinant CV et Portfolio, construit avec Pelican et déployé via Docker.

## 🚀 Fonctionnalités

- 📱 Design responsive
- 🌓 Mode sombre/clair
- ✨ Animations fluides
- 📊 Portfolio interactif
- 🎨 Design moderne
- 🔄 Hot reload en développement

## 📋 Prérequis

- Docker
- Docker Compose

## 🛠️ Installation

1. Clonez le repository

```bash
git clone https://github.com/votre-username/cv-portfolio.git
cd cv-portfolio
```

2. Créez votre contenu dans `content/pages/`

```markdown
# Exemple mon-cv.md
Title: Mon CV
Template: cv
Image: images/profile.jpg
```

3. Personnalisez les styles dans `themes/cv-theme/static/css/`

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

## 📝 Personnalisation

### Contenu
1. Modifiez les fichiers Markdown dans `content/pages/`
2. Ajoutez vos images dans `content/images/`
3. Créez de nouvelles pages selon vos besoins

### Style
1. Modifiez `themes/cv-theme/static/css/style.css`
2. Personnalisez les templates dans `themes/cv-theme/templates/`
3. Ajoutez vos propres assets dans `static/`

## 🔍 Dépannage

### Problèmes courants

1. Images non affichées

```bash
# Vérifiez les chemins
docker exec -it cv-prod-1 ls -R /usr/share/nginx/html/
```

2. CSS non chargé

```bash
# Reconstruisez les conteneurs
docker-compose down
docker-compose build --no-cache
docker-compose up
```

## 🤝 Contribution

1. Fork le projet
2. Créez votre branche (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📜 Licence

Distribué sous la licence MIT. Voir `LICENSE` pour plus d'informations.

## 📧 Contact

Votre Nom - [@votretwitter](https://twitter.com/votretwitter)

Lien du projet: [https://github.com/votre-username/cv-portfolio](https://github.com/votre-username/cv-portfolio)

## 🙏 Remerciements

- [Pelican](https://blog.getpelican.com/)
- [Docker](https://www.docker.com/)
- [Font Awesome](https://fontawesome.com/)