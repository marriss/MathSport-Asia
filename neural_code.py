# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 15:43:44 2018

@author: vishal vish
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 14:24:26 2018

@author: vishal vish
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 22:38:39 2018

@author: vishal vish
"""

# Artificial Neural Network

# Installing Theano
# pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

# Installing Tensorflow
# pip install tensorflow

# Installing Keras
# pip install --upgrade keras

# Part 1 - Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_excel('r and w 1-6,7-10,11-15.xlsx')
X = dataset.iloc[:, 0:9].values#since upperbound is excluded
y = dataset.iloc[:, 9].values




"""from sklearn.preprocessing import LabelEncoder, OneHotEncoder
#labelencoder_X_1 = LabelEncoder()
#X[:, 0] = labelencoder_X_1.fit_transform(X[:, 0])

labelencoder_X_2 = LabelEncoder()
y = labelencoder_X_2.fit_transform(y)

onehotencoder = OneHotEncoder(categorical_features = [1]) #to create the dummy variables.
y = onehotencoder.fit_transform(y).toarray()
y = [:, 1:]"""


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split  #cross validation is replaced by model selection.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Part 2 - Now let's make the ANN!

# Importing the Keras libraries and packages
import keras
from keras.models import Sequential#to initialise our NN
from keras.layers import Dense#to build layers of our ANN

# Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(units = 12, kernel_initializer = 'uniform', activation = 'relu', input_dim = 9))
"""output dim is the no of nodes in hidden layer
(basically avg of input and output no of nodes......
but we will study more in cross validation technique...part 10
initializer=for the weights),"""
# Adding the second hidden layer
classifier.add(Dense(units = 12, kernel_initializer = 'uniform', activation = 'relu'))
classifier.add(Dense(units = 12, kernel_initializer = 'uniform', activation = 'relu'))
# Adding the output layer
classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'softmax'))#if categorical data then see video for activation 

# Compiling the ANN(applying stochastic gradient desent)
classifier.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])#if categorical data then see video for loss funtion

# Fitting the ANN to the Training set
classifier.fit(X_train, y_train, batch_size = 1, epochs = 1000)

# Part 3 - Making predictions and evaluating the model

# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)



#home work
