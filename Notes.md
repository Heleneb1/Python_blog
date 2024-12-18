pour creer ce fichier python manage.py dumpdata posts.Post --indent 4 > posts_data.json

## Mise en place d'un fichier env et données à sécuriser

Étapes :
Créer le fichier .env :

À la racine du projet, crée un fichier nommé .env.
Ajoute-y la clé :
env

```
SECRET_KEY=ta_clé_secrète
```

Installer python-dotenv :

```
pip install python-dotenv
```

### Modifier settings.py :

Ajoute l'import et charge .env au début :
python

```
from dotenv import load_dotenv
import os
load_dotenv()
```

Remplace la ligne existante :
python

```
SECRET_KEY = os.getenv('SECRET_KEY')
```

Mettre à jour .gitignore :

Ajoute .env pour ne pas le versionner.
Mettre à jour requirements.txt :

```
pip freeze > requirements.txt
```

Tester le projet :

Relance le serveur pour vérifier que tout fonctionne.

```
python manage.py runserver
```
