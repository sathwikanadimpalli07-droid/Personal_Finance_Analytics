import pandas as pd
from sqlalchemy import create_engine
engine = create_engine(
    "mysql+mysqlconnector://root:12345@localhost/personal_finance_analytics"
)

users = pd.read_sql("SELECT * FROM users",engine)

print("="*80)
print("USERS TABLE EDA")
print("="*80)

print(users.head())
print(users.tail())
print("\nShape:")
print(users.shape)
print("\nColumns:")
print(users.columns)
print("\nData Types:")
print(users.dtypes)
print("\nInfo:")
users.info()
print("\nStatistical Summary:")
print(users.describe())
print("\nMissing Values:")
print(users.isnull().sum())
print("\nDuplicate Rows:")
print(users.duplicated().sum())
print("\nUnique Cities:")
print(users["city"].unique())
print("\nNumber of Cities:")
print(users["city"].nunique())
print("\nUsers by City:")
print(users["city"].value_counts())
print("\nUsers by Occupation:")
print(users["occupation"].value_counts())
print("\nMinimum Age:", users["age"].min())
print("Maximum Age:", users["age"].max())
print("Average Age:", users["age"].mean())
print("Median Age:", users["age"].median())
print("Age Standard Deviation:", users["age"].std())
print("\nUsers with Age < 18")
print(users[users["age"] < 18])


accounts = pd.read_sql("SELECT * FROM accounts",engine)

print("="*80)
print("ACCOUNTS TABLE EDA")
print("="*80)

print(accounts.head())
print(accounts.tail())
print(accounts.shape)
print(accounts.columns)
print(accounts.dtypes)
accounts.info()
print(accounts.describe())
print(accounts.isnull().sum())
print(accounts.duplicated().sum())
print(accounts["bank_name"].value_counts())
print(accounts["account_type"].value_counts())
print("Minimum Balance:", accounts["current_balance"].min())
print("Maximum Balance:", accounts["current_balance"].max())
print("Average Balance:", accounts["current_balance"].mean())
print("Median Balance:", accounts["current_balance"].median())
print("Balance Std:", accounts["current_balance"].std())
print(accounts[accounts["current_balance"] < 0])


transactions = pd.read_sql("SELECT * FROM transactions",engine)

print("="*80)
print("TRANSACTIONS TABLE EDA")
print("="*80)

print(transactions.head())
print(transactions.tail())
print(transactions.shape)
print(transactions.columns)
print(transactions.dtypes)
transactions.info()
print(transactions.describe())
print(transactions.isnull().sum())
print(transactions.duplicated().sum())
print("\nTransaction Type:")
print(transactions["type"].value_counts())
print("\nTransaction Category:")
print(transactions["category"].value_counts())
print("\nPayment Mode:")
print(transactions["payment_mode"].value_counts())
print("Minimum Amount:", transactions["amount"].min())
print("Maximum Amount:", transactions["amount"].max())
print("Average Amount:", transactions["amount"].mean())
print("Median Amount:", transactions["amount"].median())
print("Std Amount:", transactions["amount"].std())
print(transactions[transactions["amount"] < 0])
print("\nUnique Categories")
print(transactions["category"].unique())
print("\nNumber of Categories")
print(transactions["category"].nunique())
print("\nUnique Payment Modes")
print(transactions["payment_mode"].unique())


budget = pd.read_sql("SELECT * FROM budget",engine)

print("="*80)
print("BUDGET TABLE EDA")
print("="*80)

print(budget.head())
print(budget.tail())
print(budget.shape)
print(budget.columns)
print(budget.dtypes)
budget.info()
print(budget.describe())
print(budget.isnull().sum())
print(budget.duplicated().sum())
print(budget["category"].value_counts())
print("Minimum Budget:", budget["monthly_limit"].min())
print("Maximum Budget:", budget["monthly_limit"].max())
print("Average Budget:", budget["monthly_limit"].mean())
print("Median Budget:", budget["monthly_limit"].median())
print("Budget Std:", budget["monthly_limit"].std())
print(budget[budget["monthly_limit"] < 0])


investment = pd.read_sql("SELECT * FROM investment",engine)

print("="*80)
print("INVESTMENT TABLE EDA")
print("="*80)

print(investment.head())
print(investment.tail())
print(investment.shape)
print(investment.columns)
print(investment.dtypes)
investment.info()
print(investment.describe())
print(investment.isnull().sum())
print(investment.duplicated().sum())
print(investment["investment_type"].value_counts())
print("Minimum Investment:", investment["amount"].min())
print("Maximum Investment:", investment["amount"].max())
print("Average Investment:", investment["amount"].mean())
print("Median Investment:", investment["amount"].median())
print("Minimum Current Value:", investment["current_value"].min())
print("Maximum Current Value:", investment["current_value"].max())
print(investment[investment["amount"] < 0])
print(investment[investment["current_value"] < 0])


savings_goals = pd.read_sql("SELECT * FROM savings_goals",engine)

print("="*80)
print("SAVINGS GOALS TABLE EDA")
print("="*80)

print(savings_goals.head())
print(savings_goals.tail())
print(savings_goals.shape)
print(savings_goals.columns)
print(savings_goals.dtypes)
savings_goals.info()
print(savings_goals.describe())
print(savings_goals.isnull().sum())
print(savings_goals.duplicated().sum())
print(savings_goals["goal_name"].value_counts())
print("Minimum Target Amount:", savings_goals["target_amount"].min())
print("Maximum Target Amount:", savings_goals["target_amount"].max())
print("Average Target Amount:", savings_goals["target_amount"].mean())
print("Minimum Current Amount:", savings_goals["current_amount"].min())
print("Maximum Current Amount:", savings_goals["current_amount"].max())
print("Average Current Amount:", savings_goals["current_amount"].mean())
print(savings_goals[savings_goals["target_amount"] < 0])
print(savings_goals[savings_goals["current_amount"] < 0])


print("="*80)
print("CROSS TABLE EDA")
print("="*80)

print("Users:", len(users))
print("Accounts:", len(accounts))
print("Transactions:", len(transactions))
print("Budget:", len(budget))
print("Investment:", len(investment))
print("Savings Goals:", len(savings_goals))
print(transactions[transactions["type"]=="Income"]["amount"].sum())
print(transactions[transactions["type"]=="Expense"]["amount"].sum())
print(transactions.nlargest(10, "amount"))
print(transactions.nsmallest(10, "amount"))
transaction_count = transactions.groupby("account_id").size()
print(transaction_count.sort_values(ascending=False).head(10))


# ================================================================================
# USERS TABLE EDA
# ================================================================================
#    user_id             name  age  gender      occupation       city registration_date
# 0        1      Kala Parmer   40    Male         Teacher  Bangalore        2025-02-21
# 1        2    Daksha Sharma   36  Female          Doctor    Chennai        2025-11-26
# 2        3   Hemang Trivedi   41  Female          Banker  Hyderabad        2026-01-29
# 3        4  Benjamin Sehgal   54  Female  Business Owner    Kolkata        2024-08-20
# 4        5         Riya Rai   44  Female          Doctor    Chennai        2024-07-24
#      user_id               name  age  gender      occupation       city registration_date
# 495      496          Sara Iyer   54    Male          Lawyer  Ahmedabad        2025-05-10
# 496      497  Siddharth Trivedi   39  Female         Teacher    Kolkata        2026-03-29
# 497      498       Shivani Kari   51    Male  Business Owner    Chennai        2026-04-24
# 498      499       Barkha Saraf   59  Female         Student  Ahmedabad        2025-05-08
# 499      500       Anjali Salvi   31  Female          Lawyer  Ahmedabad        2026-05-13

# Shape:
# (500, 7)

# Columns:
# Index(['user_id', 'name', 'age', 'gender', 'occupation', 'city',
#        'registration_date'],
#       dtype='str')

# Data Types:
# user_id               int64
# name                    str
# age                   int64
# gender                  str
# occupation              str
# city                    str
# registration_date    object
# dtype: object

# Info:
# <class 'pandas.DataFrame'>
# RangeIndex: 500 entries, 0 to 499
# Data columns (total 7 columns):
#  #   Column             Non-Null Count  Dtype 
# ---  ------             --------------  ----- 
#  0   user_id            500 non-null    int64 
#  1   name               500 non-null    str   
#  2   age                500 non-null    int64 
#  3   gender             500 non-null    str   
#  4   occupation         500 non-null    str   
#  5   city               500 non-null    str   
#  6   registration_date  500 non-null    object
# dtypes: int64(2), object(1), str(4)
# memory usage: 27.5+ KB

# Statistical Summary:
#           user_id         age
# count  500.000000  500.000000
# mean   250.500000   40.592000
# std    144.481833   11.152861
# min      1.000000   22.000000
# 25%    125.750000   31.000000
# 50%    250.500000   39.000000
# 75%    375.250000   51.000000
# max    500.000000   60.000000

# Missing Values:
# user_id              0
# name                 0
# age                  0
# gender               0
# occupation           0
# city                 0
# registration_date    0
# dtype: int64

# Duplicate Rows:
# 0

# Unique Cities:
# <StringArray>
# ['Bangalore',   'Chennai', 'Hyderabad',   'Kolkata',      'Pune', 'Ahmedabad',
#     'Mumbai',     'Delhi']
# Length: 8, dtype: str

# Number of Cities:
# 8

# Users by City:
# city
# Ahmedabad    75
# Bangalore    72
# Kolkata      68
# Hyderabad    65
# Delhi        62
# Chennai      61
# Pune         49
# Mumbai       48
# Name: count, dtype: int64

# Users by Occupation:
# occupation
# Banker                63
# Engineer              62
# Business Owner        53
# Student               50
# Manager               49
# Doctor                48
# Accountant            46
# Teacher               44
# Lawyer                44
# Software Developer    41
# Name: count, dtype: int64

# Minimum Age: 22
# Maximum Age: 60
# Average Age: 40.592
# Median Age: 39.0
# Age Standard Deviation: 11.152861005913884

# Users with Age < 18
# Empty DataFrame
# Columns: [user_id, name, age, gender, occupation, city, registration_date]
# Index: []
# ================================================================================
# ACCOUNTS TABLE EDA
# ================================================================================
#    account_id  user_id       bank_name account_type  opening_balance  current_balance
# 0           1        1     Canara Bank      Savings           5640.0              0.0
# 1           2        2             SBI      Savings          14703.0          21460.0
# 2           3        2  Kotak Mahindra      Current           7930.0          49972.0
# 3           4        2       Axis Bank      Current          35768.0          67562.0
# 4           5        3            HDFC      Current          58671.0          95503.0
#       account_id  user_id    bank_name account_type  opening_balance  current_balance
# 1006        1007      497         HDFC      Current          46417.0          47281.0
# 1007        1008      497  Canara Bank      Current          93310.0         134188.0
# 1008        1009      498    Axis Bank      Current          78161.0          97007.0
# 1009        1010      499        ICICI      Current          22961.0          21054.0
# 1010        1011      500         HDFC      Current          76719.0          74037.0
# (1011, 6)
# Index(['account_id', 'user_id', 'bank_name', 'account_type', 'opening_balance',
#        'current_balance'],
#       dtype='str')
# account_id           int64
# user_id              int64
# bank_name              str
# account_type           str
# opening_balance    float64
# current_balance    float64
# dtype: object
# <class 'pandas.DataFrame'>
# RangeIndex: 1011 entries, 0 to 1010
# Data columns (total 6 columns):
#  #   Column           Non-Null Count  Dtype  
# ---  ------           --------------  -----  
#  0   account_id       1011 non-null   int64  
#  1   user_id          1011 non-null   int64  
#  2   bank_name        1011 non-null   str    
#  3   account_type     1011 non-null   str    
#  4   opening_balance  1011 non-null   float64
#  5   current_balance  1011 non-null   float64
# dtypes: float64(2), int64(2), str(2)
# memory usage: 47.5 KB
#         account_id      user_id  opening_balance  current_balance
# count  1011.000000  1011.000000      1011.000000      1011.000000
# mean    506.000000   247.101879     52871.156281     67175.784372
# std     291.994863   143.311696     26712.611670     33702.686915
# min       1.000000     1.000000      5090.000000         0.000000
# 25%     253.500000   121.500000     30547.000000     42284.500000
# 50%     506.000000   245.000000     53364.000000     67345.000000
# 75%     758.500000   371.000000     75924.000000     93185.500000
# max    1011.000000   500.000000     99980.000000    147403.000000
# account_id         0
# user_id            0
# bank_name          0
# account_type       0
# opening_balance    0
# current_balance    0
# dtype: int64
# 0
# bank_name
# Kotak Mahindra          159
# Punjab National Bank    158
# ICICI                   155
# Axis Bank               153
# Canara Bank             130
# HDFC                    129
# SBI                     127
# Name: count, dtype: int64
# account_type
# Current    532
# Savings    479
# Name: count, dtype: int64
# Minimum Balance: 0.0
# Maximum Balance: 147403.0
# Average Balance: 67175.784371909
# Median Balance: 67345.0
# Balance Std: 33702.68691522878
# Empty DataFrame
# Columns: [account_id, user_id, bank_name, account_type, opening_balance, current_balance]
# Index: []
# ================================================================================
# TRANSACTIONS TABLE EDA
# ================================================================================
#    transaction_id  account_id transaction_date  ...     type payment_mode                       description
# 0               1         741       2025-12-01  ...  Expense         Cash       Corporis error ipsa fuga.\r
# 1               2         407       2024-10-27  ...  Expense   Debit card    Ratione officiis neque amet.\r
# 2               3         702       2024-12-09  ...  Expense          UPI             Nostrum veniam eum.\r
# 3               4          36       2025-07-15  ...   Income   Debit card           Consequatur adipisci.\r
# 4               5         349       2026-06-05  ...  Expense   Debit card  Nesciunt tenetur perspiciatis.\r

# [5 rows x 8 columns]
#        transaction_id  account_id transaction_date  ...     type payment_mode                  description
# 49995           49996         699       2024-11-04  ...  Expense  Credit card           Laboriosam modi.\r
# 49996           49997         692       2024-07-17  ...  Expense         Cash           Occaecati culpa.\r
# 49997           49998         645       2026-04-06  ...  Expense   Debit card      Cum ipsum temporibus.\r
# 49998           49999         450       2026-04-10  ...  Expense         Cash  Consequatur totam beatae.\r
# 49999           50000         705       2024-10-14  ...  Expense         Cash           Inventore saepe.\r

# [5 rows x 8 columns]
# (50000, 8)
# Index(['transaction_id', 'account_id', 'transaction_date', 'amount',
#        'category', 'type', 'payment_mode', 'description'],
#       dtype='str')
# transaction_id        int64
# account_id            int64
# transaction_date     object
# amount              float64
# category                str
# type                    str
# payment_mode            str
# description             str
# dtype: object
# <class 'pandas.DataFrame'>
# RangeIndex: 50000 entries, 0 to 49999
# Data columns (total 8 columns):
#  #   Column            Non-Null Count  Dtype  
# ---  ------            --------------  -----  
#  0   transaction_id    50000 non-null  int64  
#  1   account_id        50000 non-null  int64  
#  2   transaction_date  50000 non-null  object 
#  3   amount            50000 non-null  float64
#  4   category          50000 non-null  str    
#  5   type              50000 non-null  str    
#  6   payment_mode      50000 non-null  str    
#  7   description       50000 non-null  str    
# dtypes: float64(1), int64(2), object(1), str(4)
# memory usage: 3.1+ MB
#        transaction_id    account_id         amount
# count    50000.000000  50000.000000   50000.000000
# mean     25000.500000    507.608180   30355.691280
# std      14433.901067    291.580744   44025.684401
# min          1.000000      1.000000     100.000000
# 25%      12500.750000    254.000000    7845.000000
# 50%      25000.500000    508.000000   15349.500000
# 75%      37500.250000    759.000000   22819.250000
# max      50000.000000   1011.000000  199985.000000
# transaction_id      0
# account_id          0
# transaction_date    0
# amount              0
# category            0
# type                0
# payment_mode        0
# description         0
# dtype: int64
# 0

# Transaction Type:
# type
# Expense    40069
# Income      9931
# Name: count, dtype: int64

# Transaction Category:
# category
# Travel                4172
# EMI                   4073
# Rent                  4063
# Entertainment         4035
# Food                  4015
# Education             4013
# Healthcare            3969
# Shopping              3957
# Utilities             3906
# Insurance             3866
# Salary                2033
# Rental Income         1998
# Investment Returns    1996
# Business              1979
# Freelance             1925
# Name: count, dtype: int64

# Payment Mode:
# payment_mode
# Credit card    10156
# Debit card     10071
# UPI             9992
# Net Banking     9933
# Cash            9848
# Name: count, dtype: int64
# Minimum Amount: 100.0
# Maximum Amount: 199985.0
# Average Amount: 30355.69128
# Median Amount: 15349.5
# Std Amount: 44025.68440099247
# Empty DataFrame
# Columns: [transaction_id, account_id, transaction_date, amount, category, type, payment_mode, description]
# Index: []

# Unique Categories
# <StringArray>
# [         'Insurance',             'Travel',                'EMI',
#            'Business',           'Shopping', 'Investment Returns',
#       'Entertainment',          'Freelance',          'Utilities',
#              'Salary',               'Rent',         'Healthcare',
#           'Education',               'Food',      'Rental Income']
# Length: 15, dtype: str

# Number of Categories
# 15

# Unique Payment Modes
# <StringArray>
# ['Cash', 'Debit card', 'UPI', 'Net Banking', 'Credit card']
# Length: 5, dtype: str
# ================================================================================
# BUDGET TABLE EDA
# ================================================================================
#    budget_id  user_id   category  monthly_limit
# 0          1      152       Rent        38423.0
# 1          2      366       Rent        46724.0
# 2          3      367  Insurance        23382.0
# 3          4      448        EMI        22892.0
# 4          5      110  Utilities        27165.0
#       budget_id  user_id       category  monthly_limit
# 2495       2496      366  Entertainment        32958.0
# 2496       2497      311           Food        19426.0
# 2497       2498      293            EMI        20854.0
# 2498       2499       34     Healthcare        31090.0
# 2499       2500      240           Food        19154.0
# (2500, 4)
# Index(['budget_id', 'user_id', 'category', 'monthly_limit'], dtype='str')
# budget_id          int64
# user_id            int64
# category             str
# monthly_limit    float64
# dtype: object
# <class 'pandas.DataFrame'>
# RangeIndex: 2500 entries, 0 to 2499
# Data columns (total 4 columns):
#  #   Column         Non-Null Count  Dtype  
# ---  ------         --------------  -----  
#  0   budget_id      2500 non-null   int64  
#  1   user_id        2500 non-null   int64  
#  2   category       2500 non-null   str    
#  3   monthly_limit  2500 non-null   float64
# dtypes: float64(1), int64(2), str(1)
# memory usage: 78.3 KB
#         budget_id      user_id  monthly_limit
# count  2500.00000  2500.000000    2500.000000
# mean   1250.50000   251.880800   27676.659200
# std     721.83216   143.906736   12954.765107
# min       1.00000     1.000000    5032.000000
# 25%     625.75000   127.750000   16781.500000
# 50%    1250.50000   253.500000   27992.500000
# 75%    1875.25000   373.250000   38845.250000
# max    2500.00000   500.000000   49985.000000
# budget_id        0
# user_id          0
# category         0
# monthly_limit    0
# dtype: int64
# 0
# category
# Utilities        270
# Food             269
# EMI              268
# Entertainment    267
# Education        252
# Rent             243
# Healthcare       240
# Travel           240
# Insurance        227
# Shopping         224
# Name: count, dtype: int64
# Minimum Budget: 5032.0
# Maximum Budget: 49985.0
# Average Budget: 27676.6592
# Median Budget: 27992.5
# Budget Std: 12954.765107320538
# Empty DataFrame
# Columns: [budget_id, user_id, category, monthly_limit]
# Index: []
# ================================================================================
# INVESTMENT TABLE EDA
# ================================================================================
#    investment_id  user_id investment_type    amount purchase_date  current_value
# 0              1      452            Gold  319592.0    2026-05-03      410940.69
# 1              2      324          Stocks   83808.0    2026-03-31       98722.18
# 2              3        3            Gold  337841.0    2025-08-21      281895.70
# 3              4      208  Fixed Deposits  188681.0    2025-02-12      228514.33
# 4              5      452  Cryptocurrency  259243.0    2026-05-11      386169.22
#       investment_id  user_id investment_type    amount purchase_date  current_value
# 1995           1996      102  Cryptocurrency   34675.0    2025-01-25       47091.00
# 1996           1997      351  Fixed Deposits  195526.0    2026-06-25      161126.21
# 1997           1998      213          Stocks  235557.0    2025-10-22      312222.22
# 1998           1999      439          Stocks  447365.0    2025-12-08      544929.86
# 1999           2000      420          Stocks  465578.0    2024-12-23      492090.51
# (2000, 6)
# Index(['investment_id', 'user_id', 'investment_type', 'amount',
#        'purchase_date', 'current_value'],
#       dtype='str')
# investment_id        int64
# user_id              int64
# investment_type        str
# amount             float64
# purchase_date       object
# current_value      float64
# dtype: object
# <class 'pandas.DataFrame'>
# RangeIndex: 2000 entries, 0 to 1999
# Data columns (total 6 columns):
#  #   Column           Non-Null Count  Dtype  
# ---  ------           --------------  -----  
#  0   investment_id    2000 non-null   int64  
#  1   user_id          2000 non-null   int64  
#  2   investment_type  2000 non-null   str    
#  3   amount           2000 non-null   float64
#  4   purchase_date    2000 non-null   object 
#  5   current_value    2000 non-null   float64
# dtypes: float64(2), int64(2), object(1), str(1)
# memory usage: 93.9+ KB
#        investment_id      user_id         amount  current_value
# count    2000.000000  2000.000000    2000.000000    2000.000000
# mean     1000.500000   250.896500  254905.336500  304866.648560
# std       577.494589   143.633259  141031.392622  181583.138685
# min         1.000000     1.000000   10027.000000   10051.960000
# 25%       500.750000   128.000000  134787.500000  155300.875000
# 50%      1000.500000   251.000000  253465.000000  291207.820000
# 75%      1500.250000   375.000000  378262.500000  432071.242500
# max      2000.000000   500.000000  499900.000000  769312.660000
# investment_id      0
# user_id            0
# investment_type    0
# amount             0
# purchase_date      0
# current_value      0
# dtype: int64
# 0
# investment_type
# Stocks            421
# Cryptocurrency    399
# Mutual Funds      398
# Fixed Deposits    393
# Gold              389
# Name: count, dtype: int64
# Minimum Investment: 10027.0
# Maximum Investment: 499900.0
# Average Investment: 254905.3365
# Median Investment: 253465.0
# Minimum Current Value: 10051.96
# Maximum Current Value: 769312.66
# Empty DataFrame
# Columns: [investment_id, user_id, investment_type, amount, purchase_date, current_value]
# Index: []
# Empty DataFrame
# Columns: [investment_id, user_id, investment_type, amount, purchase_date, current_value]
# Index: []
# ================================================================================
# SAVINGS GOALS TABLE EDA
# ================================================================================
#    goal_id  user_id       goal_name  target_amount  current_amount    deadline
# 0        1      240        Vacation       813314.0        270251.0  2028-11-15
# 1        2      373    Car Purchase        71896.0         52134.0  2027-03-11
# 2        3      406  Emergency Fund       993359.0        323850.0  2028-07-03
# 3        4      422    Car Purchase       920308.0        134584.0  2026-11-24
# 4        5      241  Emergency Fund       259270.0         72840.0  2028-01-31
#       goal_id  user_id       goal_name  target_amount  current_amount    deadline
# 1495     1496       85    Car Purchase       382951.0         40414.0  2026-07-19
# 1496     1497      357        Vacation       202423.0        158480.0  2027-11-12
# 1497     1498      482  Emergency Fund       873559.0        198370.0  2028-12-22
# 1498     1499        3    Car Purchase       112625.0        106365.0  2029-06-06
# 1499     1500      294  Emergency Fund       385049.0        374686.0  2029-05-28
# (1500, 6)
# Index(['goal_id', 'user_id', 'goal_name', 'target_amount', 'current_amount',
#        'deadline'],
#       dtype='str')
# goal_id             int64
# user_id             int64
# goal_name             str
# target_amount     float64
# current_amount    float64
# deadline           object
# dtype: object
# <class 'pandas.DataFrame'>
# RangeIndex: 1500 entries, 0 to 1499
# Data columns (total 6 columns):
#  #   Column          Non-Null Count  Dtype  
# ---  ------          --------------  -----  
#  0   goal_id         1500 non-null   int64  
#  1   user_id         1500 non-null   int64  
#  2   goal_name       1500 non-null   str    
#  3   target_amount   1500 non-null   float64
#  4   current_amount  1500 non-null   float64
#  5   deadline        1500 non-null   object 
# dtypes: float64(2), int64(2), object(1), str(1)
# memory usage: 70.4+ KB
#            goal_id      user_id  target_amount  current_amount
# count  1500.000000  1500.000000    1500.000000     1500.000000
# mean    750.500000   247.322667  523709.644667   272471.514000
# std     433.157015   142.390990  278511.014599   222244.665824
# min       1.000000     1.000000   50082.000000    10014.000000
# 25%     375.750000   127.000000  270441.000000    86743.000000
# 50%     750.500000   247.000000  532474.000000   214170.500000
# 75%    1125.250000   365.250000  771553.250000   409635.500000
# max    1500.000000   500.000000  999643.000000   995308.000000
# goal_id           0
# user_id           0
# goal_name         0
# target_amount     0
# current_amount    0
# deadline          0
# dtype: int64
# 0
# goal_name
# Vacation              396
# Car Purchase          372
# Emergency Fund        371
# House Down Payment    361
# Name: count, dtype: int64
# Minimum Target Amount: 50082.0
# Maximum Target Amount: 999643.0
# Average Target Amount: 523709.6446666667
# Minimum Current Amount: 10014.0
# Maximum Current Amount: 995308.0
# Average Current Amount: 272471.514
# Empty DataFrame
# Columns: [goal_id, user_id, goal_name, target_amount, current_amount, deadline]
# Index: []
# Empty DataFrame
# Columns: [goal_id, user_id, goal_name, target_amount, current_amount, deadline]
# Index: []
# ================================================================================
# CROSS TABLE EDA
# ================================================================================
# Users: 500
# Accounts: 1011
# Transactions: 50000
# Budget: 2500
# Investment: 2000
# Savings Goals: 1500
# 1013301654.0
# 504482910.0
#        transaction_id  account_id transaction_date  ...    type payment_mode                             description
# 13153           13154          29       2025-05-03  ...  Income          UPI                            Quas nemo.\r
# 46713           46714         751       2025-07-19  ...  Income  Credit card    Vel ratione nihil soluta suscipit.\r
# 38453           38454         666       2025-01-03  ...  Income  Net Banking         Optio excepturi eos possimus.\r
# 47345           47346         392       2024-10-26  ...  Income         Cash                   Tenetur blanditiis.\r
# 20581           20582         400       2025-09-29  ...  Income  Net Banking                           Eius culpa.\r
# 26272           26273         909       2025-07-09  ...  Income         Cash                    Velit consectetur.\r
# 24954           24955          99       2026-03-15  ...  Income          UPI              Et neque inventore nisi.\r
# 49175           49176         204       2025-02-16  ...  Income  Credit card          Et quia quia incidunt velit.\r
# 20417           20418         201       2024-08-16  ...  Income         Cash  Dignissimos totam eos beatae labore.\r
# 43210           43211         430       2025-06-12  ...  Income  Credit card      Natus nesciunt natus doloremque.\r

# [10 rows x 8 columns]
#        transaction_id  account_id  ... payment_mode                                        description
# 34569           34570          29  ...   Debit card               Maxime ipsum maxime sapiente quae.\r
# 40193           40194         111  ...          UPI                                      Ipsam odit.\r
# 41875           41876         328  ...          UPI  Dolores sit voluptatum consequuntur reprehende...
# 11486           11487         944  ...   Debit card                               Fugiat quos quasi.\r
# 21587           21588         597  ...  Credit card        Provident maxime maxime recusandae dolor.\r
# 36825           36826         525  ...  Credit card                               Magnam temporibus.\r
# 2562             2563         223  ...  Credit card                              Nihil aliquid modi.\r
# 15961           15962         498  ...          UPI                          Blanditiis a sit optio.\r
# 20148           20149         595  ...   Debit card                                    In voluptate.\r
# 41127           41128         911  ...         Cash                         Eaque quibusdam sunt ex.\r

# [10 rows x 8 columns]
# account_id
# 791    79
# 178    70
# 774    69
# 798    68
# 882    67
# 733    67
# 991    66
# 617    66
# 342    65
# 657    65
# dtype: int64