CREATE DATABASE personal_finance_analytics;
USE personal_finance_analytics;

CREATE TABLE users(
user_id INT auto_increment PRIMARY KEY,
name VARCHAR(50) NOT NULL,
age INT,
gender varchar(15),
occupation varchar(25),
city varchar(50),
registration_date date
);

CREATE table accounts(
account_id int auto_increment primary key,
user_id int not null,
bank_name varchar(50),
account_type varchar(50),
opening_balance decimal(12,2),
current_balance decimal(12,2),
FOREIGN KEY(user_id) REFERENCES users(user_id)
);
CREATE TABLE transactions(
transaction_id int auto_increment primary key,
account_id int not null,
transaction_date date,
amount decimal(12,2),
category varchar(100),
type ENUM('Income','Expense'),
payment_mode Enum('UPI','Credit card','Debit card','Cash','Net Banking'),
description varchar(255),
FOREIGN KEY(account_id) REFERENCES accounts(account_id)
);

create table budget(
budget_id int auto_increment primary key,
user_id int not null,
category varchar(100),
monthly_limit decimal(12,2),
foreign key(user_id) references users(user_id)
);

create table investment(
investment_id int auto_increment primary key,
user_id int not null,
investment_type ENUM('Mutual Funds','Stocks','Fixed Deposits','Gold','Cryptocurrency'),
amount decimal(12,2),
purchase_date date,
current_value decimal(12,2),
foreign key(user_id) references users(user_id)
);

create table savings_goals(
goal_id int auto_increment primary key,
user_id int not null,
goal_name varchar(50),
target_amount decimal(12,2),
current_amount decimal(12,2),
deadline date,
foreign key(user_id) references users(user_id)
);

create table finance_health(
score_id int auto_increment primary key,
user_id int not null,
savings_score decimal(12,2),
investment_score decimal(12,2),
budget_score decimal(12,2),
emergency_score decimal(12,2),
total_score decimal(12,2),
score_category varchar(20),
calculated_date date,
foreign key(user_id) references users(user_id)
);

create table expense_predictions(
prediction_id int auto_increment primary key,
user_id int not null,
prediction_month date,
predicted_expense decimal(12,2),
actual_expense decimal(12,2),
model_name varchar(50),
created_at timestamp default current_timestamp,
foreign key(user_id) references users(user_id)
);