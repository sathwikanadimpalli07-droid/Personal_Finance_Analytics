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
print(users.head())
print(accounts.head())
print(transactions.head())
print(budget.head())
print(investment.head())
print(savings_goals.head())
print(users.dtypes)
print(accounts.dtypes)
print(transactions.dtypes)
print(budget.dtypes)
print(investment.dtypes)
print(savings_goals.dtypes)