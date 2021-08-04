import datetime
from operator import itemgetter

import tournoi.view as view
from tournoi.model import Tournament
from tournoi.model import Player
from tournoi.model import Match
from tournoi.model import Turn
from tournoi.database import DataBase


class Controller:
    def __init__(self):
        self.view = view.View()
        self.database = DataBase()
        self.tournament = None

    def principal_user_choice(self):
        val = self.view.get_principal_choices()
        if val == 1:
            self.new_player()
        elif val == 2:
            self.create_tournament()
        elif val == 3:
            self.loading_process()
        elif val == 4:
            exit()

    def tournament_user_choice(self):
        val = self.view.get_tournament_choices()
        if val == 1:
            self.create_turn()
        elif val == 2:
            self.results()
        elif val == 3:
            pass
        elif val == 4:
            return self.principal_user_choice()
        elif val == 5:
            exit()

    def new_player(self):
        surname = self.view.get_player_surname()
        name = self.view.get_player_name()
        date_of_birth = self.view.get_player_date_of_birth()
        sex = self.view.get_player_sex()
        ranking = self.view.get_player_rank()
        player = Player(surname, name, date_of_birth, sex, ranking)
        serialized_player = player.serialized_player()
        self.database.save_player(serialized_player)
        return self.principal_user_choice()

    def create_tournament(self):
        if len(self.database.player_table) < 8:
            self.view.create_tournament_false(self.database.player_table)
            return self.principal_user_choice()
        else:
            name = self.view.get_tournament_name()
            place = self.view.get_tournament_place()
            date = self.view.get_tournament_date()
            time_control = self.view.get_tournament_time_control()
            description = self.view.get_tournament_description()
            self.tournament = Tournament(name, place, date, time_control, description)
            self.add_players()
            serialized_tournament = self.tournament.serialized_tournament()
            self.database.save_tournament(serialized_tournament)
            turn = self.create_turn()
            serialized_turn = turn.serialized_turn()
            self.tournament.turns.append(serialized_turn)
            self.database.update_tournament_table({"turns": serialized_turn})
            return self.tournament_user_choice()

    def loading_process(self):
        if self.database.tournament_table:
            tournament_list = self.database.extract_tournaments_list()
            self.load_tournament(tournament_list)
            self.view.ok_tournament_load()
            return self.tournament_user_choice()
        else:
            self.view.nok_tournament_load()
            return self.principal_user_choice()

    def load_tournament(self, tournaments_list):
        for data_tournament in tournaments_list:
            self.tournament = Tournament(name=data_tournament[0], place=data_tournament[1], date=data_tournament[2],
                                         time_control=data_tournament[5], description=data_tournament[6])
            self.tournament.turns.append(data_tournament[3])
            self.tournament.players = data_tournament[4]

    def add_players(self):
        players_list = self.database.extract_players_list()
        players_name_list = [player[0] for player in players_list]
        self.view.print_players_name_list(players_name_list)
        while len(self.tournament.players) != 8:
            tournament_players_name = [player["surname"] for player in self.tournament.players]
            self.view.number_of_players(self.tournament.players)
            name = self.view.get_name()
            while name not in players_name_list:
                self.view.error_name_in_list(name)
                name = self.view.get_name()
            if name in tournament_players_name:
                self.view.error_name_in_tournament(name)
            else:
                index = players_name_list.index(name)
                data_player = players_list[index]
                player = Player(surname=data_player[0], name=data_player[1], date_of_birth=data_player[2],
                                sex=data_player[3], ranking=int(data_player[4]))
                serialized_player = player.serialized_player()
                self.tournament.players.append(serialized_player)

    def create_turn(self):
        name = -1
        tournaments_table = self.database.tournament_table.all()
        for tournament in tournaments_table:
            turns = tournament["turns"]
            if len(turns) == 0:
                name = "Round 1"
                print(name)
            else:
                n = len(turns)+1
                name = f"Round {n}"
                print(name)

        # for tournament in tournaments_table:
        #     i = 0
        #     run = True
        #     turns = tournament["turns"]
        #     while run:
        #         try:
        #             turns[i]
        #             i += 1
        #         except IndexError:
        #             run = False
        #             i += 1
        #     name = f"Round {i}"
        now = datetime.datetime.now()
        start_date_time = f"Date et heure de debut : {now.strftime('%d/%m/%Y %H:%M:%S')}"
        turn_matches = self.make_1st_pair_of_players()
        turn = Turn(name, turn_matches, start_date_time)
        return turn

    def make_1st_pair_of_players(self):
        matches_list = []
        i = 0
        sorted_players = sorted(self.tournament.players, key=itemgetter("ranking"), reverse=False)
        for player in range(int(len(sorted_players)/2)):
            player_1 = sorted_players[0+i]
            player_2 = sorted_players[(int(len(sorted_players)/2))+i]
            match = Match(player_1.get("name"), player_2.get("name"))
            serialized_match = match.serialized_match()
            matches_list.append(serialized_match)
            i += 1
        return matches_list

    def results(self):
        if self.tournament.turns[0]:
            turn = self.tournament.turns[-1]
            match_list = turn[1]
            matches_tuples = []
            for duo in match_list:
                player_1 = duo[0]
                player_name_1 = player_1[0]
                player_2 = duo[1]
                player_name_2 = player_2[0]
                match = Match(player_name_1, player_name_2)
                match.player_1_score = self.view.get_score_player(match.player_name_1)
                match.player_2_score = self.view.get_score_player(match.player_name_2)
                matches_tuples.append(match.serialized_match())
            now = datetime.datetime.now()
            end_date_time = f"Date et heure de fin : {now.strftime('%d/%m/%Y %H:%M:%S')}"
            completed_turn = Turn(turn[0], matches_tuples, turn[2])
            completed_turn.end_date_time = end_date_time
            self.tournament.turns[-1] = completed_turn.serialized_turn()
            serialized_tournament = self.tournament.serialized_tournament()
            self.database.update_tournament_table(serialized_tournament)
            self.view.ok_turn_score()
            return self.tournament_user_choice()
        else:
            self.view.nok_turn_load()
            return self.tournament_user_choice()


if __name__ == "__main__":
    controller = Controller()
    controller.create_turn()
