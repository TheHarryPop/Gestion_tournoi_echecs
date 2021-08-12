# Gestion_tournoi_echecs

Ce programme python permet de gérer des tournois d'échecs selon le système suisse

## Installation et Lancement

### Installation de python

Suivez les instruction d'installation de python en suivant le lien https://www.python.org/

### Installation environnement et requirements

Utiliser les commandes suivantes pour créer un environnement, installer les requirements puis pour lancer l'exécution du programme :

```bash
$ git clone https://github.com/TheHarryPop/Gestion_tournoi_echecs.git
$ cd Gestion_tournoi_echecs
$ python3 -m venv env (Sous Windows => python -m venv env)
$ source env/bin/activate (Sous Windows => env\Scripts\activate)
$ pip install -r requirements.txt
$ python main.py
```

## Usage

### Contexte d'utilisation

- Commencer par insérer des joueurs dans la base de données.
- Seuls les joueurs enregistrés dans la base de données peuvent participer aux tournois.
- Pour créer un nouveau tournoi, la base de données doit nécessairement contenir au minimum 8 joueurs.
- A la création du tournoi, l'utilisateur sélectionne les participants dans la base de données via leur nom de famille.
- Le tournoi est automatiquement composé de 4 tours.
- Les matchs du premier tour sont automatiquement créés en fonction du niveau de chaque joueur
- Les matchs des tours suivants sont automatiquements créés en fonction du classement du tournoi
- Différentes statistiques sont consultables suivant les données enregistrées :
	- Dans le menu principal :
		- La liste des tournois enregistrés dans la base de données
		- La liste des joueurs enregistrés dans la base de données (par ordre alphabétique et par classement personnel)
	- Dans le menu de gestion d'un tournoi :
		- La liste des joueurs qui participent à un tournoi (par ordre alphabétique et par classement personnel)
		- La liste des tours d'un tournoi
		- La liste des matchs d'un tour en cours
		- La liste des matchs d'un tour passé
		- Le classement d'un tournoi

### Menu principal

- tapez 1 pour créer un joueur
- tapez 2 pour créer un tournoi
- tapez 3 pour afficher la liste des tournois enregistrés
- tapez 4 pour afficher la liste par ordre alphabétique les joueurs enregistrés
- tapez 5 pour afficher la liste par ordre de classement les joueurs enregistrés
- tapez 6 pour charger un tournoi déjà créé
- tapez 7 pour accéder au menu du tournoi
- tapez 8 pour quitter l'application

### Menu de gestion d'un tournoi

- tapez 1 pour créer un nouveau tour
- tapez 2 pour afficher la liste par ordre alphabétique des joueurs du tournoi
- tapez 3 pour afficher la liste par classement personnel des joueurs du tournoi
- tapez 4 pour afficher la liste des tours du tournoi
- tapez 5 pour afficher les matchs du tour en cours
- tapez 6 pour afficher les matchs joués
- tapez 7 pour renseigner les scores
- tapez 8 pour afficher le classement
- tapez 9 pour revenir au menu principal
- tapez 10 pour quitter l'application

## PEP8

### flake8

Utiliser la commande suivante pour créer un rapport d'erreurs flake8-html qui sera publié dans le répertoire flake8-report

```bash
flake8 --max-line-length 119 --format html --htmldir flake8-report --exclude .git,__pycache__,env -v
```