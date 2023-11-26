"""Contient les fonctions nécessaires à la gestion des objets"""

import turtle as t
from .CONFIGS import *
from maze_game import labyrinthe as laby
from maze_game import affichage_textes


def creer_dictionnaire_objets(fichier_des_objets: str) -> dict:
    """
    Crée le dictionnaire des objets associés à leur placement dans le labyrinthe.
    :param fichier_des_objets: chemin du fichier texte contenant les infos sur les objets. Dans ce fichier,
    chaque ligne donne les coordonnées d'un objet, puis sa désignation. Ex: (12, 3), "un oreiller"
    :return: dictionnaire des objets dans lequel:
    - les clés sont des tuples (lig, col) correspondant aux coordonnées de la case où est l'objet
    - les valeurs sont des chaînes indiquant de quel objet il s'agit
    """
    dico_objets = {}
    with open(fichier_des_objets, 'r', encoding="utf-8") as f:
        for ligne in f.readlines():
            coordonnees, objet = eval(ligne)
            dico_objets[coordonnees] = objet
    return dico_objets


def afficher_inventaire(inventaire: list):
    """
    Affiche l'inventaire dans la zone prévue à cet effet
    :param inventaire: liste des lignes contenues dans le fichier inventaire.txt
    """

    police = ("Arial", 16, "normal")
    nb_lignes = len(inventaire)
    nb_objets = nb_lignes - 1
    x, y = POINT_AFFICHAGE_INVENTAIRE
    y -= 40 * nb_objets

    t.up()
    t.goto(x, y)
    t.down()
    t.color("black")
    t.write(inventaire[nb_objets], font=police)


def ramasser_objet(plan, case_objet):
    """Tout ce qui se passe quand le personnage se déplace sur une case où il y a un objet!"""
    lig, col = case_objet

    # on "vide" la case en la passant en blanc
    plan[lig][col] = CASE_VIDE
    laby.tracer_case(plan, case_objet)

    # on cherche l'objet associé à cette case
    dico_objets = creer_dictionnaire_objets(fichier_objets)

    # on affiche un message dans la zone d'annonces
    message = "Vous avez trouvé un indice !"
    affichage_textes.annonce(message)

    # on ajoute l'objet dans l'inventaire
    with open(fichier_inventaire, 'a', encoding="utf-8") as f:
        f.write(f"\n- {dico_objets[case_objet]}")
    with open(fichier_inventaire, 'r', encoding="utf-8") as f:
        inventaire = f.readlines()
    afficher_inventaire(inventaire)
