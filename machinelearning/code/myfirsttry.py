from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split 

boston_dataset = load_boston()
print(boston_dataset)
X = boston_dataset.data
Y = boston_dataset.target

feature_Names = boston_dataset.feature_names

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.4, random_state=1) 

