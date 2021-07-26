import tournoi.view as view
from tournoi.model import Tournament
from tournoi.model import Player
from tournoi.database import DataBase


class Controller:
    def __init__(self):
        self.view = view.View()
        self.database = DataBase()
        self.tournament = None
        self.players = []

    def user_choice(self):
        val = self.view.get_choices()
        if val == 1:
            self.new_player()
        elif val == 2:
            self.create_tournament()
        elif val == 3:
            self.search_player()
        elif val == 4:
            exit()

    def new_player(self):
        surname = self.view.get_player_surname()
        name = self.view.get_player_name()
        date_of_birth = self.view.get_player_date_of_birth()
        sex = self.view.get_player_sex()
        ranking = self.view.get_player_rank()
        player = Player(surname, name, date_of_birth, sex, ranking)
        serialized_player = player.serialized_player()
        self.players.append(serialized_player)
        self.database.save_player(serialized_player)
        return self.user_choice()

    def create_tournament(self):
        if len(self.database.player_table) < 8:
            print("La base de données doit contenir au moins 8 joueurs pour pouvoir créer un tournoi \n"
                  f"Pour le moment, elle en contient {len(self.database.player_table)}")
            return self.user_choice()
        else:
            name = self.view.get_tournament_name()
            place = self.view.get_tournament_place()
            date = self.view.get_tournament_date()
            time_control = self.view.get_tournament_time_control()
            description = self.view.get_tournament_description()
            number_of_rounds = self.view.get_tournament_number_of_rounds()
            if number_of_rounds != "":
                self.tournament = Tournament(name, place, date, time_control, description, number_of_rounds)
            else:
                self.tournament = Tournament(name, place, date, time_control, description)
            serialized_tournament = self.tournament.serialized_tournament()
            self.database.save_tournament(serialized_tournament)
            return self.user_choice()

    def search_player(self):
        pass


def main():
    controller = Controller()
    controller.new_player()


if __name__ == "__main__":
    main()
