"""Contient les fonctions nécessaires à l'affichage des annonces et de l'inventaire."""

import turtle as t
from .CONFIGS import *


def clear_zone(depart: tuple, largeur: int, hauteur: int):
    """
    Efface le contenu d'une zone rectangulaire
    :param depart: tuple contenant les coordonnées turtle du coin inférieur gauche de la zone
    :param largeur: nombre de pixels de la largeur de la zone
    :param hauteur: nombre de pixels de la hauteur de la zone
    """
    t.up()
    t.goto(depart)
    t.down()
    t.color(COULEUR_EXTERIEUR)
    t.begin_fill()
    for _ in range(2):
        t.forward(largeur)
        t.left(90)
        t.forward(hauteur)
        t.left(90)
    t.end_fill()


def clear_annonces():
    """Efface le contenu de la zone des annonces"""
    clear_zone(POINT_AFFICHAGE_ANNONCES, LARGEUR_ZONE_ANNONCES, HAUTEUR_ZONE_ANNONCES)


# Fonction inutilisée à ce stade, mais qui sera utile pour un éventuel développement
# avec changements de niveaux
def clear_inventaire():
    """Efface le contenu de la zone d'inventaire"""
    clear_zone(POINT_BAS_INVENTAIRE, LARGEUR_INVENTAIRE, HAUTEUR_INVENTAIRE)


def annonce(prompt: str, style="normal", taille=16, couleur="black"):
    """Écrit un message (promt) dans la zone Annonces"""
    police = ("Arial", taille, style)
    clear_annonces()
    t.up()
    t.goto(POINT_AFFICHAGE_ANNONCES)
    t.down()
    t.color(couleur)
    t.write(prompt, font=police)
