import os
from pathlib import Path

from django.core.wsgi import get_wsgi_application

# Define o caminho para o diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Define a configuração do ambiente para o Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

# Cria a aplicação WSGI
application = get_wsgi_application()
