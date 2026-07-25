--Compare Budget vs Actual Expenses
select u.user_id,u.name,b.category,b.monthly_limit as budget_amount,ifnull(sum(t.amount),0) as actual_expense,b.monthly_limit-ifnull(sum(t.amount),0) as remaining_budget,case when b.monthly_limit>ifnull(sum(t.amount),0) then 'Within Budget' else 'Budget Exceeded' end as budget_status from users u join budget b on u.user_id=b.user_id left join accounts a on u.user_id=a.user_id left join transactions t on a.account_id=t.account_id where b.category=t.category and t.type='Expense' group by u.user_id,u.name,b.category,b.monthly_limit order by u.user_id,u.name;
--Compare Total Income vs Total Investment
select u.user_id,u.name,ifnull(i.total_income,0) as total_income,ifnull(inv.total_investment,0) as total_investment,round((ifnull(inv.total_investment,0)/nullif(i.total_income,0))*100,2) as investment_percentage from users u left join(select a.user_id,sum(t.amount) as total_income from accounts a join transactions t on a.account_id=t.account_id where t.type='income' group by a.user_id)i on u.user_id=i.user_id left join(select user_id,sum(amount) as total_investment from investment group by user_id)inv on u.user_id=inv.user_id order by u.user_id;
--Generate Complete Financial Summary for Each User
select u.user_id,u.name,ifnull(i.total_income,0) as total_income,ifnull(e.total_expense,0) as total_expense,ifnull(inv.total_investment,0) as total_investment,ifnull(s.total_savings,0) as savings_goals,ifnull(i.total_income,0)-ifnull(e.total_expense,0) as net_savings from users u left join (select a.user_id,sum(t.amount) as total_income from accounts a join transactions t on a.account_id=t.account_id where t.type='income' group by a.user_id)i on u.user_id=i.user_id left join(select a.user_id,sum(t.amount) as total_expense from accounts a join transactions t on a.account_id=t.account_id where t.type='expense' group by a.user_id)e on u.user_id=e.user_id left join(select user_id,sum(amount) as total_investment from investment group by user_id)inv on u.user_id=inv.user_id left join(select user_id,sum(target_amount) as total_savings from savings_goals group by user_id)s on u.user_id=s.user_id order by u.user_id;
--Calculate Net Savings for Every User
select u.user_id,u.name,sum(case when t.type='income' then t.amount else -t.amount end)as net_savings from users u join accounts a on u.user_id=a.user_id join transactions t on a.account_id=t.account_id group by u.user_id,u.name order by u.user_id;
--Calculate Savings Rate (%) for Every User
select u.user_id,u.name,sum(case when t.type='income' then t.amount else 0 end) as total_income,sum(case when t.type='expense' then t.amount else 0 end) as total_expense,sum(case when t.type='income' then t.amount else -t.amount end)as net_savings,round(sum(case when t.type='income' then t.amount else -t.amount end)/nullif(sum(case when t.type='income' then t.amount else 0 end),0)*100,2)as savings_rate from users u join accounts a on u.user_id=a.user_id join transactions t on a.account_id=t.account_id group by u.user_id,u.name order by u.user_id;
--Top 10 Highest Spending Users
select u.user_id,u.name,sum(t.amount) as total_expense from users u join accounts a on u.user_id=a.user_id join transactions t on a.account_id=t.account_id where t.type='expense' group by u.user_id,u.name order by total_expense desc limit 10;
--Top 10 Highest Spending Categories
select category,sum(amount) as total_expense from transactions where type='expense' group by category order by total_expense desc limit 10;
--Category wise Expense Distribution
select category,sum(amount) as total_expense,round(sum(amount)*100/(select sum(amount) from transactions where type='expense'),2)as expense_percent from transactions where type='expense' group by category order by total_expense desc;
--Monthly Expense Trend
select date_format(transaction_date,'%m-%y') as month,sum(amount) as total_expense from transactions where type='expense' group by date_format(transaction_date,'%m-%y') order by month;
--Average Transaction Amount by Category
select category,count(*) as total_transactions,avg(amount) as average_amount,min(amount) as minimum_amount,max(amount) as maximum_amount from transactions where type='expense' group by category order by average_amount desc;
--Monthly Income Trend
select date_format(transaction_date,'%m-%y') as month,sum(amount) as total_income from transactions where type='income' group by date_format(transaction_date,'%m-%y') order by month;
--Highest Income Users
select u.user_id,u.name,sum(t.amount) as total_income from users u join accounts a on u.user_id=a.user_id join transactions t on a.account_id=t.account_id where t.type='income' group by u.user_id,u.name order by total_income desc limit 10;
--Income by Occupation
select t.category,count(distinct u.user_id) as total_users,sum(t.amount) as total_income,avg(t.amount) as average_income from users u join accounts a on u.user_id=a.user_id join transactions t on a.account_id=t.account_id where t.type='income' group by u.occupation order by total_income desc;
--Income by City
select u.city,count(distinct u.user_id) as total_users,sum(t.amount) as total_income,avg(t.amount) as average_income from users u join accounts a on u.user_id=a.user_id join transactions t on a.account_id=t.account_id where t.type='income' group by u.city order by total_income desc;
--Users Who Exceeded Their Budgets
select u.user_id,u.name,b.category,b.monthly_limit,sum(t.amount) as total_expense,sum(t.amount)-b.monthly_limit as exceeded_amount from users u join budget b on u.user_id=b.user_id join accounts a on u.user_id=a.user_id join transactions t on a.account_id=t.account_id where t.type='expense' and b.category=t.category group by u.user_id,u.name,b.category,b.monthly_limit having total_expense>b.monthly_limit order by exceeded_amount desc;
--Remaining Budget for Each User and Category
select u.user_id,u.name,b.category,b.monthly_limit,sum(t.amount) as total_expense,b.monthly_limit-sum(t.amount) as remaining_budget from users u join budget b on u.user_id=b.user_id join accounts a on u.user_id=a.user_id join transactions t on a.account_id=t.account_id where t.type='expense' and b.category=t.category group by u.user_id,u.name,b.category,b.monthly_limit order by remaining_budget desc;
--Budget Utilization Percentage
select u.user_id,u.name,b.category,b.monthly_limit,sum(t.amount) as total_expense,round(sum(t.amount)/b.monthly_limit*100,2) as budget_utilization from users u join budget b on u.user_id=b.user_id join accounts a on u.user_id=a.user_id join transactions t on a.account_id=t.account_id where t.type='expense' and b.category=t.category group by u.user_id,u.name,b.category,b.monthly_limit order by budget_utilization desc;
--Users Savings Goals Completion Percentage
select u.user_id,u.name,s.goal_name,s.target_amount,s.current_amount,round((s.current_amount/s.target_amount)*100,2)as completion_percent from users u join savings_goals s on u.user_id=s.user_id order by completion_percent desc;
--Investment Allocation by Investment Type
select investment_type,count(*) as total_users,sum(amount) as total_investment,avg(amount) as average_investment from investment group by investment_type order by total_investment desc;
--Investment Return Percentage for Each User
select u.user_id,u.name,sum(i.amount) as total_investment,sum(i.current_value) as current_value,round((sum(i.current_value)-sum(i.amount))*100/sum(i.amount),0) as return_percent from users u join investment i on u.user_id=i.user_id group by u.user_id,u.name order by return_percent desc;