import pandas as pd
from sqlalchemy import create_engine
engine = create_engine(
    "mysql+mysqlconnector://root:12345@localhost/personal_finance_analytics"
)
users = pd.read_sql("SELECT * FROM users",engine)
accounts = pd.read_sql("SELECT * FROM accounts",engine)
transactions = pd.read_sql("SELECT * FROM transactions",engine)
budget = pd.read_sql("SELECT * FROM budget",engine)
investment = pd.read_sql("SELECT * FROM investment",engine)
savings_goals = pd.read_sql("SELECT * FROM savings_goals",engine)

users["registration_date"] = pd.to_datetime(users["registration_date"])
transactions["transaction_date"] = pd.to_datetime(transactions["transaction_date"])
investment["purchase_date"] = pd.to_datetime(investment["purchase_date"])
savings_goals["deadline"] = pd.to_datetime(savings_goals["deadline"])

users["name"] = users["name"].str.strip()
users["city"] = users["city"].str.strip()
users["occupation"] = users["occupation"].str.strip()
users["gender"] = users["gender"].str.strip()
accounts["bank_name"] = accounts["bank_name"].str.strip()
accounts["account_type"] = accounts["account_type"].str.strip()
transactions["type"] = transactions["type"].str.strip()
transactions["category"] = transactions["category"].str.strip()
transactions["payment_mode"] = transactions["payment_mode"].str.strip()
transactions["description"] = transactions["description"].str.strip()
budget["category"] = budget["category"].str.strip()
investment["investment_type"] = investment["investment_type"].str.strip()
savings_goals["goal_name"] = savings_goals["goal_name"].str.strip()

users["name"] = users["name"].str.title()
users["city"] = users["city"].str.title()
users["occupation"] = users["occupation"].str.title()
users["gender"] = users["gender"].str.title()
accounts["bank_name"] = accounts["bank_name"].str.title()
accounts["account_type"] = accounts["account_type"].str.title()
transactions["type"] = transactions["type"].str.title()
transactions["category"] = transactions["category"].str.title()
transactions["payment_mode"] = transactions["payment_mode"].str.title()
budget["category"] = budget["category"].str.title()
investment["investment_type"] = investment["investment_type"].str.title()
savings_goals["goal_name"] = savings_goals["goal_name"].str.title()

Q1 = users["age"].quantile(0.25)
Q3 = users["age"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
age_outliers = users[
    (users["age"] < lower) |
    (users["age"] > upper)
]
print(age_outliers)

Q1 = accounts["current_balance"].quantile(0.25)
Q3 = accounts["current_balance"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
account_outliers = accounts[
    (accounts["current_balance"] < lower) |
    (accounts["current_balance"] > upper)
]
print(account_outliers)

Q1 = transactions["amount"].quantile(0.25)
Q3 = transactions["amount"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
transaction_outliers = transactions[
    (transactions["amount"] < lower) |
    (transactions["amount"] > upper)
]
print(transaction_outliers)

Q1 = budget["monthly_limit"].quantile(0.25)
Q3 = budget["monthly_limit"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
budget_outliers = budget[
    (budget["monthly_limit"] < lower) |
    (budget["monthly_limit"] > upper)
]
print(budget_outliers)

Q1 = investment["amount"].quantile(0.25)
Q3 = investment["amount"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
investment_outliers = investment[
    (investment["amount"] < lower) |
    (investment["amount"] > upper)
]
print(investment_outliers)

Q1 = savings_goals["target_amount"].quantile(0.25)
Q3 = savings_goals["target_amount"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
savings_outliers = savings_goals[
    (savings_goals["target_amount"] < lower) |
    (savings_goals["target_amount"] > upper)
]
print(savings_outliers)

print(users["user_id"].duplicated().sum())
print(accounts["account_id"].duplicated().sum())
print(transactions["transaction_id"].duplicated().sum())
print(budget["budget_id"].duplicated().sum())
print(investment["investment_id"].duplicated().sum())
print(savings_goals["goal_id"].duplicated().sum())


users.to_csv(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\cleaned_data\clean_users.csv", index=False)
accounts.to_csv(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\cleaned_data\clean_accounts.csv", index=False)
transactions.to_csv(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\cleaned_data\clean_transactions.csv", index=False)
budget.to_csv(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\cleaned_data\clean_budget.csv", index=False)
investment.to_csv(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\cleaned_data\clean_investment.csv", index=False)
savings_goals.to_csv(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\cleaned_data\clean_savings_goals.csv", index=False)

print("All cleaned datasets have been saved successfully.")

# Empty DataFrame
# Columns: [user_id, name, age, gender, occupation, city, registration_date]
# Index: []
# Empty DataFrame
# Columns: [account_id, user_id, bank_name, account_type, opening_balance, current_balance]
# Index: []
#        transaction_id  account_id transaction_date    amount  \
# 3                   4          36       2025-07-15  166806.0   
# 6                   7         152       2026-06-07   76165.0   
# 9                  10         687       2025-09-19  166095.0   
# 11                 12         785       2026-07-02  109438.0   
# 29                 30         952       2025-12-22   85883.0   
# ...               ...         ...              ...       ...   
# 49950           49951         148       2025-06-14  128419.0   
# 49951           49952          17       2024-10-11  180249.0   
# 49957           49958         469       2026-04-26   97086.0   
# 49971           49972         158       2025-11-19   82267.0   
# 49978           49979         571       2025-09-29  190178.0   

#                  category    type payment_mode  \
# 3                Business  Income   Debit Card   
# 6      Investment Returns  Income         Cash   
# 9               Freelance  Income  Net Banking   
# 11                 Salary  Income   Debit Card   
# 29              Freelance  Income          Upi   
# ...
# 0
# 0
# 0
# All cleaned datasets have been saved successfully.
# Output is truncated. View as a scrollable element or open in a text editor. Adjust cell output settings...