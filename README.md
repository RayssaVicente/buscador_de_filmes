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


- git clone https://github.com/RayssaVicente/buscador_de_filmes.git

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

  ## Layout em Diferentes Dispositivos
  
1. **Notebook (tela: 1326 x 136)**
  ![Captura de Tela (827)](https://github.com/user-attachments/assets/ada955d2-f945-45b2-9009-026e0c34efdd)

2. **Ipad (tela: 575 x 767)**
  ![Captura de Tela (829)](https://github.com/user-attachments/assets/4e6fcd6e-7b12-44dc-a4d3-d0a6498eb551)
  ![Captura de Tela (828)](https://github.com/user-attachments/assets/ef1c3cee-1b80-4bc0-aef8-0ec139aaa0f5)

4. **Macbook Air(tela: 1559 x 975**
  ![Captura de Tela (835)](https://github.com/user-attachments/assets/7bd7a706-c725-4e9a-b604-e578faa5824c)
  ![Captura de Tela (836)](https://github.com/user-attachments/assets/50a48a92-bf96-4d09-8233-bb6f042eb39b)

6. **Iphone 14 Pro(tela: 379 x 872**
 

























