# Load libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

#
# Example.py, example2.py, and regressionexample.py
# are all example machine learning programs I use as reference and to learn the sklearn framework
# everything else are examples that I have built
# I Have added comments to the examples, but otherwise they remain the same
#

# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

# splits the data set up
array = dataset.values
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.20
seed = 7

# Test options and evaluation metric
seed = 7
scoring = 'accuracy'
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

# appends the different models for the models
models = []
# appends a logistic regression model
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
# Appends a linear discriminant anaylsis model
models.append(('LDA', LinearDiscriminantAnalysis()))
# Appends a K-nearest neighbors classificaton model
models.append(('KNN', KNeighborsClassifier()))
# Appends a decision tree model
models.append(('CART', DecisionTreeClassifier()))
# Appends a standard Gaussian Distribution model 
models.append(('NB', GaussianNB()))
# Appends a Support Vector Model
models.append(('SVM', SVC(gamma='auto')))

# evaluate each model in turn
results = []
names = []
for name, model in models:
	# splits data into ten equal folds for data testing
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	# Tests the data using cross validation
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	# Appends answer to results
	results.append(cv_results)
	# Appends name of model to names
	names.append(name)
	# Formats message to be printed comparing models
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)

# Plots the comparisons between the different algorithms 
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()

# Prints specifically the KNN (K-nearest neighbors model, being the most accurate for the data)
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))