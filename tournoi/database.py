from tinydb import TinyDB
from tinydb import Query


class DataBase:
    def __init__(self):
        # Pour lancer via main.py
        self.db = TinyDB("tournoi/Database.json")
        # Pour lancer via un fichier.py du répertoire /tournoi
        # self.db = TinyDB("Database.json")
        self.tournament_table = self.db.table("Tournaments")
        self.player_table = self.db.table("Players")

    def save_tournament(self, serialized_tournament):
        self.tournament_table.insert(serialized_tournament)

    def save_player(self, serialized_player):
        self.player_table.insert(serialized_player)

    def extract_tournaments_list(self):
        tournaments_list = []
        tournaments_table = self.tournament_table.all()
        for tournament in tournaments_table:
            tournament_list = []
            name = tournament["name"]
            tournament_list.append(name)
            place = tournament["place"]
            tournament_list.append(place)
            date = tournament["date"]
            tournament_list.append(date)
            turns = tournament["turns"]
            tournament_list.append(turns)
            players = tournament["players"]
            tournament_list.append(players)
            time_control = tournament["time control"]
            tournament_list.append(time_control)
            description = tournament["description"]
            tournament_list.append(description)
            ranking = tournament["ranking"]
            tournament_list.append(ranking)
            tournaments_list.append(tournament_list)
        return tournaments_list

    def extract_players_list(self):
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

    def update_tournament_table(self, item):
        self.tournament_table.update(item)

    def get_doc_id_by_player(self, surname):
        user = Query()
        try:
            player = self.player_table.get(user.surname == surname)
            player_id = player.doc_id
            return player_id
        except AttributeError:
            result = "error"
            return result

    def get_doc_id_by_name(self, name):
        search = Query()
        try:
            tournament = self.tournament_table.get(search.name == name)
            tournament_id = tournament.doc_id
            return tournament_id
        except AttributeError:
            result = "error"
            return result

    def get_player_by_doc_id(self, doc_id):
        player = self.player_table.get(doc_id=doc_id)
        return player

    def get_tournament_by_doc_id(self, doc_id):
        tournament = self.tournament_table.get(doc_id=doc_id)
        return tournament


if __name__ == "__main__":
    database = DataBase()