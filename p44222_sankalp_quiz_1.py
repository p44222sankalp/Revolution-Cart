# -*- coding: utf-8 -*-
"""P44222_Sankalp_Quiz_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19AP4hZZveRquM0TI4V4XSPjxywzwk50_
"""

# prompt: import pandas

import pandas as pd

# prompt: import file /content/Sankalp C G - revolutioncart_data.csv


df = pd.read_csv('/content/Sankalp C G - revolutioncart_data.csv')

df

# prompt: Consider monthly_revenue as y and rest as x

X = df.drop('monthly_revenue', axis=1)
y = df['monthly_revenue']

# prompt: split the x and y into training and test

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# prompt: use linear regression model

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Create a Linear Regression model
model = LinearRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# prompt: check accuracy

from sklearn.metrics import r2_score

# Calculate the R-squared score
r2 = r2_score(y_test, y_pred)
print(f"R-squared Score: {r2}")

# prompt: do cross validation

from sklearn.model_selection import cross_val_score

# Perform cross-validation
cv_scores = cross_val_score(model, X, y, cv=5)  # Use 5-fold cross-validation

# Print the cross-validation scores
print("Cross-Validation Scores:", cv_scores)

# Print the mean and standard deviation of the cross-validation scores
print("Mean CV Score:", cv_scores.mean())
print("Standard Deviation of CV Scores:", cv_scores.std())

# prompt: use lasso regression model

from sklearn.linear_model import Lasso

# Create a Lasso Regression model
lasso_model = Lasso(alpha=0.1)  # You can adjust the alpha parameter

# Train the model on the training data
lasso_model.fit(X_train, y_train)

# Make predictions on the test data
y_pred_lasso = lasso_model.predict(X_test)

# Calculate the R-squared score for Lasso
r2_lasso = r2_score(y_test, y_pred_lasso)
print(f"Lasso R-squared Score: {r2_lasso}")

# Perform cross-validation with Lasso
cv_scores_lasso = cross_val_score(lasso_model, X, y, cv=5)

# Print the cross-validation scores for Lasso
print("Lasso Cross-Validation Scores:", cv_scores_lasso)
print("Lasso Mean CV Score:", cv_scores_lasso.mean())
print("Lasso Standard Deviation of CV Scores:", cv_scores_lasso.std())

# prompt: do cross validation for lasso model

# Perform cross-validation with Lasso
cv_scores_lasso = cross_val_score(lasso_model, X, y, cv=5)

# Print the cross-validation scores for Lasso
print("Lasso Cross-Validation Scores:", cv_scores_lasso)
print("Lasso Mean CV Score:", cv_scores_lasso.mean())
print("Lasso Standard Deviation of CV Scores:", cv_scores_lasso.std())

# prompt: use ridge regression model

from sklearn.linear_model import Ridge

# Create a Ridge Regression model
ridge_model = Ridge(alpha=1.0)  # You can adjust the alpha parameter

# Train the model on the training data
ridge_model.fit(X_train, y_train)

# Make predictions on the test data
y_pred_ridge = ridge_model.predict(X_test)

# Calculate the R-squared score for Ridge
r2_ridge = r2_score(y_test, y_pred_ridge)
print(f"Ridge R-squared Score: {r2_ridge}")

# Perform cross-validation with Ridge
cv_scores_ridge = cross_val_score(ridge_model, X, y, cv=5)

# Print the cross-validation scores for Ridge
print("Ridge Cross-Validation Scores:", cv_scores_ridge)
print("Ridge Mean CV Score:", cv_scores_ridge.mean())
print("Ridge Standard Deviation of CV Scores:", cv_scores_ridge.std())

# prompt: use elasticnet model

from sklearn.linear_model import ElasticNet

# Create an ElasticNet model
elasticnet_model = ElasticNet(alpha=0.1, l1_ratio=0.5)  # Adjust alpha and l1_ratio as needed

# Train the model on the training data
elasticnet_model.fit(X_train, y_train)

# Make predictions on the test data
y_pred_elasticnet = elasticnet_model.predict(X_test)

# Calculate the R-squared score for ElasticNet
r2_elasticnet = r2_score(y_test, y_pred_elasticnet)
print(f"ElasticNet R-squared Score: {r2_elasticnet}")

# Perform cross-validation with ElasticNet
cv_scores_elasticnet = cross_val_score(elasticnet_model, X, y, cv=5)

# Print the cross-validation scores for ElasticNet
print("ElasticNet Cross-Validation Scores:", cv_scores_elasticnet)
print("ElasticNet Mean CV Score:", cv_scores_elasticnet.mean())
print("ElasticNet Standard Deviation of CV Scores:", cv_scores_elasticnet.std())

# prompt: use linear regression model

# You already have a Linear Regression model created and trained earlier in the code.
# If you want to use it for predictions, you can do the following:

# Make predictions on new data (e.g., X_test)
y_pred_linear = model.predict(X_test)

# Evaluate the model's performance (e.g., R-squared, MSE)
r2_linear = r2_score(y_test, y_pred_linear)
print(f"Linear Regression R-squared Score: {r2_linear}")

# You can also access the model's coefficients and intercept:
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

# prompt: measure accuracy for linear regression model

from sklearn.metrics import mean_absolute_error, mean_squared_error

# Assuming you have already trained your linear regression model and have y_test and y_pred_linear

# Calculate Mean Absolute Error (MAE)
mae = mean_absolute_error(y_test, y_pred_linear)
print(f"Mean Absolute Error (MAE): {mae}")

# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred_linear)
print(f"Mean Squared Error (MSE): {mse}")

# Calculate Root Mean Squared Error (RMSE)
rmse = mean_squared_error(y_test, y_pred_linear, squared=False)
print(f"Root Mean Squared Error (RMSE): {rmse}")

# You can also calculate other metrics like R-squared, as you already have in your code.

# prompt: do cross validation for linear regression model

from sklearn.model_selection import cross_val_score

# Assuming 'model' is your LinearRegression model and 'X' and 'y' are your data
cv_scores = cross_val_score(model, X, y, cv=5)  # Use 5-fold cross-validation

# Print the cross-validation scores
print("Cross-Validation Scores:", cv_scores)

# Print the mean and standard deviation of the cross-validation scores
print("Mean CV Score:", cv_scores.mean())
print("Standard Deviation of CV Scores:", cv_scores.std())

# prompt: dump model

import pickle

# Save the model to a file
filename = 'linear_regression_model.pkl'
pickle.dump(model, open(filename, 'wb'))

print(f"Model saved to {filename}")

#Linear Regression Model is considered as it showed higher accuracy
