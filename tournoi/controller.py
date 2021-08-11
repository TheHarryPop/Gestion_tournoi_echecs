import datetime
import numpy as np
import pandas as pd

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
        """Affiche les différents choix d'actions du menu principal"""
        val = self.view.get_principal_choices()
        if val == 1:
            self.new_player()
        elif val == 2:
            self.create_tournament()
        elif val == 3:
            self.loading_process()
        elif val == 4:
            if not self.tournament:
                self.view.print_absence_tournament()
                return self.principal_user_choice()
            else:
                self.tournament_user_choice()
        elif val == 5:
            exit()

    def tournament_user_choice(self):
        """Affiche les différents choix d'actions du menu du tournoi chargé"""
        val = self.view.get_tournament_choices()
        if val == 1:
            if len(self.tournament.turns) < self.tournament.number_of_rounds:
                turn = self.tournament.turns[-1]
                if not turn[-1]:
                    self.view.scores_not_already_registered()
                else:
                    self.create_turn()
            else:
                self.view.maxi_turn_reached()
            return self.tournament_user_choice()
        elif val == 2:
            self.show_turn_matches()
        elif val == 3:
            self.show_played_matches()
        elif val == 4:
            self.add_results()
        elif val == 5:
            self.show_tournament_ranking()
        elif val == 6:
            self.principal_user_choice()
        elif val == 7:
            exit()

    def new_player(self):
        """Créer un nouveau joueur et l'enregistre dans la base de données"""
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
        """Créer un nouveau tournoi si la base de données contient au moins 8 joueurs"""
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
            for player in self.tournament.players:
                pairing_manager = {player: []}
                self.tournament.pairing_manager.append(pairing_manager)
            serialized_tournament = self.tournament.serialized_tournament()
            self.database.save_tournament(serialized_tournament)
            self.create_turn()
            return self.tournament_user_choice()

    def loading_process(self):
        """Affiche les différents tournois enregistrés dans la base de données"""
        if self.database.tournament_table:
            tournaments_names_list = self.database.extract_tournaments_names_list()
            self.load_tournament(tournaments_names_list)
            self.view.ok_tournament_load()
            return self.tournament_user_choice()
        else:
            self.view.nok_tournament_load()
            return self.principal_user_choice()

    def load_tournament(self, tournaments_names_list):
        """Charge le tournoi enregistré, sélectionné par l'utilisateur"""
        tournament_name = self.view.data_tournament(tournaments_names_list)
        while tournament_name not in tournaments_names_list:
            self.view.error_tournament_in_list(tournament_name)
            tournament_name = self.view.data_tournament(tournaments_names_list)
        tournament_id = self.database.get_doc_id_by_name(tournament_name)
        data_tournament = self.database.get_tournament_by_doc_id(tournament_id)

        self.tournament = Tournament(name=data_tournament["name"], place=data_tournament["place"],
                                     date=data_tournament["date"], time_control=data_tournament["time control"],
                                     description=data_tournament["description"])
        self.tournament.turns = data_tournament["turns"]
        self.tournament.players = data_tournament["players"]
        self.tournament.ranking = data_tournament["ranking"]
        self.tournament.pairing_manager = data_tournament["pairing manager"]

    def add_players(self):
        """Affiche les joueurs enregistrés dans la base de données puis les ajoute au tournoi après sélection par
        l'utilisateur"""
        players_list = self.database.extract_players_list()
        players_name_list = [each_player[0] for each_player in players_list]
        self.view.print_players_name_list(players_name_list)
        while len(self.tournament.players) != 8:
            tournament_players_name = self.tournament.players
            self.view.number_of_players(self.tournament.players)
            name = self.view.get_name()
            name_id = self.database.get_doc_id_by_player(name)
            while name not in players_name_list:
                self.view.error_name_in_list(name)
                name = self.view.get_name()
            if name_id in tournament_players_name:
                self.view.error_name_in_tournament(name)
            else:
                player_id = self.database.get_doc_id_by_player(name)
                self.tournament.players.append(player_id)
        for each_player in self.tournament.players:
            player_data = self.database.get_player_by_doc_id(each_player)
            player_dict = {"surname": player_data["surname"], "score": 0, "ranking": int(player_data["ranking"])}
            self.tournament.ranking.append(player_dict)

    def create_turn(self):
        """Créer un nouveau tour"""
        tournaments_table = self.database.tournament_table.all()
        name = -1
        turn_matches = -1
        for tournament in tournaments_table:
            turns = tournament["turns"]
            if not turns:
                name = "Round 1"
                turn_matches = self.make_1st_pair_of_players()
            else:
                name = f"Round {len(turns) + 1}"
                turn_matches = self.make_next_pair_of_players()
        now = datetime.datetime.now()
        start_date_time = f"Date et heure de debut : {now.strftime('%d/%m/%Y %H:%M:%S')}"
        turn = Turn(name, turn_matches, start_date_time)
        serialized_turn = turn.serialized_turn()
        self.tournament.turns.append(serialized_turn)
        self.database.update_tournament_table({"turns": self.tournament.turns})

    def make_1st_pair_of_players(self):
        """Créer les paires du premier tour en triant les joueurs par classement"""
        matches_list = []
        i = 0
        players_list = []
        for player_id in self.tournament.players:
            data_player = self.database.get_player_by_doc_id(player_id)
            player_object = Player(surname=data_player.get("surname"), name=data_player.get("name"),
                                   date_of_birth=data_player.get("date_of_birth"), sex=data_player.get("sex"),
                                   ranking=int(data_player.get("ranking")))
            serialized_player = player_object.serialized_player()
            players_list.append(serialized_player)
        sorted_players = sorted(players_list, key=lambda x: (-x["ranking"]))
        for each_player in range(int(len(sorted_players)/2)):
            player_1 = sorted_players[0+i]
            player_1_surname = player_1.get("surname")
            player_2 = sorted_players[(int(len(sorted_players)/2))+i]
            player_2_surname = player_2.get("surname")
            match = Match(player_1_surname, player_2_surname)
            player_1_id = self.database.get_doc_id_by_player(player_1_surname)
            player_2_id = self.database.get_doc_id_by_player(player_2_surname)
            for player in self.tournament.pairing_manager:
                for key, value in player.items():
                    if str(key) == str(player_1_id):
                        match_list = value
                        match_list.append(str(player_2_id))
                        player[key] = match_list
                    elif str(key) == str(player_2_id):
                        match_list = value
                        match_list.append(str(player_1_id))
                        player[key] = match_list
                    else:
                        pass
            serialized_match = match.match_tuple()
            matches_list.append(serialized_match)
            i += 1
        self.database.update_tournament_table({"pairing manager": self.tournament.pairing_manager})
        return matches_list

    # def make_next_pair_of_players(self):
    #     """Créer les paires des tours 2 à 4 en triant par score puis, en cas d'égalité, par classement personnel
    #     Si le joueur 1 de l'instance de Match à déjà rencontré le joueur 2, ce dernier sera remplacé par le joueur
    #     suivant"""
    #     new_matches = []
    #     id_in_turn = []
    #     i = 0
    #     match_list = []
    #     ranking = self.tournament.ranking
    #     sorted_players = sorted(ranking, key=lambda x: (-x["score"], -x["ranking"]))
    #     for each_player in range(int(len(sorted_players) / 2)):
    #         player_1 = sorted_players[0 + i]
    #         player_1_surname = player_1.get("surname")
    #         player_1_id = self.database.get_doc_id_by_player(player_1_surname)
    #         player_2 = sorted_players[1 + i]
    #         player_2_surname = player_2.get("surname")
    #         player_2_id = self.database.get_doc_id_by_player(player_2_surname)
    #         for player in self.tournament.pairing_manager:
    #             for key, value in player.items():
    #                 if key == str(player_1_id):
    #                     match_list = str(value)
    #         j = 1
    #
    #         while str(player_2_id) in match_list:
    #             player_2 = sorted_players[1 + i + j]
    #             player_2_surname = player_2.get("surname")
    #             player_2_id = self.database.get_doc_id_by_player(player_2_surname)
    #             j += 1
    #         match = Match(player_1_surname, player_2_surname)
    #         for player in self.tournament.pairing_manager:
    #             for key, value in player.items():
    #                 if str(key) == str(player_1_id):
    #                     match_list = value
    #                     match_list.append(str(player_2_id))
    #                     id_in_turn.append(str(player_2_id))
    #                     player[key] = match_list
    #                 elif str(key) == str(player_2_id):
    #                     match_list = value
    #                     match_list.append(str(player_1_id))
    #                     id_in_turn.append(str(player_1_id))
    #                     player[key] = match_list
    #                 else:
    #                     pass
    #         self.database.update_tournament_table({"pairing manager": self.tournament.pairing_manager})
    #         serialized_match = match.match_tuple()
    #         new_matches.append(serialized_match)
    #         i += 2
    #     return new_matches

    def make_next_pair_of_players(self):
        """Créer les paires des tours 2 à 4 en triant par score puis, en cas d'égalité, par classement personnel
        Si le joueur 1 de l'instance de Match à déjà rencontré le joueur 2, ce dernier sera remplacé par le joueur
        suivant"""
        new_matches = []
        id_in_turn = []
        i = 0
        match_list = []
        ranking = self.tournament.ranking
        sorted_players = sorted(ranking, key=lambda x: (-x["score"], -x["ranking"]))
        for each_player in range(int(len(sorted_players) / 2)):
            player_1 = sorted_players[0 + i]
            player_1_surname = player_1.get("surname")
            player_1_id = self.database.get_doc_id_by_player(player_1_surname)
            while str(player_1_id) in id_in_turn:
                print("là")
                i += 1
                player_1 = sorted_players[0 + i]
                player_1_surname = player_1.get("surname")
                player_1_id = self.database.get_doc_id_by_player(player_1_surname)
            player_2 = sorted_players[1 + i]
            player_2_surname = player_2.get("surname")
            player_2_id = self.database.get_doc_id_by_player(player_2_surname)
            for player in self.tournament.pairing_manager:
                for key, value in player.items():
                    if key == str(player_1_id):
                        match_list = str(value)
                        print(match_list)
            j = 1
            raz = False
            while str(player_2_id) in id_in_turn or str(player_2_id) in match_list:
                print("ici")
                player_2 = sorted_players[1 + i + j]
                player_2_surname = player_2.get("surname")
                player_2_id = self.database.get_doc_id_by_player(player_2_surname)
                raz = True
                j += 1
            if raz:
                i -= 1

            print(player_1_surname)
            print(player_2_surname)

            match = Match(player_1_surname, player_2_surname)
            for player in self.tournament.pairing_manager:
                for key, value in player.items():
                    if str(key) == str(player_1_id):
                        match_list = value
                        match_list.append(str(player_2_id))
                        id_in_turn.append(str(player_2_id))
                        player[key] = match_list
                    elif str(key) == str(player_2_id):
                        match_list = value
                        match_list.append(str(player_1_id))
                        id_in_turn.append(str(player_1_id))
                        player[key] = match_list
                    else:
                        pass
            self.database.update_tournament_table({"pairing manager": self.tournament.pairing_manager})
            serialized_match = match.match_tuple()
            new_matches.append(serialized_match)
            i += 2
        return new_matches

    def add_results(self):
        """Ajoute les scores de chaque joueur du tour en cours"""
        turn = self.tournament.turns[-1]
        match_list = turn[1]
        matches_tuples = []
        for duo in match_list:
            player_1 = duo[0]
            if player_1[1] == "Match a venir":
                player_name_1 = player_1[0]
                player_2 = duo[1]
                player_name_2 = player_2[0]
                match = Match(player_name_1, player_name_2)
                match.player_1_score = self.view.get_score_player(match.player_name_1)
                if match.player_1_score == 1.0:
                    match.player_2_score = 0.0
                elif match.player_1_score == 0.0:
                    match.player_2_score = 1.0
                else:
                    match.player_2_score = 0.5
                for each_player in self.tournament.ranking:
                    if each_player["surname"] == player_name_1:
                        score = float(each_player["score"])
                        each_player["score"] = score + match.player_1_score
                    elif each_player["surname"] == player_name_2:
                        score = float(each_player["score"])
                        each_player["score"] = score + match.player_2_score
                    else:
                        pass
                matches_tuples.append(match.match_tuple())
            else:
                self.view.scores_already_registered()
                return self.tournament_user_choice()
        now = datetime.datetime.now()
        end_date_time = f"Date et heure de fin : {now.strftime('%d/%m/%Y %H:%M:%S')}"
        completed_turn = Turn(turn[0], matches_tuples, turn[2])
        completed_turn.end_date_time = end_date_time
        self.tournament.turns[-1] = completed_turn.serialized_turn()
        serialized_tournament = self.tournament.serialized_tournament()
        self.database.update_tournament_table(serialized_tournament)
        self.view.ok_turn_score()
        return self.tournament_user_choice()

    def show_tournament_ranking(self):
        """Affiche le classement actuel du tournoi en triant par score , puis par rang en cas d'égalité"""
        ranking = self.tournament.ranking
        sorted_players = sorted(ranking, key=lambda x: (-x["score"], -x["ranking"]))
        surnames = []
        total_statistics = []
        for each_player in sorted_players:
            surname = [each_player.get("surname")]
            surnames.append(surname)
            statistics = [each_player.get("score"), each_player.get("ranking")]
            total_statistics.append(statistics)
        tournament_ranking_numpy = np.array(total_statistics)
        index_value = []
        for surname in surnames:
            value = surname[0]
            index_value.append(value)
        tournament_ranking_df = pd.DataFrame(tournament_ranking_numpy, index=[index_value],
                                             columns=["score", "ranking"])
        self.view.print_tournament_ranking(tournament_ranking_df)
        return self.tournament_user_choice()

    def show_turn_matches(self):
        turns_names = [data[0] for data in self.tournament.turns]
        turns_matches = [data[1] for data in self.tournament.turns]
        first_match = [turn_matches[1] for turn_matches in turns_matches]
        player_1 = [player[0] for player in first_match]
        n = 0
        for player in player_1:
            if player[1] == "Match a venir":
                self.view.print_played_matches(turns_names[player_1.index(player)],
                                               turns_matches[player_1.index(player)])
                n += 1
        if n == 0:
            if len(self.tournament.turns) == self.tournament.number_of_rounds:
                self.view.maxi_turn_reached()
            else:
                self.view.need_new_turn()
        return self.tournament_user_choice()

    def show_played_matches(self):
        turns_names = [data[0] for data in self.tournament.turns]
        turns_matches = [data[1] for data in self.tournament.turns]
        first_match = [turn_matches[1] for turn_matches in turns_matches]
        player_1 = [player[0] for player in first_match]
        for player in player_1:
            if player[1] != "Match a venir":
                self.view.print_played_matches(turns_names[player_1.index(player)],
                                               turns_matches[player_1.index(player)])
        return self.tournament_user_choice()


if __name__ == "__main__":
    pass
