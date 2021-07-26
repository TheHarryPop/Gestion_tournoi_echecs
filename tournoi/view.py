import datetime


class View:

    @staticmethod
    def get_choices():
        test = 0
        choice = -1
        while test == 0:
            request = input("Quelle action souhaitez vous réaliser ? \n"
                            "tapez 1 pour créer un joueur \n"
                            "tapez 2 pour créer un tournoi \n"
                            "tapez 3 pour rechercher un joueur existant \n"
                            "tapez 4 pour quitter l'application ")
            try:
                test = int(request) + 1
                if int(request) == 1:
                    choice = 1
                elif int(request) == 2:
                    choice = 2
                elif int(request) == 3:
                    choice = 3
                elif int(request) == 4:
                    choice = 4
                else:
                    print("Erreur, vous devez choisir parmi les trois propositions")
                    test = 0
            except ValueError:
                print("Erreur, vous devez entrer une valeur au format numérique")
        return choice

    @staticmethod
    def get_player_surname():
        surname = str.capitalize(input("Quel est le nom de famille du joueur ? "))
        return surname

    @staticmethod
    def get_player_name():
        name = str.capitalize(input("Quel est le prénom du joueur ? "))
        return name

    @staticmethod
    def get_player_date_of_birth():
        date_test = 0
        date_of_birth = -1
        while date_test == 0:
            date_of_birth = input("Quel est la date de naissance du joueur ? (format numérique Jour/Mois/Année) ")
            try:
                datetime.datetime.strptime(date_of_birth, "%d/%m/%Y")
                date_test += 1
            except ValueError:
                print("Veuillez saisir une date valide")
        return date_of_birth

    @staticmethod
    def get_player_sex():
        test = 0
        sex = -1
        while test == 0:
            request = input("Quel est le sexe du joueur ? \n"
                            "tapez 1 pour Homme \n"
                            "tapez 2 pour Femme \n")
            try:
                test = int(request) + 1
                if int(request) == 1:
                    sex = "Homme"
                elif int(request) == 2:
                    sex = "Femme"
                else:
                    print("Erreur, vous devez choisir parmi les deux propositions")
                    test = 0
            except ValueError:
                print("Erreur, vous devez entrer une valeur au format numérique")
        return sex

    @staticmethod
    def get_player_rank():
        test = 0
        ranking = -1
        while test == 0:
            ranking = input("Quel est le rang du joueur ? ")
            try:
                test = int(ranking) + 1
            except ValueError:
                print("Erreur, vous devez entrer un classement au format numérique")
        return ranking

    @staticmethod
    def get_tournament_name():
        name = str.capitalize(input("Quel est le nom du tournoi ? "))
        return name

    @staticmethod
    def get_tournament_place():
        place = str.capitalize(input("Où se déroule le tournoi ? "))
        return place

    @staticmethod
    def get_tournament_date():
        test = 0
        tournament_date = -1
        while test == 0:
            tournament_date = input("A quelle date se déroule le tournoi ? (format numérique Jour/Mois/Année) ")
            try:
                datetime.datetime.strptime(tournament_date, "%d/%m/%Y")
                test += 1
            except ValueError:
                print("Veuillez saisir une date valide")
        return tournament_date

    @staticmethod
    def get_tournament_number_of_rounds():
        number_of_rounds = input("Combien de tours composent le tournoi ? (tapez enter pour la valeur par défaut = 4) ")
        if number_of_rounds != "":
            return number_of_rounds
        else:
            number_of_rounds = ""
            return number_of_rounds

    @staticmethod
    def get_score_player_1():
        test = 0
        score = -1
        while test == 0:
            score = input("Quel est le score du joueur 1 ? ")
            try:
                test = int(score) + 1
            except ValueError:
                print("Erreur, vous devez entrer un score au format numérique")
        return score

    @staticmethod
    def get_score_player_2():
        test = 0
        score = -1
        while test == 0:
            score = input("Quel est le score du joueur 2 ? ")
            try:
                test = int(score) + 1
            except ValueError:
                print("Erreur, vous devez entrer un score au format numérique")
        return score

    @staticmethod
    def get_tournament_time_control():
        test = 0
        choice = -1
        while test == 0:
            time_control = input("Quel est le type de contrôle de temps  ? \n"
                                 "tapez 1 pour bullet\n"
                                 "tapez 2 pour blitz\n"
                                 "tapez 3 pour coup rapide\n")
            try:
                test = int(time_control) + 1
                if int(time_control) == 1:
                    choice = "bullet"
                elif int(time_control) == 2:
                    choice = "blitz"
                elif int(time_control) == 3:
                    choice = "coup rapide"
                else:
                    print("Erreur, vous devez choisir parmi les trois propositions")
                    test = 0
            except ValueError:
                print("Erreur, vous devez entrer une valeur au format numérique")
        return choice

    @staticmethod
    def get_tournament_description():
        description = str.capitalize(input("Description du tournoi : "))
        return description


def main():
    pass


if __name__ == "__main__":
    main()
