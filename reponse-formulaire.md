# Correction du formulaire:

1) En tenant compte du travail effectué, quels sont les prérequis nécessaires pour utiliser un réseau de neurones ?

```
Il faut un dataset ou un générateur de dataset d'une grande taille.
Il faut aussi formater les données en supprimant toute donnée non numérique et aussi rendre les données numériques dans un intervalle comme -0.5-0.5 ou encore 0-1
```

2) A quoi correspond le paramètre `epochs` utilisé dans l'entraînement du modèle ?   

```
Le terme "epochs", correspond au nombre de fois que l'entraînement complet sera effectué.
Il est recommandé d'entraîner plusieurs fois le modèle pour qu'il soit plus précis.
```

3) Que faudrait-il faire pour que le modèle soit plus précis ?

- [x] Augmenter le nombre d'epoch 
- [ ] Diminuer le nombre d'epoch
- [x] Augmenter le batch size
- [ ] Diminuer le batch size
- [x] Augmenter le dataset
- [ ] Diminuer le dataset
- [ ] Avoir de meilleur composant
- [x] Augmenter le nombre de couche dans le modele 
- [ ] Diminuer le nombre de couche dans le modele 
- [ ] Mon modèle & préparation des données sont parfaits

4) L'apprentissage du modèle s'est-il fait de manière supervisée ou non supervisée ? Pourquoi ?

```
Elle s'est fait de manière supervisée car il s'agit d'un dataset dont on contrôle les données
```

5) Quels sont les meilleurs pourcentages de découpage du dataset ? (entrainement, test)

```
Le meilleur découpage en général est 85% et 15%.
```

6) Pouvez-vous citer les 3 groupes (layer, output, input) qui caractérisent un réseau neuronal  (image ci-dessous) ?
![](https://imgur.com/Y30MDF0.jpg)


Détailler brièvement le rôle de chaque groupe.

```
La partie rouge correspond à "input". C'est données d'entrées vont être le dataset.
La partie bleue est "layer". Cela va être le modèle. Celui-ci va posséder (généralement plusieurs couches).
Enfin la partie verte est l"output". C'est le résultat de la prédiction de la machine.
```