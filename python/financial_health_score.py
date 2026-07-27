import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
financial_summary = pd.read_csv(
    r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\feature_engineered_data\financial_summary.csv"
)
financial_summary.replace([np.inf, -np.inf], np.nan, inplace=True)
financial_summary.fillna(0, inplace=True)
def normalize(series):
    if series.max() == series.min():
        return pd.Series([50] * len(series))
    return (
        (series - series.min()) /
        (series.max() - series.min())
    ) * 100
financial_summary["saving_score"] = normalize(
    financial_summary["savings_rate"]
)
financial_summary["investment_score"] = normalize(
    financial_summary["investment_rate"]
)
financial_summary["goal_score"] = normalize(
    financial_summary["goal_completion"]
)
financial_summary["profit_score"] = normalize(
    financial_summary["investment_profit"]
)
financial_summary["budget_score"] = (
    100 -
    normalize(financial_summary["budget_utilization"])
)
financial_summary["financial_health_score"] = (
financial_summary["saving_score"]*0.30 +
financial_summary["investment_score"]*0.20 +
financial_summary["goal_score"]*0.20 +
financial_summary["budget_score"]*0.20 +
financial_summary["profit_score"]*0.10
).round(2)
def health_category(score):
    if score >= 80:
        return "Excellent"
    elif score >= 60:
        return "Good"
    elif score >= 40:
        return "Average"
    else:
        return "Poor"
financial_summary["health_category"] = (
    financial_summary["financial_health_score"]
    .apply(health_category)
)
print(financial_summary.head(10))
print(
financial_summary[
[
"financial_health_score",
"health_category"
]
].head(10)
)
print(
financial_summary["financial_health_score"]
.describe()
)
print(
financial_summary["financial_health_score"]
.mean()
)
top_users = financial_summary.sort_values(
    by="financial_health_score",
    ascending=False
)
print(top_users.head(10))
poor_users = financial_summary.sort_values(
    by="financial_health_score"
)
print(poor_users.head(10))

category = (
financial_summary["health_category"]
.value_counts()
)
plt.figure(figsize=(7,5))
plt.bar(
category.index,
category.values
)
plt.title("Financial Health Categories")
plt.xlabel("Category")
plt.ylabel("Number of Users")
plt.tight_layout()
plt.savefig(
r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\visualizations\financial_health_category.png"
)
plt.show()

plt.figure(figsize=(8,5))
plt.hist(
financial_summary["financial_health_score"],
bins=20
)
plt.title("Financial Health Score Distribution")
plt.xlabel("Score")
plt.ylabel("Users")
plt.tight_layout()
plt.savefig(
r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\visualizations\financial_health_distribution.png"
)
plt.show()

financial_summary.to_csv(
r"C:\Users\nadim\OneDrive\Documents\GitHub\Personal_Finance_Analytics\financial_health\financial_health_score.csv",
index=False
)
print("Financial Health Score generated successfully!")