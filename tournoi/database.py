from tinydb import TinyDB
from tinydb import Query


class DataBase:
    """Permet de créer un objet Database. S'il n'existe pas encore, un Database.json est créé dans le répertoire
    tournoi. Les tables Tournaments et Players sont associées à des variables"""

    def __init__(self):
        self.db = TinyDB("tournoi/Database.json")
        self.tournament_table = self.db.table("Tournaments")
        self.current_tournament = None
        self.player_table = self.db.table("Players")

    def save_tournament(self, serialized_tournament):
        """Sauvegarde un tournoi sur le Database.json"""
        self.tournament_table.insert(serialized_tournament)

    def save_player(self, serialized_player):
        """Sauvegarde un joueur sur le Database.json"""
        self.player_table.insert(serialized_player)

    def extract_tournaments_names_list(self):
        """Extrait les noms de tous les tournois enregistrés dans le Database.json"""
        tournaments_names_list = []
        tournaments_table = self.tournament_table.all()
        for tournament in tournaments_table:
            name = tournament["name"]
            tournaments_names_list.append(name)
        return tournaments_names_list

    def extract_players_list(self):
        """Extrait les noms de tous les joueurs enregistrés dans le Database.json"""
        players_list = []
        players_table = self.player_table.all()
        for player in players_table:
            player_list = []
            surname = player["surname"]
            player_list.append(surname)
            name = player["name"]
            player_list.append(name)
            date_of_birth = player["date_of_birth"]
            player_list.append(date_of_birth)
            sex = player["sex"]
            player_list.append(sex)
            ranking = player["ranking"]
            player_list.append(ranking)
            players_list.append(player_list)
        return players_list

    def update_tournament_table(self, item, doc_id):
        """Mets à jour la table de tournoi en cours d'utilisation"""
        self.current_tournament.update(item)
        self.tournament_table.update(self.current_tournament, doc_ids=[doc_id])

    def get_doc_id_by_player(self, surname):
        """Extrait le doc_id d'un joueur en procédant à une recherche par nom dans le Database.json"""
        user = Query()
        try:
            player = self.player_table.get(user.surname == surname)
            player_id = player.doc_id
            return player_id
        except AttributeError:
            return None

    def get_doc_id_by_name(self, name):
        """Extrait le doc_id d'un tournoi en procédant à une recherche par nom dans le Database.json"""
        search = Query()
        try:
            tournament = self.tournament_table.get(search.name == name)
            tournament_id = tournament.doc_id
            return tournament_id
        except AttributeError:
            return None

    def get_player_by_doc_id(self, doc_id):
        """Extrait les données d'un joueur enregistré en procédant à une recherche par doc_id dans le Database.json"""
        player = self.player_table.get(doc_id=doc_id)
        return player

    def get_tournament_by_doc_id(self, doc_id):
        """Extrait les données d'un tournoi enregistré en procédant à une recherche par doc_id dans le Database.json"""
        tournament = self.tournament_table.get(doc_id=doc_id)
        return tournament


if __name__ == "__main__":
    pass
