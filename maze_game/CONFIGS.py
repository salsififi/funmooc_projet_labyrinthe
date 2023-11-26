"""Contient toutes les constantes du programme"""

# Coordonnées du labyrinthe
XMIN, XMAX = -240, 50
YMIN, YMAX = -240, 200
LARGEUR_LABY = XMAX - XMIN
HAUTEUR_LABY = YMAX - YMIN

# Coordonnées de la zone d'affichage des annonces
POINT_AFFICHAGE_ANNONCES = (-240, 240)  # Point d'origine de l'affichage des annonces
LARGEUR_ZONE_ANNONCES = 940
HAUTEUR_ZONE_ANNONCES = 80

# Coordonnées de la zone d'affichage de l'inventaire
POINT_AFFICHAGE_INVENTAIRE = (70, 180)  # Point d'origine de l'affichage de l'inventaire
POINT_BAS_INVENTAIRE = (70, -240)
LARGEUR_INVENTAIRE = 630
HAUTEUR_INVENTAIRE = 475

# Les valeurs ci-dessous définissent les couleurs des cases du plan
COULEUR_COULOIR = 'white'
COULEUR_MUR = 'grey'
COULEUR_OBJECTIF = 'yellow'
COULEUR_PORTE = 'orange'
COULEUR_OBJET = 'green'
COULEUR_VUE = 'wheat'
COULEURS = [COULEUR_COULOIR, COULEUR_MUR, COULEUR_OBJECTIF, COULEUR_PORTE, COULEUR_OBJET, COULEUR_VUE]
COULEUR_EXTERIEUR = 'white'

# Couleur et dimension du personnage
COULEUR_PERSONNAGE = 'red'
RATIO_PERSONNAGE = 0.9  # Rapport entre diamètre du personnage et dimension des cases
POSITION_DEPART = (0, 1)  # Porte d'entrée du château

# Désignation des fichiers de données à utiliser
fichier_plan = 'maze_game/sources/plans/plan_chateau.txt'
fichier_questions = 'maze_game/sources/portes/dico_portes.txt'
fichier_objets = 'maze_game/sources/objets/dico_objets.txt'
fichier_inventaire = 'maze_game/inventaire.txt'

# Codes utilisés pour désigner les différents éléments
CASE_VIDE = 0
CASE_MUR = 1
CASE_SORTIE = 2
CASE_PORTE = 3
CASE_OBJET = 4
CASE_VUE = 5
