import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

# loading the dataset
diabetes=datasets.load_diabetes()
print(diabetes.data.shape)
print(diabetes.target.shape)

# train-test-split
from sklearn.model_selection import train_test_split # auto-shuffled, 
# random_state = seed used by random number generator
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X=scaler.fit_transform(diabetes.data)

X_train,X_test,Y_train,Y_test=train_test_split(X,diabetes.target,test_size=0.3,random_state=50)
print(X_train.shape)
print(Y_train.shape)
print(X_test.shape)
print(Y_test.shape)

# creating model - fit / predict / accuracy
from sklearn.linear_model import LinearRegression

model=LinearRegression(fit_intercept=True,normalize=True)
model.fit(X_train,Y_train)
Y_train_pred=model.predict(X_train)
Y_test_pred=model.predict(X_test)

from sklearn.metrics import r2_score # r2_score & model.score are same

print(r2_score(Y_train,Y_train_pred))
print(r2_score(Y_test,Y_test_pred))
print(model.score(X_train,Y_train)) # this is better - we don't have to find Y_train_pred
print(model.score(X_test,Y_test))

# calculating cost
from sklearn.metrics import mean_squared_error # for cost

print(mean_squared_error(Y_train,Y_train_pred))
print(mean_squared_error(Y_test,Y_test_pred))

# plotting the curve

# training set plot
fig, ax = plt.subplots()
ax.scatter(Y_train,Y_train_pred, edgecolors=(0, 0, 0))
ax.plot([Y_train.min(), Y_train.max()], [Y_train.min(), Y_train.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()

# test set plot
fig, ax = plt.subplots()
ax.scatter(Y_test,Y_test_pred, color='green')
ax.plot([Y_test.min(), Y_test.max()], [Y_test.min(), Y_test.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()