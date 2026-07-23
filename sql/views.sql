--Create a view to display complete user details
create view vw_user as select user_id,name,age,gender,occupation,city,registration_date from users;
--Create a view showing users and their bank accounts
create view vw_user_account as select u.user_id,u.name,u.age,u.city,a.account_id,a.bank_name,a.account_type,a.current_balance from users u join accounts a on u.user_id=a.user_id;
--Create a view showing every transaction along with user details
create view vw_user_transaction as select u.user_id,u.name,a.account_id,a.bank_name,t.transaction_id,t.transaction_date,t.amount,t.category,t.type,t.payment_mode from users u join accounts a on u.user_id=a.user_id join transactions t on a.account_id=t.account_id;
--Create a view showing the total income for each user
create or replace view vw_total_income as select u.user_id,u.name,sum(t.amount) as total_income from users u join accounts a on u.user_id=a.user_id join transactions t on a.account_id=t.account_id where type='income' group by u.user_id,u.name;
--Create a view showing the total expenses for each user
create view vw_total_expense as select u.user_id,u.name,sum(t.amount) as total_expense from users u join accounts a on u.user_id=a.user_id join transactions t on a.account_id=t.account_id where type='expense' group by u.user_id,u.name;
--Create a view showing Budget Utilization for every user
create view vw_budget_utilization as select u.user_id,u.name,b.category,b.monthly_limit,ifnull(sum(t.amount),0) as total_expense,b.monthly_limit-ifnull(sum(t.amount),0) as remaining_budget from users u join budget b left join accounts a on u.user_id=a.user_id left join transactions t on a.account_id=t.account_id where t.type='expense' and t.category=b.category group by u.user_id,u.name,b.category,b.monthly_limit;
--Create a view showing Investment Summary
create view vw_investment_summary as select u.user_id,u.name,sum(i.amount) as invested_amount,sum(current_value) as current_value,sum(i.current_value)-sum(i.amount) as profit from users u join investment i on u.user_id=i.user_id group by u.user_id=u.name;
--Create a Monthly Financial Summary View
create or replace view vw_monthly_summary as select year(transaction_date) as year,month(transaction_date) as month,monthname(transaction_date) as month_name,sum(case when type='income' then amount else 0 end) as total_income,sum(case when type='expense' then amount else 0 end) as total_expense from transactions group by year,month,month_name order by year,month;
--Create a Financial Dashboard View
create view vw_financial_dashboard as select u.user_id,u.name,count(distinct a.account_id) as total_accounts,sum(case when t.type='income' then t.amount else 0 end) as total_income,sum(case when t.type='expense' then t.amount else 0 end) as total_expense,ifnull(sum(distinct i.amount),0) as total_investment,ifnull(sum(distinct s.current_amount),0) as savings_goals from users u left join accounts a on u.user_id=a.user_id left join transactions t on a.account_id=t.account_id left join investment i on u.user_id=i.user_id left join savings_goals s on u.user_id=s.user_id group by u.user_id,u.name;
--List All Views in the Current Database
show full tables where table_type='VIEW';
--View the Data
select * from vw_user;