# Gestion_tournoi_echecs

Ce programme python permet de gérer des tournois d'échecs selon le système suisse

## Installation et Lancement

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
- Seuls les joueurs enregistrés dans la base de données peuvent participer aux tournois
- Pour créer un nouveau tournoi, la base de données doit nécessairement contenir au minimum 8 joueurs
- A la création du tournoi, l'utilisateur sélectionnera les participants dans la base de données via leur nom de famille
- Le tournoi est automatiquement composé de 4 tours.
- Les matchs du premier tour sont automatiquement créés en fonction du niveau de chaque joueur
- Les matchs des tours suivants sont automatiquements créés en fonction du classement du tournoi



