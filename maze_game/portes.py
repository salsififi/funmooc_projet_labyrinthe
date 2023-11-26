"""Contient les fonctions nécessaires à la gestion des portes"""

import turtle as t
from .CONFIGS import *
from maze_game import affichage_textes


def creer_dictionnaire_questions() -> dict:
    """
    Crée le dictionnaire des couples questions/réponses associés à la position des portes.
    :return: Dictionnaire avec pour entrées les coordonnées des portes et pour valeurs des
    tuples (question, réponse)
    """
    dico_questions = {}
    with open(fichier_questions, 'r', encoding="utf-8") as f:
        for ligne in f.readlines():
            coordo, couple_q_r = eval(ligne)
            dico_questions[coordo] = couple_q_r
    return dico_questions


def poser_question(case: tuple) -> bool:
    """
    Pose la question associée à la porte, et renvoie True si la réponse donnée est bonne, False sinon.
    :param case:  tuple contenant les coordonnées de la case porte dans la matrice
    :return: True si l'utilisateurice répond bien à la question, False sinon
    """
    dico_questions = creer_dictionnaire_questions()
    question, bonne_reponse = dico_questions[case]
    reponse = t.textinput("Question", question)

    t.listen()

    if reponse == bonne_reponse:
        affichage_textes.annonce("La porte s'ouvre !")
        return True
    affichage_textes.annonce("Mauvaise réponse...")
    return False
