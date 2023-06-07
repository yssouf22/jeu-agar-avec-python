# -*- coding: utf-8 -*-

import math

# La fonction pour lire le fichier d'entrée
def read_input(file_name):
    with open(file_name, 'r') as file:
        data = file.read().split("\n")
    time = int(data[0]) # Extraire le temps imparti
    # Vérifiez si chaque ligne n'est pas vide avant de tenter de la traiter
    cells = [list(map(int, i.split(','))) for i in data[1:] if i] # Extraire les informations des cellules
    return time, cells

# La fonction pour écrire le fichier de sortie
def write_output(file_name, cells_to_eat):
    with open(file_name, 'w') as file:
        for cell in cells_to_eat:
            file.write(str(cell) + "\n") # Écrire chaque cellule à manger

# Trouver la cellule la plus proche de la position actuelle
def closest_cell(current_position, cells):
    closest_cell = None
    closest_distance = float('inf')

    for cell in cells:
        # Calculer la distance à l'aide de la formule de distance Euclidienne
        distance = math.sqrt((cell[1] - current_position[0])**2 + (cell[2] - current_position[1])**2)
        # Mettre à jour la cellule la plus proche et la distance la plus proche
        if distance < closest_distance:
            closest_cell = cell
            closest_distance = distance

    return closest_cell, closest_distance

# Manger autant de cellules que possible dans le temps imparti
def eat_cells(time, cells):
    cells_to_eat = [] # Initialiser la liste des cellules à manger
    current_position = [0, 0] # Définir la position de départ
    remaining_time = time # Initialiser le temps restant

    # Continuer à manger des cellules tant qu'il reste du temps
    while cells:
        # Trouver la cellule la plus proche
        cell, distance = closest_cell(current_position, cells)
        # Si le temps nécessaire pour atteindre la cellule est inférieur au temps restant
        if distance <= remaining_time:
            remaining_time -= distance # Mettre à jour le temps restant
            current_position = [cell[1], cell[2]] # Mettre à jour la position actuelle
            cells_to_eat.append(cell[0]) # Ajouter la cellule à la liste des cellules à manger
            cells.remove(cell) # Supprimer la cellule de la liste des cellules disponibles
        else:
            break

    return cells_to_eat

# La fonction principale
def main():
    time, cells = read_input('input.txt') # Lire le fichier d'entrée
    cells_to_eat = eat_cells(time, cells) # Calculer les cellules à manger
    write_output('output.txt', cells_to_eat) # Écrire le fichier de sortie

if __name__ == "__main__":
    main()
