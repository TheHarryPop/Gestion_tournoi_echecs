class Tournament:

    def __init__(self, name, place, date, time_control, description, number_of_rounds=4):
        self.name = name
        self.place = place
        self.date = date
        self.time_control = time_control
        self.description = description
        self.number_of_rounds = number_of_rounds
        self.players = []
        self.turns = []
        self.ranking = []

    def serialized_tournament(self):
        tournament = {"name": self.name, "place": self.place, "date": self.date, "turns": self.turns,
                      "players": self.players, "time control": self.time_control, "description": self.description,
                      "number of rounds": self.number_of_rounds, "ranking": self.ranking}
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


class Turn:
    """chaque instance du tour doit contenir un champ de nom. Actuellement, nous appelons nos tours "Round 1", "Round 2"
    , etc. Elle doit également contenir un champ Date et heure de début et un champ Date et heure de fin, qui doivent
    tous deux être automatiquement remplis lorsque l'utilisateur crée un tour et le marque comme terminé. Les instances
    de round doivent être stockées dans une liste sur l'instance de tournoi à laquelle elles appartiennent."""

    def __init__(self, name, turn_matches, start_date_time):
        self.name = name
        self.turn_matches = turn_matches
        self.start_date_time = start_date_time
        self.end_date_time = None

    def serialized_turn(self):
        turn = [self.name, self.turn_matches, self.start_date_time, self.end_date_time]
        return turn


class Match:
    """Un match consiste en une paire de joueurs avec un champ de résultat pour chaque joueur.
    Un match doit être stocké sous forme de tuple contenant deux listes qui contiennent deux éléments.
    Une référence à une instance de joueur et un score => match = ([name, score],[name, score])"""
    def __init__(self, player_name_1, player_name_2):
        self.player_name_1 = player_name_1
        self.player_name_2 = player_name_2
        self.player_1_score = "Match a venir"
        self.player_2_score = "Match a venir"

    def match_tuple(self):
        match = ([self.player_name_1, self.player_1_score], [self.player_name_2, self.player_2_score])
        return match


def main():
    pass


if __name__ == "__main__":
    main()
