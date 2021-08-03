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
```python
def extract_cat():
```
Cette fonction liste les différentes pages de catégories de livres

```python
def extract_books(links_cat):
```
Cette fonction liste tous les livres présents dans les catégories

```python
def extract_data(links_books, cat):
```
Cette fonction créer un fichier .CSV pour chaque catégorie dans lequel on trouve le détail suivant pour chaque livre :

Le délimiteur utilisé est un pipe : |
- product_page_url
- universal_product_code 
- title
- price_including_tax
- price_excluding_tax
- number_available
- product_description
- category
- review_rating
- image_url

L'image de chaque livre est elle aussi téléchargée et insérée dans un dossier Images



