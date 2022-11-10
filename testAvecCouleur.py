# first neural network with keras make predictions
from numpy import loadtxt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# load the dataset
dataset = loadtxt('Dataset.csv', delimiter=',')
dataset_test = loadtxt('Dataset-test.csv',delimiter=',')

# split into input (X) and output (y) variables
X = dataset[:,0:4]
y = dataset[:,4]

X_test = dataset_test[:,0:4]
y_test = dataset_test[:,4]

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
