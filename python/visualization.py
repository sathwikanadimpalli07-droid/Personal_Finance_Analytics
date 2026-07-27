import pandas as pd
import matplotlib.pyplot as plt
users = pd.read_csv(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\feature_engineered_data\users_features.csv")
accounts = pd.read_csv(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\feature_engineered_data\accounts_features.csv")
transactions = pd.read_csv(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\feature_engineered_data\transactions_features.csv")
budget = pd.read_csv(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\feature_engineered_data\budget_features.csv")
investment = pd.read_csv(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\feature_engineered_data\investment_features.csv")
savings = pd.read_csv(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\feature_engineered_data\savings_features.csv")
financial = pd.read_csv(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\feature_engineered_data\financial_summary.csv")

age = users["age_group"].value_counts()
plt.figure(figsize=(8,5))
plt.bar(age.index.astype(str), age.values)
plt.title("Users by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Users")
plt.tight_layout()
plt.savefig(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\visualizations\users_by_age_group.png")
plt.show()

city = users["city"].value_counts()
plt.figure(figsize=(10,6))
plt.bar(city.index, city.values)
plt.title("Users by City")
plt.xlabel("City")
plt.ylabel("Users")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\visualizations\users_by_city.png")
plt.show()

occupation = users["occupation"].value_counts()
plt.figure(figsize=(10,5))
plt.bar(occupation.index, occupation.values)
plt.title("Users by Occupation")
plt.xlabel("Occupation")
plt.ylabel("Users")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\visualizations\users_by_occupation.png")
plt.show()

plt.figure(figsize=(8,5))
plt.hist(accounts["current_balance"], bins=25)
plt.title("Account Balance Distribution")
plt.xlabel("Balance")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\visualizations\balance_distribution.png")
plt.show()

balance = accounts["balance_category"].value_counts()
plt.figure(figsize=(6,5))
plt.bar(balance.index.astype(str), balance.values)
plt.title("Balance Categories")
plt.xlabel("Category")
plt.ylabel("Accounts")
plt.tight_layout()
plt.savefig(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\visualizations\balance_category.png")
plt.show()

month = transactions.groupby("month")["amount"].sum()
month = month.reindex([
"January","February","March","April","May","June",
"July","August","September","October","November","December"
])
plt.figure(figsize=(10,5))
plt.plot(month.index, month.values, marker="o")
plt.title("Monthly Transaction Amount")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\visualizations\monthly_transactions.png")
plt.show()

income = transactions[
transactions["type"]=="Income"
]["amount"].sum()
expense = transactions[
transactions["type"]=="Expense"
]["amount"].sum()
plt.figure(figsize=(6,5))
plt.bar(["Income","Expense"], [income,expense])
plt.title("Income vs Expense")
plt.ylabel("Amount")
plt.tight_layout()
plt.savefig(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\visualizations\income_vs_expense.png")
plt.show()

expense_category = (
transactions[
transactions["type"]=="Expense"
]
.groupby("category")["amount"]
.sum()
)
plt.figure(figsize=(10,5))
plt.bar(expense_category.index, expense_category.values)
plt.xticks(rotation=45)
plt.title("Expense by Category")
plt.tight_layout()
plt.savefig(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\visualizations\expense_by_category.png")
plt.show()

payment = transactions["payment_mode"].value_counts()
plt.figure(figsize=(8,5))
plt.pie(payment.values,
labels=payment.index,
autopct="%1.1f%%")
plt.title("Payment Mode Distribution")
plt.tight_layout()
plt.savefig(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\visualizations\payment_mode.png")
plt.show()

inv = investment["investment_type"].value_counts()
plt.figure(figsize=(8,5))
plt.bar(inv.index, inv.values)
plt.xticks(rotation=45)
plt.title("Investment Types")
plt.tight_layout()
plt.savefig(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\visualizations\investment_types.png")
plt.show()

plt.figure(figsize=(8,5))
plt.hist(investment["roi"], bins=20)
plt.title("ROI Distribution")
plt.xlabel("ROI")
plt.ylabel("Investments")
plt.tight_layout()
plt.savefig(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\visualizations\roi_distribution.png")
plt.show()

status = investment["profit_status"].value_counts()
plt.figure(figsize=(6,5))
plt.pie(
status.values,
labels=status.index,
autopct="%1.1f%%"
)
plt.title("Profit vs Loss")
plt.tight_layout()
plt.savefig(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\visualizations\profit_loss.png")
plt.show()

plt.figure(figsize=(8,5))
plt.hist(
savings["completion_percentage"],
bins=20
)
plt.title("Savings Goal Completion")
plt.xlabel("Completion %")
plt.ylabel("Users")
plt.tight_layout()
plt.savefig(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\visualizations\savings_completion.png")
plt.show()

plt.figure(figsize=(8,5))
plt.hist(
financial["savings_rate"],
bins=20
)
plt.title("Savings Rate")
plt.tight_layout()
plt.savefig(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\visualizations\savings_rate.png")
plt.show()

plt.figure(figsize=(8,5))
plt.hist(
    financial["budget_utilization"],
    bins=20
)
plt.title("Budget Utilization")
plt.xlabel("Budget Utilization (%)")
plt.ylabel("Users")
plt.tight_layout()
plt.savefig(r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\visualizations\Budget_utilization.png")
plt.show()