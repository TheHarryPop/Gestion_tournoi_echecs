import tournoi.view as view


class Tournament:

    def __init__(self, name, place, date, time_control, description, number_of_rounds=4):
        self.name = name
        self.place = place
        self.date = date
        self.time_control = time_control
        self.description = description
        self.number_of_rounds = number_of_rounds
        self.players = []
        self.tours = []

    def add_player(self, player):
        self.players.append(player)

    def add_tour(self):
        self.tours.append(Tour.create_list_tour())

    def serialized_tournament(self):
        tournament = {"name": self.name, "place": self.place, "date": self.date, "tour": self.tours,
                      "player": self.players, "time control": self.time_control, "description": self.description,
                      "number of rounds": self.number_of_rounds}
        return tournament


class Player:

    def __init__(self, surname, name, date_of_birth, sex, ranking):
        self.surname = surname
        self.name = name
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.ranking = ranking

    def serialized_player(self):
        player = {"surname": self.surname, "name": self.name, "date_of_birth": self.date_of_birth, "sex": self.sex,
                  "ranking": self.ranking}
        return player


class Tour:

    def __init__(self):
        self.tour = []

    def create_list_tour(self):
        self.tour.append(Match.pair_of_players())
        return self.tour


class Match:
    """Un match consiste en une paire de joueurs avec un champ de résultat pour chaque joueur.
    Un match doit être stocké sous forme de tuple contenant deux listes qui contiennent deux éléments.
    Une référence à une instance de joueur et un score"""
    def __init__(self, player_id_1, player_id_2):
        self.player_id_1 = player_id_1
        self.player_id_2 = player_id_2
        self.player_1 = []
        self.player_2 = []

    def pair_of_players(self):
        self.player_1 = [self.player_id_1]
        self.player_2 = [self.player_id_2]
        paire_of_players = (self.player_1, self.player_2)
        return paire_of_players

    def add_result(self):
        self.player_1.append(view.request_score_player_1())
        self.player_2.append(view.request_score_player_2())
        match_score = (self.player_1, self.player_2)
        return match_score


def main():
    pass


if __name__ == "__main__":
    main()
