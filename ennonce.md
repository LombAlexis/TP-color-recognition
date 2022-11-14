
# TP - Énoncé - Reconnaissance de couleurs 🏳‍🌈

## 0 - Objectifs

L'objectif de ce TP est de réaliser une application Python de reconnaissance de couleurs. On cherche à pouvoir déterminer la classe de couleur (au format texte) à laquelle appartient une couleur RGB.

Quelques exemples de fonctionnement de l'application :

| R (in) | G (in) | B (in) | Couleur la plus proche (out) |
|--------|--------|--------|------------------------------|
| 240    | 5      | 2      | 🟥 Rouge                     |
| 255    | 5      | 250    | 🟪 Fuchsia                   |
| 0      | 120    | 0      | 🟩 Vert                      |

## 1 - Prérequis

Vous devez réaliser ce TP en Python, nous vous recommandons d'utiliser **[Python 3](https://www.python.org/downloads/)** pour éviter des problèmes de compatibilité avec les librairies requises.

Pensez à installer, avant la séance, les librairies **[pandas](https://gifts.worldwildlife.org/gift-center/gifts/Species-Adoptions/Panda.aspx?sc=AWY2005OQ18318A03785RX&_ga=2.160781181.1170045420.1668093542-311135590.1668093541)** et **[tensorflow](https://www.tensorflow.org/tutorials/quickstart/beginner)** (data generation), ainsi que **[sklearn](https://scikit-learn.org/stable/getting_started.html)** (data management).

https://pandas.pydata.org/


## 2 - Génération du dataset

*Votre environnement de dev est prêt ? Alors c'est parti, on peut commencer à mettre les mains dans le cambouis !*

Avant de pouvoir entraîner le modèle de notre application, on a besoin de données à lui fournir.

>
> 💡 **Remarque** : il ne vous aura pas échappé que le problème abordé dans ce TP est très simpliste... Dans les faits, cette simplicité permet de :
>  - générer des datasets complets (variables explicatives / à expliquer) à l'aide d'un algorithme "classique"
>  - pouvoir adapter la taille du dataset pour observer les changements de comportements de notre modèle
>

Le code ci-dessous permet de générer un dataset à la taille voulue : 

```python
import math
import random

import pandas as pd

# constantes

COLORS = {
    "black": (0, 0, 0),
    "silver": (192, 192, 192),
    "gray": (128, 128, 128),
    "white": (255, 255, 255),
    "maroon": (128, 0, 0),
    "red": (255, 0, 0),
    "purple": (128, 0, 128),
    "fuchsia": (255, 0, 255),
    "green": (0, 128, 0),
    "lime": (0, 255, 0),
    "olive": (128, 128, 0),
    "yellow": (255, 255, 0),
    "navy": (0, 0, 128),
    "blue": (0, 0, 255),
    "teal": (0, 128, 128),
    "aqua": (0, 255, 255)
}

Y_LABEL = "Value"


def random_rgb():
    """
    Génère un tuple RGB.
    """
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )


def to_decimal(rgb):
    """
    Convertie un tuple rgb qui a pour valeur 0 à 255 vers des valeurs entre -0.5 et 0.5.
    """
    r, g, b = rgb
    return (
        r / 255 - 0.5,
        g / 255 - 0.5,
        b / 255 - 0.5
    )

def to_hex(rgb):
    """
    Convertie un tuple rgb qui a pour valeur -0.5 à 0.5 vers des valeurs entre 0 et 255.
    """
    r, g, b = rgb
    return (
        int((r + 0.5) * 255),
        int((g + 0.5) * 255),
        int((b + 0.5) * 255)
    )


def closest_color(rgb):
    """
    Détermine à partir d'une couleur en RGB son nom associé.
    (ici on réalise exactement l'opération que le réseau de neurone sera amené à effectuer plus
    tard).
    """
    r, g, b = rgb
    color_diffs = []
    for color_name in COLORS:
        cr, cg, cb = COLORS[color_name]
        color_diff = math.sqrt((r - cr) ** 2 + (g - cg) ** 2 + (b - cb) ** 2)
        color_diffs.append((color_diff, COLORS[color_name], color_name))
    return min(color_diffs)[2]


def create_dataset(n):
    """
    Génère un dataset qui contient 4 colonnes: R, G, B, ColorName
    """
    dataset_array = []
    for _ in range(n):
        rgb_color = random_rgb()
        r, g, b = rgb_color
        rc, gc, bc = to_decimal(rgb_color)
        dataset_array.append([rc, gc, bc, closest_color((r, g, b))])
    return pd.DataFrame(data=dataset_array, columns=["R", "G", "B", Y_LABEL])
```
## 3 - Préparation des données

Maintenant que vos données sont prêtes, vous allez les préparer pour faciliter leur traitement, complétez le code ci-dessous :

 - a) Ramenez les valeurs du dataset entre 0 et 1.
 - b) Séparez les variables explicatives "X" et à expliquer "y".
 - c) Séparez le dataset en lots d'entrainement (train) et de test (test) pour vous retrouver avec les variables : 
   - **X_train**
   - **y_train**
   - **X_test**
   - **y_test**

> 💡 Remarque : pensez à utiliser la librairie **[sklearn](https://scikit-learn.org/stable/getting_started.html)** pour la séparation des données

```python
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

# Obtention des X
X = ds.loc[...] # complétez la méthode loc 

# Obtention d'y
le = preprocessing.LabelEncoder()
y = le.fit_transform(...)  # transformez les classes en valeurs numériques ("aqua" --> 0)
y = ...  # reconvertissez y en DataFrame Pandas

# Séparation des données d'entrainement et des données de test
...
```

## 4 - Création du modèle

### **TensorFlow** (pour les curieux 🔎)
TensorFlow est une bibliothèque open source de Machine Learning, créée par Google, permettant de développer et d’exécuter des applications de Machine Learning et de Deep Learning. 

### **Keras** (pour les curieux 🔎)

Keras est une API de réseau de neurones écrite en langage Python. Il s’agit d’une bibliothèque Open Source, qui est exécutée au-dessus du framework TensorFlow.

Aujourd’hui, Keras est l’une des APIs de réseaux de neurones les plus utilisées pour le développement et le testing de réseaux de neurones. Elle permet de créer très facilement des "layers" pour les réseaux de neurones ou de mettre en place des architectures complexes.

### **Du code, du code, on veut coder !!** 🤪

En Machine Learning, un modèle est une structure qui a été entraînée pour reconnaître certains types de données. 

Vous allez créer votre propre modèle, avec le nombre d'entrées et le nombre de sorties requises, qui aura pour objectif d'apprendre les différentes couleurs de votre dataset.

> 💡 **Remarque** : vous devrez choisir :
> - le nombre de couches internes 
> - le nombre de neurones
> - la fonction d'activation
> - la fonction de perte

a) Servez-vous des fonctions [Sequential()](https://keras.io/api/models/sequential/), [Input()](https://keras.io/api/layers/core_layers/input/), [Dense()](https://keras.io/api/layers/core_layers/dense/) de l'API Keras pour créer le modèle.

b) Compilez votre modèle à l'aide de la fonction [compile()](https://keras.io/api/models/model_training_apis/) avec l'argument d'optimisation "`adam`".


## 5 - Entraînement du modèle

Maintenant que les bases de notre modèle sont prêtes, on peut passer à la phase d'apprentissage. 
La fontion [fit()](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit) issue de `tf.keras.Model` permet d'entraîner simplement le modèle en offrant également un customisation assez poussée pour s'adapter à de nombreuses situations.

a) Servez-vous de cette fonction pour entraîner le modèle avec les données de la [partie 3](#3-préparation-des-données).

> 💸 **Tips** : les paramètres `epochs` et `batch_size` doivent être bien choisis, prenez le temps de bien comprendre leur utilité à travers la documentation de [fit()](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit).

## 6 - Evaluation du modèle

a) Utilisez la fonction [evaluate()](https://www.tensorflow.org/api_docs/python/tf/keras/Model#evaluate) pour tester la partie test de votre dataset (`X_test` et `y_test`) dans l'objectif d'obtenir la **précision** et la **perte**  de votre modèle.

## 7 - Prédictions

a) Exécutez votre modèle sur une donnée aléatoire de votre dataset de test.  

b) Vérifiez si la couleur prédite correspond bien à la couleur attendue.

> 💡 **Remarque** : Aidez-vous de la fonction [predict()](https://www.tensorflow.org/api_docs/python/tf/keras/Model#predict)


