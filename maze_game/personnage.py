"""Contient des fonctions nécessaires au traitement du personnage dans le labyrinthe."""

import turtle as t
from .CONFIGS import *
from maze_game import labyrinthe as laby
from maze_game import objets
from maze_game import portes
from maze_game import affichage_textes as aff_tex


plan = laby.lire_matrice(fichier_plan)
case_perso = POSITION_DEPART


def placer_personnage(matrice: list, case: tuple):
    """
    Place le personnage.
    :param matrice: matrice du plan du labyrinthe
    :param case: tuple contenant les coordonnées de la case où se situe le personnage
    """
    pas = laby.calculer_pas(matrice)
    x_perso, y_perso = laby.coordonnees(case, pas)
    x_perso += pas / 2
    y_perso += pas / 2
    t.up()
    t.goto(x_perso, y_perso)
    t.down()
    t.dot(RATIO_PERSONNAGE * pas, COULEUR_PERSONNAGE)


def deplacer(mouvement: tuple):
    """
    Déplace le personnage si le mouvement demandé est autorisé.
    :param mouvement: tuple définissant le mouvement demandé
    """
    global plan, case_perso
    nv_lig = case_perso[0] + mouvement[0]
    nv_col = case_perso[1] + mouvement[1]
    nv_case = (nv_lig, nv_col)
    dans_la_carte = nv_lig in range(len(plan)) and nv_col in range(len(plan[0]))
    porte_ouverte = False

    # on efface la zone d'annonces
    aff_tex.clear_annonces()

    if plan[nv_lig][nv_col] == CASE_PORTE:
        aff_tex.annonce("Cette porte est fermée.")
        porte_ouverte = portes.poser_question(nv_case)
    mvt_possible = (dans_la_carte
                    and (plan[nv_lig][nv_col] in (CASE_VIDE, CASE_SORTIE, CASE_OBJET, CASE_VUE)
                         or porte_ouverte))

    if mvt_possible:
        # on retrace la case de départ sans la tortue, en la colorant (case vue)
        plan[case_perso[0]][case_perso[1]] = CASE_VUE
        laby.tracer_case(plan, case_perso)
        # s'il y a un objet dans la case de destination:
        if plan[nv_lig][nv_col] == CASE_OBJET:
            objets.ramasser_objet(plan, nv_case)
        # si la case de destination est une porte
        if plan[nv_lig][nv_col] == CASE_PORTE:
            plan[nv_lig][nv_col] = CASE_VIDE
            laby.tracer_case(plan, nv_case)
        # on place la tortue sur la nouvelle case de destination
        placer_personnage(plan, nv_case)
        case_perso = nv_case

        # et en cas de victoire...
        if plan[nv_lig][nv_col] == CASE_SORTIE:
            message = "Vous avez gagné!\nBRAVO !!!"
            aff_tex.annonce(message, style="bold", taille=24, couleur="red")
            # désactivation des flèches de déplacement
            t.onkeypress(None, "Right")
            t.onkeypress(None, "Left")
            t.onkeypress(None, "Up")
            t.onkeypress(None, "Down")
            t.exitonclick()


def deplacer_gauche():
    """Déplace le personnage d'une case à gauche si le mouvement est valide"""
    t.onkeypress(None, "Left")
    deplacer((0, -1))
    t.onkeypress(deplacer_gauche, "Left")


def deplacer_droite():
    """Déplace le personnage d'une case à gauche si le mouvement est valide"""
    t.onkeypress(None, "Right")
    deplacer((0, 1))
    t.onkeypress(deplacer_droite, "Right")


def deplacer_haut():
    """Déplace le personnage d'une case à gauche si le mouvement est valide"""
    t.onkeypress(None, "Up")
    deplacer((-1, 0))
    t.onkeypress(deplacer_haut, "Up")


def deplacer_bas():
    """Déplace le personnage d'une case à gauche si le mouvement est valide"""
    t.onkeypress(None, "Down")
    deplacer((1, 0))
    t.onkeypress(deplacer_bas, "Down")
