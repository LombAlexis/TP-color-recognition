import csv
import random
import sys
import math

"""
#####################################################
        Générateur de dataset (CSV)
#####################################################
"""


"""
Correspondances entre nom de couleurs et valeurs en (r,g,b)
"""
COLORS = {
    "black"     : (0,0,0),
    "silver"    : (192,192,192),
    "gray"      : (128,128,128),
    "white"     : (255,255,255),
    "maroon"    : (128,0,0),
    "red"       : (255,0,0),
    "purple"    : (128,0,128),
    "fuchsia"   : (255,0,255),
    "green"     : (0,128,0),
    "lime"      : (0,255,0),
    "olive"     : (128,128,0),
    "yellow"    : (255,255,0),
    "navy"      : (0,0,128),
    "blue"      : (0,0,255),
    "teal"      : (0,128,128),
    "aqua"      : (0,255,255)
}

"""
Génère un tuple RGB
"""
def randomRGB():
    return (
        random.randint(0, 255), 
        random.randint(0, 255), 
        random.randint(0, 255))

"""
Convertie un tuple rgb qui a pour valeur 0 à 255 vers des valeurs entre 0 et 1
"""
def convert(rgb):
    r, g, b = rgbColor
    rgbConverted = (r / 255, g / 255, b / 255)
    return rgbConverted

"""
On détermine à partir d'un couleur en RGB son nom associé
(Ici on réalise exactement l'opération que le réseau de neurone sera amené à effectuer plus tard)
"""
def closest_color(rgb):
    r, g, b = rgb
    color_diffs = []
    for colorName in COLORS:
        cr, cg, cb = COLORS[colorName]
        color_diff = math.sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
        color_diffs.append((color_diff, COLORS[colorName], colorName))
    return min(color_diffs)[2]

"""
Génère un fichier nommé Dataset.csv
Il contient 4 colonnes: R, G, B, ColorName
"""
with open('Dataset.csv', 'w', newline='') as csvfile:
    csvFile = csv.writer(csvfile, delimiter=',')

    print("Create a dataset of: " + sys.argv[1] + " called Dataset.csv")
    for i in range(int(sys.argv[1])):
        rgbColor = randomRGB()
        r, g, b = rgbColor
        rgbConverted = convert(rgbColor)
        rc, gc, bc = rgbConverted
        csvFile.writerow([rc, gc, bc, closest_color((r, g, b))])