AUTHOR = 'Hilali Salwa'
SITENAME = 'Mon CV'
SITEURL = 'http://localhost:8000'

PATH = 'content'
OUTPUT_PATH = 'output'

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'fr'

# Theme settings
THEME = 'themes/cv-theme'

# Ajoutez ces lignes
STATIC_PATHS = ['images', 'static']
EXTRA_PATH_METADATA = {
    'static/favicon.ico': {'path': 'favicon.ico'},
}

# Configuration des pages
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
DISPLAY_PAGES_ON_MENU = True

# Définir index.html comme page d'accueil
INDEX_SAVE_AS = 'blog.html'
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']

# Spécifier les templates
DIRECT_TEMPLATES = []  # Désactive les templates par défaut