# Python program to demonstrate 
# KNN classification algorithm 
# on IRIS dataset
from sklearn.datasets import load_iris 
from sklearn.neighbors import KNeighborsClassifier 
import numpy as np 
from sklearn.model_selection import train_test_split 
  
# Loads the IRIS dataset
iris_dataset=load_iris() 
  
X_train, X_test, y_train, y_test = train_test_split(iris_dataset["data"], iris_dataset["target"], random_state=0) 

# Initialzes KNN classification instance
kn = KNeighborsClassifier(n_neighbors=1) 
kn.fit(X_train, y_train) 

# Creates a numpy Array
x_new = np.array([[5, 2.9, 1, 0.2]]) 
prediction = kn.predict(x_new) 
  
# prints the prediction for the target value
print("Predicted target value: {}\n".format(prediction)) 
# prints the feature name
print("Predicted feature name: {}\n".format
    (iris_dataset["target_names"][prediction])) 
#prints The test score
print("Test score: {:.2f}".format(kn.score(X_test, y_test))) 