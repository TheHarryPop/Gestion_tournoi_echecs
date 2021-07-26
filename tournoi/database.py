from tinydb import TinyDB
from tinydb import Query


class DataBase:
    def __init__(self):
        self.db = TinyDB("tournoi/Database.json")
        self.tournament_table = self.db.table("Tournaments")
        self.player_table = self.db.table("Players")

    def save_tournament(self, serialized_tournament):
        self.tournament_table.insert(serialized_tournament)

    def save_player(self, serialized_player):
        self.player_table.insert(serialized_player)

    def get_player_by_name(self, name):
        player = Query()
        test = self.player_table.search(player.name == str(name))
        print(test)


if __name__ == "__main__":
    database = DataBase()
    print("Database crée/chargée")
    database.get_player_by_name("Catherine")
