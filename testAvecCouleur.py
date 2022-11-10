# first neural network with keras make predictions
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import pandas as pd
import random
import sys
import math

"""
#####################################################
        Générateur de dataset (CSV) fonctions
#####################################################
"""


"""
Correspondances entre nom de couleurs et valeurs en (r,g,b)
Représentation sous forme de dictionnaire
"""
COLORS = {
    "aqua"      : (0,255,255),
    "black"     : (0,0,0),
    "blue"      : (0,0,255),
    "fuchsia"   : (255,0,255),
    "gray"      : (128,128,128),
    "green"     : (0,128,0),
    "lime"      : (0,255,0),
    "maroon"    : (128,0,0),
    "navy"      : (0,0,128),
    "olive"     : (128,128,0),
    "purple"    : (128,0,128),
    "red"       : (255,0,0),
    "silver"    : (192,192,192),
    "teal"      : (0,128,128),
    "white"     : (255,255,255),
    "yellow"    : (255,255,0)
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

#####################################################
#       Générateur de dataset (CSV) - main          #
#####################################################

"""
Génère un fichier nommé Dataset.csv
Il contient 4 colonnes: R, G, B, ColorName
"""
with open('Dataset.csv', 'w', newline='') as csvfile:
    
    dataset_array = []
    for i in range(int(sys.argv[1])):
        rgbColor = randomRGB()
        r, g, b = rgbColor
        rgbConverted = convert(rgbColor)
        rc, gc, bc = rgbConverted
        dataset_array.append([rc, gc, bc, closest_color((r, g, b))])


"""
Separate the data, and add the some label for each column
"""
if __name__=="__main__":
    dataset = pd.DataFrame(data=dataset_array,columns=["R", "G", "B", "Value"])

    # Remplace la valeur en string d'une couleur par son indice correspondant ("aqua" --> 0)
    le = preprocessing.LabelEncoder()
    le.fit(list(COLORS.keys()))
    
    #Transforme les valeurs de la colonne Value du dataset en leur valeur numérique à partir de ce qui a été fit dans le LabelEncoder
    dataset['Value'] = le.transform(dataset.get("Value"))

    # Séparation des données de test, des données d'entrainement
    X_train, X_test = train_test_split(dataset,test_size=0.2)

    # Separer la variable qualitative 
    Y_train = X_train.copy()
    
    Y_train = Y.drop(Y.columns[[0,1,2,]],axis=1)
    X_train = X.drop(X.columns[[3]],axis=1)

    Y_test = X_test.copy()

    Y_test = Y_test.drop(Y.columns[[0,1,2,]],axis=1)
    X_test = X_test.drop(X.columns[[3]],axis=1)
    
    


    exit()
    # # load the dataset
    # dataset = loadtxt('Dataset.csv', delimiter=',')
    # dataset_test = loadtxt('Dataset-test.csv',delimiter=',')
    # split into input (X) and output (y) variables
    X = dataset[:,0:4]

    y = dataset[:,4]

    X_test = dataset_test[:,0:4]
    y_test = dataset_test[:,4]

    #Passage les donnes qui sont en string en chiffre

    # define the keras model
    model = Sequential()
    model.add(Dense(12, input_shape=(4,), activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    # compile the keras model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    # fit the keras model on the dataset
    model.fit(X, y, epochs=150, batch_size=10, verbose=0)
    # make class predictions with the model
    predictions = (model.predict(X_test) > 0.5).astype(int)
    # evaluate the keras model
    _, accuracy = model.evaluate(X, y)
    print('Accuracy: %.2f' % (accuracy*100))
    # summarize the first 5 cases
    compte = 0
    for i in range(69):
        if(predictions[i] == y_test[i]):
            compte+=1
        print('%s => %d (expected %d)' % (X_test[i].tolist(), predictions[i], y_test[i]))

    print("Compte = " + str(compte))



