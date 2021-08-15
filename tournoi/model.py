class Tournament:
    """Permet créer un objet Tournament qui s'enregistre automatiquement dans la Database. L'instance d'un tournoi
    nécessite que l'utilisateur renseigne un nom, un lieu, une date, une méthode de contrôle de temps et 8 joueurs
    déjà enregistrés dans la Database. Le nombre de tours est instauré par défaut à 4. Les instances de Turn seront
    stockées dans la liste turns, les informations nécessaires à établir un classement seront stockées dans la liste
    ranking, la liste pairing_manager va contenir des informations permettant de ne pas créer des matchs déjà joués"""

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
        self.pairing_manager = []

    def serialized_tournament(self):
        tournament = {"name": self.name, "place": self.place, "date": self.date, "turns": self.turns,
                      "players": self.players, "time control": self.time_control, "description": self.description,
                      "number of rounds": self.number_of_rounds, "ranking": self.ranking,
                      "pairing manager": self.pairing_manager}
        return tournament


class Player:
    """Permet de créer un objet Player qui sera automatiquement enregistré dans la Database. L'instance d'un joueur
    doit contenir au moins le nom de famille, le prénom, la date de naissance, son sexe et son classement"""

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
    """Permet de créer un objet Turn qui s'intègre à la liste des tours du tournoi en cours puis enregistré dans la
    Database. L'instance d'un tour doit contenir un champ de nom, un champ Date et heure de début et un champ Date
    et heure de fin, ainsi que la liste des matchs de ce tour. Toutes ces données sont renseignées automatiquement"""

    def __init__(self, name, turn_matches, start_date_time):
        self.name = name
        self.turn_matches = turn_matches
        self.start_date_time = start_date_time
        self.end_date_time = None

    def turn_list(self):
        turn = [self.name, self.turn_matches, self.start_date_time, self.end_date_time]
        return turn


class Match:
    """Permet de créer un objet Match qui continent les noms des joueurs et leur champ de résultat respectif. Un
    match est stocké sous forme de tuple contenant deux listes qui contiennent deux éléments : Un nom de joueur et
    son score => match = ([name, score],[name, score]). Ce tuple au automatiquement inséré dans le tour auquel il
    appartient. Si le match n'est pas encore joué, la mention "Match a venir" est indiquée à la place du score"""

    def __init__(self, player_name_1, player_name_2):
        self.player_name_1 = player_name_1
        self.player_name_2 = player_name_2
        self.player_1_score = "Match a venir"
        self.player_2_score = "Match a venir"

    def match_tuple(self):
        match = ([self.player_name_1, self.player_1_score], [self.player_name_2, self.player_2_score])
        return match


if __name__ == "__main__":
    pass
