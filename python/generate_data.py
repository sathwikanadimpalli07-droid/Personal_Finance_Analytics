import pandas as pd
import random
from faker import Faker

fake = Faker('en_IN')

users = []

occupations = [
    'Engineer',
    'Doctor',
    'Teacher',
    'Student',
    'Business Owner',
    'Software Developer',
    'Banker',
    'Lawyer',
    'Manager',
    'Accountant'
]

cities = [
    'Hyderabad',
    'Bangalore',
    'Mumbai',
    'Delhi',
    'Chennai',
    'Pune',
    'Kolkata',
    'Ahmedabad'
]

for i in range(1, 501):

    users.append({
        'user_id': i,
        'name': fake.name(),
        'age': random.randint(22, 60),
        'gender': random.choice(['Male', 'Female']),
        'occupation': random.choice(occupations),
        'city': random.choice(cities),
        'registration_date':
            fake.date_between(
                start_date='-2y',
                end_date='today'
            )
    })

users_df = pd.DataFrame(users)

print(users_df.head())

users_df.to_csv(
    'datasets/users.csv',
    index=False
)
accounts = []
account_id = 1
banks = [
    'SBI',
    'HDFC',
    'ICICI',
    'Axis Bank',
    'Kotak Mahindra',
    'Punjab National Bank',
    'Canara Bank'
]
account_types = [
    'Savings',
    'Current'
]
for user_id in users_df['user_id']:

    num_accounts = random.randint(1, 3)

    for _ in range(num_accounts):

        opening_balance = random.randint(
            5000,
            100000
        )

        current_balance = (
            opening_balance +
            random.randint(-20000, 50000)
        )

        if current_balance < 0:
            current_balance = 0

        accounts.append({
            'account_id': account_id,
            'user_id': user_id,
            'bank_name': random.choice(banks),
            'account_type':
                random.choice(account_types),
            'opening_balance':
                opening_balance,
            'current_balance':
                current_balance
        })

        account_id += 1
accounts_df = pd.DataFrame(accounts)
print(accounts_df.head())
print(len(accounts_df))
accounts_df.to_csv(
    'datasets/accounts.csv',
    index=False
)


expense_categories = [
    'Food',
    'Rent',
    'Shopping',
    'Travel',
    'Healthcare',
    'Education',
    'Entertainment',
    'Utilities',
    'Insurance',
    'EMI'
]
income_categories = [
    'Salary',
    'Freelance',
    'Business',
    'Rental Income',
    'Investment Returns'
]
payment_modes = [
    'UPI',
    'Credit Card',
    'Debit Card',
    'Cash',
    'Net Banking'
]
transactions = []
for i in range(1, 50001):

    account_ids = accounts_df['account_id'].tolist()

    transaction_type = random.choices(
        ['Expense', 'Income'],
        weights=[80, 20]
    )[0]

    if transaction_type == 'Expense':

        category = random.choice(
            expense_categories
        )

        amount = random.randint(
            100,
            25000
        )

    else:

        category = random.choice(
            income_categories
        )

        amount = random.randint(
            5000,
            200000
        )

    transactions.append({
        'transaction_id': i,
        'account_id': account_id,
        'transaction_date':
            fake.date_between(
                start_date='-2y',
                end_date='today'
            ),
        'amount': amount,
        'category': category,
        'type': transaction_type,
        'payment_mode':
            random.choice(payment_modes),
        'description':
            fake.sentence(nb_words=4)
    })
transactions_df = pd.DataFrame(
    transactions
)
print(transactions_df.head())
print(len(transactions_df))
transactions_df.to_csv(
    'datasets/transactions.csv',
    index=False
)


budgets = []
for i in range(1, 2501):

    budgets.append({
        'budget_id': i,
        'user_id': random.randint(1, 500),
        'category': random.choice(
            expense_categories
        ),
        'monthly_limit':
            random.randint(
                5000,
                50000
            )
    })

budget_df = pd.DataFrame(budgets)

print(budget_df.head())
print(len(budget_df))

budget_df.to_csv(
    'datasets/budget.csv',
    index=False
)


investment_types = [
    'Mutual Funds',
    'Stocks',
    'Fixed Deposits',
    'Gold',
    'Cryptocurrency'
]
investments = []
for i in range(1, 2001):

    amount = random.randint(
        10000,
        500000
    )

    investments.append({
        'investment_id': i,
        'user_id': random.randint(
            1,
            500
        ),
        'investment_type':
            random.choice(
                investment_types
            ),
        'amount': amount,
        'purchase_date':
            fake.date_between(
                start_date='-2y',
                end_date='today'
            ),
        'current_value':
            round(
                amount *
                random.uniform(
                    0.8,
                    1.6
                ),
                2
            )
    })

investment_df = pd.DataFrame(
    investments
)

print(investment_df.head())
print(len(investment_df))

investment_df.to_csv(
    'datasets/investment.csv',
    index=False
)


goal_names = [
    'Emergency Fund',
    'Vacation',
    'Car Purchase',
    'House Down Payment'
]

savings_goals = []

for i in range(1, 1501):

    target = random.randint(
        50000,
        1000000
    )

    savings_goals.append({
        'goal_id': i,
        'user_id': random.randint(
            1,
            500
        ),
        'goal_name':
            random.choice(
                goal_names
            ),
        'target_amount':
            target,
        'current_amount':
            random.randint(
                10000,
                target
            ),
        'deadline':
            fake.date_between(
                start_date='today',
                end_date='+3y'
            )
    })

savings_df = pd.DataFrame(
    savings_goals
)

print(savings_df.head())
print(len(savings_df))

savings_df.to_csv(
    'datasets/savings_goals.csv',
    index=False
)