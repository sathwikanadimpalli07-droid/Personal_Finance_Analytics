import pandas as pd
import numpy as np

users = pd.read_csv(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\cleaned_data\clean_users.csv")
accounts = pd.read_csv(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\cleaned_data\clean_accounts.csv")
transactions = pd.read_csv(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\cleaned_data\clean_transactions.csv")
budget = pd.read_csv(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\cleaned_data\clean_budget.csv")
investment = pd.read_csv(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\cleaned_data\clean_investment.csv")
savings_goals = pd.read_csv(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\cleaned_data\clean_savings_goals.csv")

users["registration_date"] = pd.to_datetime(users["registration_date"])
transactions["transaction_date"] = pd.to_datetime(transactions["transaction_date"])
investment["purchase_date"] = pd.to_datetime(investment["purchase_date"])

savings_goals["deadline"] = pd.to_datetime(savings_goals["deadline"])

users["age_group"] = pd.cut(
    users["age"],
    bins=[18,25,35,45,60],
    labels=["18-25","26-35","36-45","46-60"]
)
users["registration_year"] = users["registration_date"].dt.year
users["registration_month"] = users["registration_date"].dt.month_name()

accounts["balance_category"] = pd.cut(
    accounts["current_balance"],
    bins=[0,50000,150000,500000],
    labels=["Low","Medium","High"]
)

transactions["month"] = transactions["transaction_date"].dt.month_name()
transactions["month_number"] = transactions["transaction_date"].dt.month
transactions["year"] = transactions["transaction_date"].dt.year
transactions["quarter"] = transactions["transaction_date"].dt.quarter
transactions["day"] = transactions["transaction_date"].dt.day
transactions["weekday"] = transactions["transaction_date"].dt.day_name()
transactions["day_type"] = transactions["weekday"].apply(
    lambda x: "Weekend" if x in ["Saturday", "Sunday"] else "Weekday"
)
transactions["transaction_size"] = pd.cut(
    transactions["amount"],
    bins=[0,1000,5000,10000,50000],
    labels=["Small","Medium","Large","Very Large"]
)

investment["profit"] = (
    investment["current_value"] -
    investment["amount"]
)
investment["roi"] = (
    investment["profit"] /
    investment["amount"]
) * 100
investment["profit_status"] = investment["profit"].apply(
    lambda x: "Profit" if x >= 0 else "Loss"
)

savings_goals["completion_percentage"] = (
    savings_goals["current_amount"] /
    savings_goals["target_amount"]
) * 100
savings_goals["remaining_amount"] = (
    savings_goals["target_amount"] -
    savings_goals["current_amount"]
)
savings_goals["goal_status"] = savings_goals["completion_percentage"].apply(
    lambda x:
    "Completed" if x>=100
    else "Almost Complete" if x>=75
    else "Half Completed" if x>=50
    else "Started"
)

financial_summary = users[["user_id", "name"]].copy()
income = (
    transactions[transactions["type"] == "Income"]
    .merge(accounts[["account_id", "user_id"]], on="account_id")
    .groupby("user_id")["amount"]
    .sum()
    .reset_index()
)
income.rename(columns={"amount": "total_income"}, inplace=True)
print(income.head())
expense = (
    transactions[transactions["type"] == "Expense"]
    .merge(accounts[["account_id", "user_id"]], on="account_id")
    .groupby("user_id")["amount"]
    .sum()
    .reset_index()
)
expense.rename(columns={"amount": "total_expense"}, inplace=True)
print(expense.head())
investment_summary = (
    investment.groupby("user_id")["amount"]
    .sum()
    .reset_index()
)
investment_summary.rename(
    columns={"amount": "total_investment"},
    inplace=True
)
print(investment_summary.head())
current_value = (
    investment.groupby("user_id")["current_value"]
    .sum()
    .reset_index()
)
current_value.rename(
    columns={"current_value": "current_investment_value"},
    inplace=True
)
print(current_value.head())
target_summary = (
    savings_goals.groupby("user_id")["target_amount"]
    .sum()
    .reset_index()
)
target_summary.rename(
    columns={"target_amount": "total_target_amount"},
    inplace=True
)
print(target_summary.head())
current_summary = (
    savings_goals.groupby("user_id")["current_amount"]
    .sum()
    .reset_index()
)
current_summary.rename(
    columns={"current_amount": "current_savings"},
    inplace=True
)
print(current_summary.head())
budget_summary = (
    budget.groupby("user_id")["monthly_limit"]
    .sum()
    .reset_index()
)
budget_summary.rename(
    columns={"monthly_limit": "total_budget"},
    inplace=True
)
print(budget_summary.head())
financial_summary = financial_summary.merge(
    income,
    on="user_id",
    how="left"
)
financial_summary = financial_summary.merge(
    expense,
    on="user_id",
    how="left"
)
financial_summary = financial_summary.merge(
    investment_summary,
    on="user_id",
    how="left"
)
financial_summary = financial_summary.merge(
    current_value,
    on="user_id",
    how="left"
)
financial_summary = financial_summary.merge(
    target_summary,
    on="user_id",
    how="left"
)
financial_summary = financial_summary.merge(
    current_summary,
    on="user_id",
    how="left"
)
financial_summary = financial_summary.merge(
    budget_summary,
    on="user_id",
    how="left"
)
financial_summary.fillna(0, inplace=True)
financial_summary["net_savings"] = (
    financial_summary["total_income"] -
    financial_summary["total_expense"]
)
financial_summary["savings_rate"] = (
    financial_summary["net_savings"] /
    financial_summary["total_income"]
) * 100
financial_summary["savings_rate"] = (
    financial_summary["savings_rate"]
    .fillna(0)
    .round(2)
)
financial_summary["investment_rate"] = (
    financial_summary["total_investment"] /
    financial_summary["total_income"]
) * 100
financial_summary["investment_rate"] = (
    financial_summary["investment_rate"]
    .fillna(0)
    .round(2)
)
financial_summary["budget_utilization"] = (
    financial_summary["total_expense"] /
    financial_summary["total_budget"]
) * 100
financial_summary["budget_utilization"] = (
    financial_summary["budget_utilization"]
    .replace([np.inf, -np.inf], np.nan)
)
financial_summary["budget_utilization"] = (
    financial_summary["budget_utilization"]
    .fillna(0)
)
financial_summary["investment_profit"] = (
    financial_summary["current_investment_value"] -
    financial_summary["total_investment"]
)
financial_summary["goal_completion"] = (
    financial_summary["current_savings"] /
    financial_summary["total_target_amount"]
) * 100
financial_summary["goal_completion"] = (
    financial_summary["goal_completion"]
    .fillna(0)
    .round(2)
)
print(financial_summary.head())
print(financial_summary.info())
print(financial_summary.describe())




users.to_csv(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\feature_engineered_data\users_features.csv", index=False)
accounts.to_csv(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\feature_engineered_data\accounts_features.csv", index=False)
transactions.to_csv(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\feature_engineered_data\transactions_features.csv", index=False)
budget.to_csv(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\feature_engineered_data\budget_features.csv", index=False)
investment.to_csv(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\feature_engineered_data\investment_features.csv", index=False)
savings_goals.to_csv(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\feature_engineered_data\savings_features.csv", index=False)
financial_summary.to_csv(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\feature_engineered_data\financial_summary.csv", index=False)

print("Financial summary saved successfully!")