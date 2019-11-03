from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split 
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

boston_dataset = load_boston()
print(boston_dataset)

X = boston_dataset.data[:, np.newaxis, 7]
Y = boston_dataset.target
feature_Names = boston_dataset.feature_names
print(feature_Names)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.4, random_state=1) 

regr = linear_model.LinearRegression()
regr.fit(X_train, y_train)

house_y_pred = regr.predict(X_test)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(y_test, house_y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(y_test, house_y_pred))

# Plot outputs
plt.scatter(X_test, y_test,  color='black')
plt.plot(X_test, house_y_pred, color='blue', linewidth=3)
plt.title('Housing price')
plt.ylabel("Price")
plt.xlabel('AGE')

plt.xticks(())
plt.yticks(())

plt.show()