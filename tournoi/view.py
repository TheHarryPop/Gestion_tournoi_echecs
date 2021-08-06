import datetime


class View:

    @staticmethod
    def get_principal_choices():
        test = 0
        choice = -1
        while test == 0:
            request = input("Quelle action souhaitez vous réaliser ? \n"
                            "tapez 1 pour créer un joueur \n"
                            "tapez 2 pour créer un tournoi \n"
                            "tapez 3 pour charger un tournoi déjà créé \n"
                            "tapez 4 pour quitter l'application \n")
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
                    print("Erreur, vous devez choisir parmi les propositions")
                    test = 0
            except ValueError:
                print("Erreur, vous devez entrer une valeur au format numérique")
        return choice

    @staticmethod
    def get_tournament_choices():
        test = 0
        choice = -1
        while test == 0:
            request = input("Quelle action souhaitez vous réaliser ? \n"
                            "tapez 1 pour créer un nouveau tour \n"
                            "tapez 2 pour renseigner les scores \n"
                            "tapez 3 pour afficher le classement \n"
                            "tapez 4 pour revenir au menu principal \n"
                            "tapez 5 pour quitter l'application \n")
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
                elif int(request) == 5:
                    choice = 5
                else:
                    print("Erreur, vous devez choisir parmi les propositions")
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
    def get_score_player(player_name):
        test = 0
        score = -1
        while test == 0:
            request = input(f"Quel est le résultat de {player_name} ? \n"
                            "tapez 1 pour un victoire \n"
                            "tapez 0 pour un défaite \n"
                            "tapez 0.5 pour un match nul \n")
            try:
                test = float(request) + 1
                if float(request) == 1.0:
                    score = 1
                elif float(request) == 0.0:
                    score = 0
                elif float(request) == 0.5:
                    score = 0.5
                else:
                    print("Erreur, vous devez choisir parmi les propositions")
                    test = 0
            except ValueError:
                print("Erreur, vous devez entrer une valeur au format numérique")
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

    @staticmethod
    def create_tournament_false(player_table):
        print("La base de données doit contenir au moins 8 joueurs pour pouvoir créer un tournoi \n"
              f"Pour le moment, elle en contient {len(player_table)}")

    @staticmethod
    def ok_tournament_load():
        print("Tournoi chargé")

    @staticmethod
    def nok_tournament_load():
        print("il n'existe pas de tournoi enregistré")

    @staticmethod
    def ok_turn_score():
        print("Résultats du tour enregistrés")

    @staticmethod
    def nok_turn_load():
        print("il n'existe pas de tour enregistré")

    @staticmethod
    def get_name():
        test = 0
        while test == 0:
            name = str.capitalize(input("Quel est le nom du joueur à ajouter au tournoi ? "))
            try:
                int(name)
            except ValueError:
                test += 1
                return name

    @staticmethod
    def error_name_in_list(name):
        print(f"Erreur, {name} ne fait pas partie de la liste des joueurs")

    @staticmethod
    def error_name_in_tournament(name):
        print(f"Erreur, {name} fait déjà partie de la liste des joueurs inscrits au tournoi")

    @staticmethod
    def data_tournament(data_list):
        name = str.capitalize(input(f"Voici le(s) tournoi(s) enregistré(s) :\n"
                                    f"{data_list}\n"
                                    f"Lequel voulez vous charger ? "))
        return name


    @staticmethod
    def error_tournament_in_list(tournament):
        print(f"Erreur, {tournament} ne fait pas partie de la liste des tournois")

    @staticmethod
    def print_players_name_list(players_name_list):
        print(players_name_list)

    @staticmethod
    def number_of_players(tournament_players):
        print(f"Il manque encore {8 - len(tournament_players)} joueur(s) inscrit(s) au tournoi")

    @staticmethod
    def print_tournament_ranking(tournament_ranking_df):
        print(tournament_ranking_df)

    @staticmethod
    def scores_already_registered():
        print("Les scores du dernier tour sont déjà enregistrés")


if __name__ == "__main__":
    View.get_name()
