import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
from sklearn.ensemble import RandomForestRegressor
import joblib
financial = pd.read_csv(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\financial_health\financial_health_score.csv")
X = financial[
[
"total_income",
"total_investment",
"current_savings",
"total_budget",
"savings_rate",
"investment_rate",
"budget_utilization",
"goal_completion",
"financial_health_score"
]
]
y = financial["total_expense"]
X.fillna(0, inplace=True)
y.fillna(0, inplace=True)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
print(X_train.shape)
print(X_test.shape)
model=RandomForestRegressor(
    n_estimators=100,
    random_state=42
)
model.fit(
X_train,
y_train
)
predictions = model.predict(X_test)
print(predictions[:10])
mae = mean_absolute_error(
y_test,
predictions
)
print("MAE =", mae)
mse = mean_squared_error(
y_test,
predictions
)
print("MSE =", mse)
rmse = np.sqrt(mse)
print("RMSE =", rmse)
r2 = r2_score(
y_test,
predictions
)
print("R2 Score =", r2)
comparison = pd.DataFrame({
"Actual Expense": y_test,
"Predicted Expense": predictions
})
print(comparison.head(20))
importance = pd.DataFrame({
"Feature": X.columns,
"Importance": model.feature_importances_
})
importance = importance.sort_values(
by="Importance",
ascending=False
)
print(importance)
comparison.to_csv(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\predictions\expense_predictions.csv",index=False)
joblib.dump(model,r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\models\expense_prediction_model.pkl")

#model = joblib.load(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\models\expense_prediction_model.pkl")

#total_income,total_expense,total_investment,current_savings,total_budget,savings_rate,investment_rate,budget_utilization,goal_completion,financial_health_score
#1040995.0,   551521.0,     1268592.0,       884519.0       ,239842.0,    47.02,       121.86,         229.9518016027218, 72.08,          66.24                
#2049179.0,   960044.0,     1436107.0,       83085.0,       0.0,          53.15,       70.08,          0.0,               7.17,           51.98

new_user = pd.DataFrame({
    "total_income": [2049179],
    "total_investment": [1436107],
    "current_savings": [83085],
    "total_budget": [0],
    "savings_rate": [53.15],
    "investment_rate": [70.08],
    "budget_utilization": [0],
    "goal_completion": [7.17],
    "financial_health_score": [51.98]
})
prediction = model.predict(new_user)
print("Predicted Expense =", prediction[0])