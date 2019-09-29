import os
import random
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color, transform
from matplotlib.colors import Normalize

from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import GridSearchCV

#####################################################
# Load and preprocess data
namelist = os.listdir('/Users/alexanderyoung/Desktop/SampleImages/pics')
dir = os.getcwd();
total = []

y = []

for i in namelist:
    if i!=".DS_Store":
        if (i[0]=="P"):
            y.append(0)
        elif (i[0]=="A"):
            y.append(1)
        filepath=dir+"/pics/"+i
        img = io.imread(filepath, 'tiff')

        #Image already in grayscale

        #Resize gray image
        img_resized = transform.resize(img, (60,80))
    
        #Convert image to 1D array
        img_1d = np.concatenate(img_resized, 0)
        total.append(img_1d)

X = total

X_2d = X
y_2d = y

scaler = StandardScaler()
X = scaler.fit_transform(X)
X_2d = scaler.fit_transform(X_2d)

##########################################################
# Train classifiers

X_train=X_2d
X_test=[]
y_train=y_2d
y_test=[]
currentsize = len(X_train)
for x in range(int(len(X_2d)*0.4)):
    rand = random.randint(0,currentsize-2)
    # print "loop rand values", rand, X_train[rand], y_train[rand]
    X_test.append(X_train[rand])
    X_train=np.delete(X_train,rand,0)
    y_test.append(y_train[rand])
    y_train=np.delete(y_train,rand,0)
    currentsize=currentsize-1

# print X_test, y_test

C_range = np.logspace(-2, 10, 13)
gamma_range = np.logspace(-9, 3, 13)
param_grid = dict(gamma=gamma_range, C=C_range)
cv = StratifiedShuffleSplit(n_splits=10, test_size=0.6, random_state=42)
grid = GridSearchCV(SVC(), param_grid=param_grid, cv=cv)
grid.fit(X_train, y_train)
bestC = grid.best_params_["C"]
bestgam = grid.best_params_["gamma"]
print("The best parameters are %s with a score of %0.2f"
      % (grid.best_params_, grid.best_score_))

####################################################
#Decision function

plt.figure(figsize=(8, 6))
bestclf = SVC(C=bestC, gamma=bestgam)
bestclf.fit(X_train, y_train)
decision = bestclf.decision_function(X_test)
print "Decision (distances from hyperplane):", decision
print sum(decision)/len(decision)
# predict = bestclf.predict(X_test)
# print "Predict (classifications):", predict
score = bestclf.score(X_test,y_test)
print "Score (accuracy of svm):", score

