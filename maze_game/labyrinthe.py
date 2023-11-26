"""Contient des fonctions nécessaires à l'affichage du labyrinthe."""

import turtle as t
from .CONFIGS import *


def lire_matrice(mapfile: str) -> list:
    """
    Renvoie la matrice du plan du labyrinthe
    :param mapfile: fichier texte contenant le plan à tracer
    :return: matrice contenant les données du fichier converties en type int
    """
    with open(mapfile, 'r', encoding="utf-8") as f_map:
        plan = [ligne.strip().split() for ligne in f_map.readlines()]
        plan = [[int(plan[i][j]) for j in range(len(plan[0]))] for i in range(len(plan))]
    return plan


def calculer_pas(matrice: list) -> int:
    """
    Calcule la dimension à donner au côté des cases carrées afin que cela tienne dans la zone
    d'affichage du plan (290 px de large, 440 px de haut)
    :type matrice: matrice du plan du labyrinthe
    :return: entier représentant la taille du côté de chaque case
    """
    nb_cases_par_ligne = len(matrice[0])
    nb_cases_par_colonne = len(matrice)
    taille_max_hauteur = HAUTEUR_LABY // nb_cases_par_colonne
    taille_max_largeur = LARGEUR_LABY // nb_cases_par_ligne
    return min(taille_max_largeur, taille_max_hauteur)


def coordonnees(case: tuple, pas: int) -> tuple:
    """
    Renvoie les coordonnées en pixels turtle du coin inférieur gauche de case.
    :param case: tuple (ligne, colonne) désignant les coordonnées de la case dans une grille dont
    le point (0, 0) est en haut à gauche
    :param pas: nombre entier de pixels du côté d'une case
    :return: tuple (x, y) du coin inférieur gauche d'une case dans turtle (l'axe x étant horizontal et
    allant de -240 à 50 de gauche à droite, l'axe y étant vertical et allant de -240 à 200 de bas en
    haut)
    """
    lig, col = case
    x_case = XMIN + (col * pas)
    y_case = YMAX - pas - (lig * pas)
    return x_case, y_case


def tracer_carre(dimension: int):
    """Trace un carré dont la mesure du côté est de dimension pixels turtle"""
    for _ in range(4):
        t.forward(dimension)
        t.left(90)


def tracer_case(matrice: list, case: tuple):
    """
    Trace et colorie une case avec la couleur associée.
    :param matrice: matrice du plan du labyrinthe
    :param case: tuple(ligne, colonne) indiquant la position de la case dans la matrice du plan
    """

    def trouve_couleur_case() -> str:
        """Renvoie la couleur de la case"""
        id_lig, id_col = case
        code_couleur = matrice[id_lig][id_col]
        return COULEURS[code_couleur]

    couleur = trouve_couleur_case()
    pas = calculer_pas(matrice)
    x, y = coordonnees(case, pas)
    t.hideturtle()
    t.up()
    t.goto(x, y)
    t.down()
    t.color(couleur)
    t.begin_fill()
    tracer_carre(pas)
    t.end_fill()


def afficher_plan(matrice: list):
    """Affiche le plan du château à partir de la matrice de son plan"""
    for id_lig in range(len(matrice)):
        for id_col in range(len(matrice[0])):
            code_couleur = matrice[id_lig][id_col]
            if code_couleur == CASE_VIDE:
                continue  # on zappe les cases blanches
            tracer_case(matrice, (id_lig, id_col))
