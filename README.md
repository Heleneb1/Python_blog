<p align="center">
  <img src="https://raw.githubusercontent.com/Heleneb1/blog/static/assets/banner.png" alt="Blog Banner" />
</p>

# HeleneB's Blog

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.1.2-green)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

## Table des matières

- [Description](#description)
- [Application déployée](#application-déployée)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Configuration](#configuration)
- [Fonctionnalités](#fonctionnalités)
- [Auteur](#auteur)

## Description

Cette application web est créée avec **Django**. Elle permet de gérer :

- Des utilisateurs
- Des posts de blog
- Des photos associées aux posts
- Une interface d’administration

C’est un espace d’exploration et de partage de mon apprentissage en Python et Django.

## Application déployée

[Helene's Blog sur PythonAnywhere](https://heleneb.pythonanywhere.com/)

## Prérequis

Avant de commencer, assurez-vous d’avoir installé :

- Python 3.x
- pip
- virtualenv ou virtualenvwrapper

## Installation

### En local (Windows)

1. **Cloner le dépôt :**

```bash
git clone https://github.com/Heleneb1/Python_blog.git
cd Python_blog
```

## Créer un environnement virtuel

```bash
python -m venv venv
```

## Activer l’environnement virtuel

```bash
source venv/Scripts/activate
```

Tu dois voir (venv) au début de ta ligne de commande.

## Installer les dépendances

```bash
pip install -r requirements.txt
```

## Appliquer les migrations

```bash
python manage.py migrate
```

## Créer un super-utilisateur

```bash
python manage.py createsuperuser
```

Suivre les instructions pour définir le nom d’utilisateur, l’email et le mot de passe

## Lancer le serveur de développement

```bash
python manage.py runserver
```

Puis ouvrir :
👉 http://127.0.0.1:8000/

## ☁️ Déploiement sur PythonAnywhere

### 1️⃣ Cloner le projet sur PythonAnywhere

```bash

git clone https://github.com/Heleneb1/blog.git
cd blog

```

### 2️⃣ Créer et activer un environnement virtuel

```bash
python3.10 -m venv venv
source venv/bin/activate
```

### 3️⃣ Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4️⃣ Migrations

```bash
python manage.py migrate
```

### 5️⃣ Collecte des fichiers statiques

```bash
python manage.py collectstatic
```

Répondre yes.

### 6️⃣ Configurer settings.py

Dans settings.py :

ALLOWED_HOSTS = [
"heleneb.pythonanywhere.com",
"localhost",
]

### 7️⃣ Configuration dans l’onglet “Web”

🔧 Choisir Python 3.10
🔧 Virtualenv :
/home/HeleneB/blog/venv

🔧 Fichier WSGI :
/home/HeleneB/blog/blog/wsgi.py

🔧 Static files :
URL Directory
/static/ /home/HeleneB/blog/static/

Puis cliquer Add.

### 8️⃣ Recharger l’app

Onglet Web → Reload.

## 📌 Fonctionnalités

Authentification utilisateurs

Création / édition / suppression de posts

Markdown converti en HTML

Upload d’images

Page d’administration Django

Gestion des contributeurs d’un post

## Déploiement PythonAnywhere

### 🗂 Structure du projet

```
blog/
│── posts/
│── medias/
│── users/
│── static/
│── templates/
│── blog/ (core project)
│── manage.py
```

### 🧑‍💻 Technologies

Python 3

Django 5

HTML / CSS

Markdown2

PythonAnywhere (déploiement)

## 👩‍💻 Auteur

**Helene**  
GitHub : [@Heleneb1](https://github.com/Heleneb1)

### 📄 Licence

Libre d’utilisation pour l’apprentissage.
