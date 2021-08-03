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
            rounds = tournament["rounds"]
            tournament_list.append(rounds)
            players = tournament["players"]
            tournament_list.append(players)
            time_control = tournament["time control"]
            tournament_list.append(time_control)
            description = tournament["description"]
            tournament_list.append(description)
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


if __name__ == "__main__":
    database = DataBase()