
# TP - Énoncé - Reconnaissance de couleurs 🏳‍🌈

## 0 - Objectifs

L'objectif de ce TP est de réaliser une application Python de reconnaissance de couleurs. On cherche à pouvoir déterminer la classe de couleur (au format texte) à laquelle appartient une couleur RGB.

Quelques exemples de fonctionnement de l'application :

| R (in) | G (in) | B (in) | Couleur la plus proche (out) |
|--------|--------|--------|------------------------------|
| 240    | 5      | 2      | 🟥 Rouge                     |
| 255    | 5      | 250    | 🟪 Fuschia                   |
| 0      | 120    | 0      | 🟩 Vert                      |

L'idée ici est donc de concevoir un premier programme qui va générer un dataset de couleurs, puis un second intégrant un réseau de neuronnes qui va apprendre à reconnaître les couleurs par lui-même, avec un taux d'erreur minime. Enfin, vous comparerez la performance des deux programmes pour déterminer lequel est le plus efficace.

## 1 - Prérequis

Vous devez réaliser ce TP en Python, nous vous recommandons d'utiliser **[Python 3](https://www.python.org/downloads/)** pour éviter des problèmes de compatibilité avec les librairies requises.

Pensez à installer, avant la séance, les librairies **[pandas](https://gifts.worldwildlife.org/gift-center/gifts/Species-Adoptions/Panda.aspx?sc=AWY2005OQ18318A03785RX&_ga=2.160781181.1170045420.1668093542-311135590.1668093541)** et **[tensorflow_datasets](https://www.tensorflow.org/tutorials/quickstart/beginner)** (data generation), ainsi que **[sklearn](https://scikit-learn.org/stable/getting_started.html)** (data management).

https://pandas.pydata.org/


## 2 - Génération du dataset

*Votre environnement de dev est prêt ? Alors c'est parti, on peut commencer à mettre les mains dans le cambouis !*

Avant de pouvoir entraîner le modèle de notre application, on a besoin de données à lui fournir.

> 💡 **Remarque** : il ne vous aura pas échappé que le problème abordé dans ce TP est très simpliste... Dans les faits, cette simplicité permet de :
>  - générer des datasets complets (variables explicatives / à expliquer) à l'aide d'un algorithme "classique"
>  - pouvoir adapter la taille du dataset pour observer les changements de comportements de notre modèle

Le code ci-dessous permet de générer un dataset à la taille voulue : 

```python
import csv
import random
import sys
import math

import tensorflow_datasets as tfds
import pandas as pd


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


def random_rgb():
    """
    Génère un tuple RGB.
    """
    return (
        random.randint(0, 255), 
        random.randint(0, 255), 
        random.randint(0, 255))


def convert(rgb):
    """
    Convertie un tuple rgb qui a pour valeur 0 à 255 vers des valeurs entre 0 et 1.
    """
    r, g, b = rgb
    return r / 255, g / 255, b / 255


def closest_color(rgb):
    """
    On détermine à partir d'un couleur en RGB son nom associé
    (ici on réalise exactement l'opération que le réseau de neurone sera amené à effectuer plus 
    tard).
    """
    r, g, b = rgb
    color_diffs = []
    for color_name in COLORS:
        cr, cg, cb = COLORS[color_name]
        color_diff = math.sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
        color_diffs.append((color_diff, COLORS[color_name], color_name))
    return min(color_diffs)[2]
```
## 3 - Préparation des données

Maintenant que vos données sont prêtes, vous allez les préparer pour faciliter leur traitement.

 - a) Ramenez les valeurs du dataset entre 0 et 1.
 - b) Séparez les variables explicatives "X" et à expliquer "Y".
 - c) Séparez le dataset en lots d'entrainement (train) et de test (test) pour vous retrouver avec les variables : 
   - **X_train**
   - **Y_train**
   - **X_test**
   - **Y_test**

> 💡 Remarque : pensez à utiliser la librairie **[sklearn](https://scikit-learn.org/stable/getting_started.html)** pour la séparation des données

## 4 - Création du modèle

### **TensorFlow** (pour les curieux 🔎)
TensorFlow est une bibliothèque open source de Machine Learning, créée par Google, permettant de développer et d’exécuter des applications de Machine Learning et de Deep Learning. 

### **Keras** (pour les curieux 🔎)

Keras est une API de réseau de neurones écrite en langage Python. Il s’agit d’une bibliothèque Open Source, qui est exécutée au dessus du framework TensorFlow.

Aujourd’hui, Keras est l’une des APIs de réseaux de neurones les plus utilisées pour le développement et le testing de réseaux de neurones. Elle permet de créer très facilement des "layers" pour les réseaux de neurnes ou de mettre en place des architectures complexes.

### **Du code, du code, on veut coder !!** 🤪

... débrouille toi. 
> [TODO]


## 5 - Entraînement du modèle

## 6 - Evaluation du modèle

## 7 - Prédictions


# Classification de couleurs en machine learning

## Plan

### Génération du dataset
- Utilisation de notre outil pour assembler le dataset
- Options disponibles pour altérer le dataset avec des données incohérentes

### Séparation des données
- Utilisation de la librairie pandas pour importer les données
- Séparation des données :
  - Jeu de test
  - Jeu de validation 

### Génération et entrainement du modèle
- Utilisation de la librairie TensorFlow (Keras) pour générer et entrainer le modèle
  
### Évaluation / Performance du modèle 🚽
- Utilisation de la fonction de prédiction
- Utilisation de la fonction evaluate pour déterminer la précision 
- Comparaison avec un algorithme "classic" (utilisé pour la génération du dataset) 
  - Performances
  - Coût énergétique
