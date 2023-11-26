"""
Quête dans le château au sommet du Python des neiges
Auteur : Simon Salvaing
Date : novembre 2023
Jeu de labyrinthe proposé comme projet final guidé du MOOC "Apprenez à coder en Python" de
    France Université Numérique (www.fun-mooc.fr)
Point d'entrée du jeu
"""

from maze_game import personnage as perso, labyrinthe as laby, objets
from maze_game.CONFIGS import *
import turtle as t


def main():

    # Désactivation du tracé automatique
    t.Screen().tracer(0)

    # Affichage du labyrinthe, du personnage et de l'inventaire (vide)
    plan = laby.lire_matrice(fichier_plan)
    laby.afficher_plan(plan)
    perso.placer_personnage(plan, POSITION_DEPART)
    with open(fichier_inventaire, 'w', encoding="utf-8") as f_inventaire:
        f_inventaire.write("Inventaire :")
    with open(fichier_inventaire, 'r', encoding="utf-8") as f_inventaire:
        objets.afficher_inventaire(f_inventaire.readlines())

    # Déplacements
    t.listen()
    t.onkeypress(perso.deplacer_gauche, "Left")
    t.onkeypress(perso.deplacer_droite, "Right")
    t.onkeypress(perso.deplacer_haut, "Up")
    t.onkeypress(perso.deplacer_bas, "Down")
    t.mainloop()


if __name__ == "__main__":
    main()
