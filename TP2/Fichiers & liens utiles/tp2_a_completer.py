import datetime

date_actuelle = datetime.date.today()


def str_to_date(s):
    """
    Transforme une chaine de caractères au format AAAA-MM-JJ en un objet date.
    Si la chaine de caractères passée en argument est vide ou contient uniquement des espaces, la fonction devra retourner la date d'aujourd'hui.
    
    Args:
        s (str): Une chaine de caractères au format AAAA-MM-JJ à convertir en date.
    
    Returns:
        datetime.date: Une date du module datetime.
    """
    # TODO: À compléter


def str_to_heure(s):
    """
    Transforme une chaine de caractères au format HH:MM en un objet heure.
    Si la chaine de caractères passée en argument est vide ou contient uniquement des espaces, la fonction devra retourner None.

    Args:
        s (str): Une chaine de caractères au format HH:MM à convertir en heure.
    
    Returns:
        datetime.time: une heure du module datetime ou None.
    """
    # TODO: À compléter


def creer_agenda(nom_proprietaire):
    """
    Étant donné un nom de propriétaire, elle crée un nouvel agenda.
    Un agenda est juste un dictionnaire avec les champs 'proprio',
    'evenements', et 'max_id'.
    La liste des évènements d'un nouvel agenda devrait être une liste vide,
    et max_id devrait avoir 0 comme valeur initiale.

    Args:
        nom_proprietaire (str): Le nom du propriétaire de l'agenda.
    
    Returns:
        dict: Dictionnaire qui représente l'agenda.
    """
    # TODO: À compléter


def creer_evenement(identifiant, date, heure_debut, heure_fin, titre, lieu=None):
    """
    En se servant des informations passées comme arguments, cette fonction crée un
    nouvel évènement.
    Un évènement est un dictionnaire ayant les champs 'id', 'date', 'heure_debut', 'heure_fin', 'titre' et 'lieu'.

    Args:
        id (int): L'identifiant de l'évènement.
        date (datetime.date): La date de l'évènement.
        heure_debut (datetime.time): L'heure à laquelle débutera l'évènement.
        heure_fin (datetime.time): L'heure à laquelle l'évènement prendra fin.
        titre (str): Titre ou nom de l'évènement.
        lieu (str, optional): La place ou lieu où se déroulera l'évènement. None comme valeur par défaut.
    
    Returns:
        dict: Dictionnaire représentant un évènement.
    """
    # TODO: À compléter


def evenement_to_str(evt):
    """
    Formate un évènement en une chaine de caractères prête pour l'affichage.
    
    - Dans le cas où un lieu a été spécifié, le format est le suivant:
        ID:1 => Mariage du premier ministre
        2017-08-13 12:00 à 18:00
        Lieu: Cathédrale du Soleil Levant

    - Dans le cas où le lieu est égal à None, le format est le suivant:
        ID:2 => Mariage du professeur
        2017-08-16 14:00 à 18:00
        Lieu: Inconnu

    Args:
        evt (dict): L'évènement à formater.
    
    Returns:
        str: Chaîne de caractères dans le format ci-dessus représentant l'évènement passé en argument.
    """
    # TODO: À compléter


def sauvegarder_agenda(agenda, fichier):
    """
    Cette fonction sauvegarde l'agenda au niveau de l'emplacement fichier indiqué.
    Que le fichier existe ou pas, il devra être créé de nouveau.
    Le format du fichier est le suivant:
        Tom Tam
        3
        ID:1 => Mariage du premier ministre
        2017-08-13 12:00 à 18:00
        Lieu: Cathédrale du Soleil Levant
        ID:2 => Visite de grand-mère
        2017-08-03 11:00 à 16:00
        Lieu: Maison familiale
        ID:3 => Réunion du G8
        2017-09-21 09:00 à 12:00
        Lieu: Inconnu

    La première ligne du fichier est le nom du propriétaire.
    La seconde ligne représente le max_id.
    Les lignes d'après représentent les évènements formatés les uns à la suite des autres.

    Args:
        agenda (dict): L'agenda à sauvegarder.
        fichier (str): Emplacement du fichier où l'agenda sera sauvegardé.
    """
    # TODO: À compléter


def charger_agenda(fichier):
    """
    Opération inverse de la fonction 'sauvegarder_agenda'.
    Elle permet étant donné l'emplacement d'un fichier contenant un agenda de charger en mémoire cet agenda.

    Args:
        fichier (str): Emplacement du fichier où l'agenda a été sauvegardé.
    
    Returns:
        dict: Agenda contenu dans le fichier lu.
    """
    # TODO: À compléter
        

def saisir_evenement():
    """
    Demande à l'utilisateur de rentrer les informations relatives à un évènement.
    Les informations doivent être demandées dans l'ordre suivant: titre, date,
    heure de début, heure de fin, lieu.
    C'est le rôle de la fonction de s'assurer que toutes les informations
    recueillies sont valides.

    Returns:
        tuple: Un tuple (date, debut, fin, titre, lieu), l'ordre est important.
    """
    # TODO: À compléter


def evenements_en_conflit(evt1, evt2):
    """
    Permet de déterminer si deux évènements sont en conflit ou pas.
    Deux évènements sont en conflit si les plages horaires où ils
    auront lieu se chevauchent.
    Ex: 

    - Cas 1: Les évènements ci-dessous sont en conflit:

        event1 = {
            'date': str_to_date('2017-10-03'),
            'heure_debut': str_to_heure('15:00'),
            'heure_fin': str_to_heure('18:30'),
        }

        event2 = {
            'date': str_to_date('2017-10-03'),
            'heure_debut': str_to_heure('16:00'),
            'heure_fin': str_to_heure('17:00'),
        }

    - Cas 2: Les évènements ci-dessous ne sont pas en conflit:

        event1 = {
            'date': str_to_date('2017-08-05'),
            'heure_debut': str_to_heure('15:00'),
            'heure_fin': str_to_heure('18:30'),
        }

        event2 = {
            'date': str_to_date('2017-10-03'),
            'heure_debut': str_to_heure('16:00'),
            'heure_fin': str_to_heure('17:00'),
        }

    Args:
        evt1 (dict): Premier évènement.
        evt2 (dict): Second évènement.
    
    Returns:
        bool: True si les deux évènements sont en conflit, False sinon.
    """
    # TODO: À compléter


def ajouter_evenement(agenda, date, heure_debut, heure_fin, titre_evenement, lieu=None):
    """
    Étant donné un agenda et les renseignements sur un évènement à y ajouter,
    cette fonction crée un nouvel évènement qui est ensuite ajouté à l'agenda.
    L'identifiant de l'évènement créé doit être agenda['max_id'] + 1.

    Args:
        agenda (dict): Agenda auquel on veut ajouter un évènement.
        date (datetime.date): La date où se passe l'évènement.
        heure_debut (datetime.time): L'heure à laquelle débutera l'évènement.
        heure_fin (datetime.time): L'heure à laquelle l'évènement prendra fin.
        titre_evenement (str): Titre ou nom de l'évènement.
        lieu (str, optional): La place ou lieu où se déroulera l'évènement. None comme valeur par défaut.
    
    Returns:
        bool: True si l'évènement créé a pu être ajouté à l'agenda, False sinon.
    """
    # TODO: À compléter


def supprimer_evenement(agenda, identifiant):
    """
    Supprime un évènement présent au niveau d'un agenda.

    Args:
        agenda (dict): L'agenda au niveau duquel l'on souhaite faire la suppression.
        identifiant (int): ID de l'évènement à supprimer.
    
    Returns:
        bool: True si l'évènement est supprimé, False sinon.
    """
    # TODO: À compléter


def agenda_to_str(agenda, date_debut, date_fin):
    """
    Produit une chaine de caractères contenant les évènements
    présents au niveau d'un agenda entre deux dates (inclusivement).
    Les évènements doivent être triés en ordre de date et heure.

    Exemples:

    - Cas 1: Aucun évènement
    ------------------------------------------------------------
    Bonjour Prudencio Tossou, au programme le 2017-10-12:
    Aucun évènement à afficher
    ------------------------------------------------------------
    
    - Cas 2: Deux évènements
    ------------------------------------------------------------
    Bonjour Prudencio, au programme le 2017-10-12:
    ID:1 => Dance Party
    2017-10-12 16:00 à 18:30
    Lieu: Inconnu

    ID:1 => Super Gala
    2017-10-12 14:00 à 20:00
    Lieu: Franconville Leredu
    ------------------------------------------------------------


    Args:
        agenda (dict): L'agenda à afficher.
        date_debut (datetime.date): La date de début d'affichage.
        date_fin (datetime.date): La date de fin d'affichage.
    
    Returns:
        str: Chaine de caractères contenant les évènements concernés en ordre de date et heure.
    """
    res = "-"*60 + '\n'
    if date_debut == date_fin:
        res += ("Bonjour {}, au programme le {}:\n".format(agenda["proprio"].title(), date_debut))
    else:
        res += ("Bonjour {}, au programme du {} au {}:\n".format(agenda["proprio"].title(), date_debut, date_fin))

    concernes = [evt for evt in agenda["evenements"] if date_debut <= evt["date"] <= date_fin]
    concernes = sorted(concernes, key=lambda k: (k['date'], k['heure_debut']))
    dernier_evt_concerne = concernes[len(concernes) - 1] if concernes else None
    if concernes == []:
        res += "Aucun évènement à afficher.\n"
    for evt in concernes:
        if dernier_evt_concerne and evt == dernier_evt_concerne:
            res += evenement_to_str(evt) + '\n'
        else:
            res += evenement_to_str(evt) + '\n\n'
    return res + '-'*60


def afficher_menu():
    """ Affiche le menu pour l'interface utilisateur"""
    print("Menu")
    print("1- Créer un nouvel agenda")
    print("2- Ouvrir un agenda existant")
    print("3- Sauvegarder les modifications effectuées")
    print("4- Ajouter un évènement")
    print("5- Supprimer un évènement")
    print("6- Afficher l'agenda")
    print("7- Quitter")

def main():
    print("*"*50)
    print("{:^50}".format("Bienvenue dans votre gestionnaire d'agenda."))
    print("*" * 50)

    agenda = None
    continuer = True
    courant_sauvegarder = True
    while continuer:

        afficher_menu()

        choix = int(input("Entrez votre choix: "))

        if choix == 1:
            if (agenda is None) or (not courant_sauvegarder):
                proprio = input("Entrez le nom du propriétaire de l'agenda: ")
                agenda = creer_agenda(proprio)
                courant_sauvegarder = False
                print("🎉  Agenda créé avec succès!")
            else:
                print("❌  Veuillez sauvegarder l'agenda courant avant de continuer.")
        elif choix == 2:
            if (agenda is None) or (not courant_sauvegarder):
                chemin = input("Entrez le chemin d'accès au fichier de chargement: ")
                agenda = charger_agenda(chemin)
                courant_sauvegarder = False
                print("🎉  Agenda ouvert avec succès!")
            else:
                print("❌  Veuillez sauvegarder l'agenda courant avant de continuer.")
        elif choix == 3:
            if agenda is None:
                print("❌  Aucun agenda ouvert.")
            else:
                chemin = input("Entrez un chemin d'accès au fichier de sauvegarde: ")
                sauvegarder_agenda(agenda, chemin)
                print("🎉  Agenda sauvegardé!")
                courant_sauvegarder = True
        elif choix == 4:
            if agenda is None:
                print("❌  Aucun agenda ouvert.")
            else:
                date, debut, fin, titre, lieu = saisir_evenement()
                res = ajouter_evenement(agenda, date, debut, fin, titre, lieu)
                if res:
                    print('🎉  Évènement ajouté avec succès!')
                else:
                    print("❌  L'évènement n'a pu être ajouté.")
                courant_sauvegarder = False
        elif choix == 5:
            if agenda is None:
                print("❌  Aucun agenda ouvert")
            else:
                identifiant = int(input("Id de l'évènement à supprimer: "))
                res = supprimer_evenement(agenda, identifiant)
                if res:
                    print("🎉  Évenement supprimé!")
                else:
                    print("❌  L'évènement n'a pu être supprimé ou aucun évènement ayant cet ID.")
                courant_sauvegarder = False
        elif choix == 6:
            if agenda is None:
                print("❌  Aucun agenda ouvert.")
            else:
                print("Veuillez sélectionner la période d'affichage.\n"
                      "Laissez les champs vides pour afficher uniquement les évènements qui auront lieu aujourd'hui.")
                date_debut = str_to_date(input("Entrez la date de début, SVP au format AAAA-MM-JJ: "))
                date_fin = str_to_date(input("Entrez la date de fin, SVP au format AAAA-MM-JJ: "))
                print(agenda_to_str(agenda, date_debut, date_fin))
        elif choix == 7:
            if not courant_sauvegarder:
                print("❌  Veuillez sauvegarder l'agenda courant avant de continuer.")
            else:
                continuer = False
        print()

if __name__ == '__main__':
    main()
