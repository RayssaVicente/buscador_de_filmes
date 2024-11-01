# Buscador de Filmes

Este projeto é uma aplicação web de busca de filmes usando Django (Back-end) e JavaScript (Front-end). Os usuários podem pesquisar filmes e visualizar os resultados diretamente na página.

## Funcionalidades

- Campo de busca para filmes.
- Exibição dos resultados com título, imagem e ano do filme.
- Layout responsivo para desktop e dispositivos móveis.

## Pré-requisitos

- **Python 3.8+**
- **Django 4.0+**
- **Git**

## Instalação e Configuração

1. **Clone o repositório**:


- git clone https://github.com/RayssaVicente/django.git

- cd movieapi


2. **Crie um ambiente virtual**:

- python -m venv venv


3. ** Ative o ambiente virtual**:

**Windows:**

- venv\Scripts\activate

 **Mac/Linux:**

- source venv/bin/activate

4. ** Instale as dependências**:

- pip install -r requirements.txt


##  Configuração do Django:

- No arquivo settings.py, certifique-se de que as seguintes configurações estão definidas:

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

##  Como Rodar o Projeto:

1. **Iniciar o Back-end (Django)**:

Execute os comandos abaixo no diretório principal do projeto:

1. **Realize as migrações do banco de dados:**

- python manage.py migrate

2. **Inicie o servidor de desenvolvimento do Django:**

- python manage.py runserver


2.** Configuração do Front-end**

- Arquivos Estáticos (CSS e JavaScript): Verifique se os arquivos style.css e script.js estão localizados em static/movies/.


## Resolução de Problemas

1. **Erro 404ao carregar arquivos estáticos:**

- Verifique se o caminho dos arquivos está correto no HTML: {% static 'movies/style.css' %}

- Confirme se STATICFILES_DIRSestá configurado em settings.py


2. **Erro ImproperlyConfiguredparaSTATIC_ROOT:**

- Adicione STATIC_ROOTno settings.py, por exemplo:

  STATIC_ROOT = BASE_DIR / 'staticfiles'

3. **Problema ao procurar filmes:**

- Verifique se uma view filmes_lista retorna JSON corretamente.

- se de que a função JavaScript fetchMovies está sendo chamada após o clique no botão de busca.























