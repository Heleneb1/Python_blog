# Python_blog

# Mon Projet Django

## Description

Ce projet est une application web créée avec Django. Elle comprend une gestion des utilisateurs, des posts de blog et bien plus encore.

## Prérequis

Avant de pouvoir exécuter ce projet, assurez-vous d'avoir installé les éléments suivants :

- Python 3.x
- pip (gestionnaire de paquets Python)
- virtualenvwrapper

## Installation

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/ton-compte/nom-du-projet.git
   cd nom-du-projet
   ```

2. Créez et activez un environnement virtuel avec `virtualenvwrapper` :

   ```bash
   mkvirtualenv blog_env
   workon blog_env
   ```

3. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

4. Appliquez les migrations de la base de données :

   ```bash
   python manage.py migrate
   ```

5. Créez un superutilisateur pour accéder à l'admin Django :

   ```bash
   python manage.py createsuperuser
   ```

6. Lancez le serveur de développement :

   ```bash
   python manage.py runserver
   ```

7. Ouvrez votre navigateur et accédez à `http://127.0.0.1:8000/` pour voir votre application en action.

## Configuration

Ajoutez un fichier `.env` pour vos configurations spécifiques (par exemple, variables d'environnement, clés secrètes).

## Fonctionnalités

- Gestion des utilisateurs
- Création et gestion des posts de blog
- Interface d'administration
