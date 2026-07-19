--Display all users
select * from users;
--Display all accounts
select * from accounts;
--Display all transactions
select * from transactions;
--Display all budget records
select * from budget;
--Display all investment records
select * from investment;
--Display all savings goals
select * from savings_goals;
--Show only expense transactions
select * from transactions where type='expense';
--Show only income transactions
select * from transactions where type='income';
--Show users from Hyderabad
select * from users where city='Hyderabad';
--Show users whose age is greater than 40
select * from users where age>40;
--Show transactions above ₹15,000
select * from transactions where amount>15000;
--Show transactions between December 23rd 2025 and January 3rd 2026
select * from transactions where transaction_date between '2025-12-23' and '2026-01-03';
--Show Food expenses
select * from transactions where category='food';
--Show Salary income transactions
select * from transactions where type='income' and category='salary';
--Show Credit Card transactions
select * from transactions where payment_mode='credit card';
--Display users sorted by age
select * from users order by age;
--Display transactions sorted by amount
select * from transactions order by amount;
--Display latest transactions
select * from transactions order by transaction_date desc;
--Display users sorted by registration date
select * from users order by registration_date;
--Count total users
select count(*) as total_users from users;
--Count total income transactions
select count(*) as income_transactions from transactions where type='income';
--Count total expense transactions
select count(*) as expense_transactions from transactions where type='expense';
--Calculate total income
select sum(amount) as total_income from transactions where type='income';
--Calculate total expenses
select sum(amount) as total_expense from transactions where type='expense';
--Calculate average income amount
select avg(amount) as average_income from transactions where type='income';
--Calculate average expense amount
select avg(amount) as average_expense from transactions where type='expense';
--Find lowest transaction amount
select min(amount) as minimum_transaction from transactions;
--Find highest transaction amount
select max(amount) as maximum_transaction from transactions;
--Calculate total expenses by category
select category,sum(amount) as total_expense from transactions where type='expense' group by category order by total_expense desc;
--Display categories with expenses greater than ₹5,00,00,000
select category,sum(amount) as total_expense from transactions where type='expense' group by category having total_expense>50000000 order by total_expense desc;
--Display distinct categories 
select distinct category from transactions;
--Display top 10 expensive transactions
select * from transactions order by amount desc limit 10;
--Display users whose name starts with S
select * from users where name like 'S%';
--Display users from Hyderabad or Chennai
select * from users where city in('Hyderabad','Chennai');
--Show transactions where description is not null
select * from transactions where description is not null;
--Display all transactions happened after 1st January 2026
select * from transactions where transaction_date>'2026-01-01';