--Display users with their account details
select u.user_id,u.name,a.account_id,a.bank_name from users as u join accounts as a on u.user_id=a.user_id;
--Display users with all their transaction details
select u.user_id,u.name,a.account_id,a.bank_name,t.transaction_date,t.amount from users as u join accounts as a on u.user_id=a.user_id join transactions as t on a.account_id=t.account_id;
--Display users with their budget details
select u.user_id,u.name,b.budget_id,b.category from users as u join budget as b on u.user_id=b.user_id;
--Display users with their investment details
select u.user_id,u.name,i.investment_id,i.investment_type from users as u join investment as i on u.user_id=i.user_id;
--Display users with their savings goals
select u.user_id,u.name,s.goal_id,s.goal_name from users as u join savings_goals as s on u.user_id=s.user_id;
--Display account details along with transaction details
select a.account_id,t.amount,t.category,t.type from accounts as a join transactions as t on a.account_id=t.account_id;
--Display investments with user details
select i.investment_id,i.user_id,i.investment_type,i.amount from investment as i join users as u on i.user_id=u.user_id;
--Display budget details with user information
select b.budget_id,u.user_id,b.category from budget as b join users as u on b.user_id=u.user_id;
--Display savings goal details with user information
select g.goal_id,u.user_id,g.goal_name,g.deadline from savings_goals as g join users as u on g.user_id=u.user_id;
--Display all users and their account details
select u.user_id,u.name,u.occupation,a.account_id,a.bank_name,a.account_type from users as u left join accounts as a on u.user_id=a.user_id;
--Display all users and their investment details
select u.user_id,u.name,u.occupation,i.investment_id,i.investment_type,i.amount from users as u left join investment as i on u.user_id=i.user_id;
--Display all users and their budget details
select u.user_id,u.name,u.occupation,b.budget_id,b.category,b.monthly_limit from users as u left join budget as b on u.user_id=b.user_id;
--Display all users and their savings goals
select u.user_id,u.name,u.occupation,g.goal_name,g.target_amount,g.deadline from users as u left join savings_goals as g on u.user_id=g.user_id;
--Find users without investments
select u.user_id,u.name,u.occupation from users as u left join investment as i on u.user_id=i.user_id where i.user_id is null;
--Find users without savings goals
select u.user_id,u.name,u.occupation from users as u left join savings_goals as g on u.user_id=g.user_id where g.user_id is null;
--Find users without savings goals
select u.user_id,u.name,u.occupation from users as u left join budget as b on u.user_id=b.user_id where b.user_id is null;
--Display all accounts with their user details
select u.user_id,u.name,a.account_id,a.bank_name,a.account_type from users as u right join accounts as a on u.user_id=a.user_id;
--Display all transactions with account details
select a.account_id,a.bank_name,a.account_type,t.transaction_id,t.amount,t.category,t.type from accounts a right join transactions t on a.account_id=t.account_id;
--Display all investments with user details
select u.user_id,u.name,i.investment_id,i.investment_type,i.amount from users u right join investment i on u.user_id=i.user_id;
--Display all budget records with user details
select u.user_id,u.name,b.budget_id,b.category,b.monthly_limit from users u right join budget b on u.user_id=b.user_id;
--Find users living in the same city
select u1.name as User1,u2.name as User2,u1.city as City from users u1 join users u2 on u1.city=u2.city and u1.user_id<u2.user_id order by u1.city;
--Find users having the same occupation
select u1.name as User1,u2.name as User2,u1.occupation as Occupation from users u1 join users u2 on u1.occupation=u2.occupation and u1.user_id<u2.user_id order by u1.occupation;
--Find users registered on the same date
select u1.name as User1,u2.name as User2,u1.registration_date as Registration_date from users u1 join users u2 on u1.registration_date=u2.registration_date and u1.user_id<u2.user_id order by u1.registration_date;
--Classify transactions as Small, Medium, or Large
select transaction_id,amount,category,type,case when amount<5000 then 'Small Transaction' when amount between 5000 and 15000 then 'Medium Transaction' else 'Large Transaction' end Transaction_size from transactions;
--Classify users by age group
select user_id,name,age,case when age<30 then 'Youth' when age between 30 and 50 then 'Adult' else 'Senior' end Age_group from users;
--Classify account balances
select account_id,current_balance,case when current_balance<25000 then 'Low Balance' when current_balance between 25000 and 75000 then 'Medium Balance' else 'High Balance' end Balance_status from accounts;
--Classify investments as Profit or Loss
select investment_id,investment_type,amount,current_value,case when current_value>amount then 'Profit' when current_value=amount then 'No profit No loss' else 'Loss' end Investment_status from investment;
--Classify savings goals
select goal_id,goal_name,target_amount,current_amount,case when current_amount>target_amount then 'Completed' else 'Not completed' end Savings_target from savings_goals;
--Find users who have investments
select u.user_id,u.name from users u where exists(select 1 from investment i where u.user_id=i.user_id);
--Find users who have transactions
select u.user_id,u.name from users u where exists(select 1 from accounts a join transactions t on a.account_id=t.account_id where u.user_id=a.user_id);
--Find users without budget details
select u.user_id,u.name from users u where not exists(select 1 from budget b where u.user_id=b.user_id);
--Find users without transactions
select u.user_id,u.name from users u where not exists(select 1 from accounts a join transactions t on a.account_id=t.account_id where u.user_id=a.user_id);
--Display investment amount using COALESCE
select u.user_id,u.name,coalesce(i.amount,0) as amount from users u left join investment i on u.user_id=i.user_id;
--Display current investment value
select u.user_id,u.name,coalesce(i.current_value,0) as current_value from users u left join investment i on u.user_id=i.user_id;
--Replace NULL monthly budget
select u.user_id,u.name,ifnull(b.monthly_limit,0) as monthly_budget from users u left join budget b on u.user_id=b.user_id;
--Replace NULL savings amount
select u.user_id,u.name,ifnull(g.current_amount,0) as current_amount from users u left join savings_goals g on u.user_id=g.user_id;
--Combine investment and savings amounts
select user_id,amount as financial_amount,'Investment' as Source from investment union select user_id,target_amount,'Savings_goals' from savings_goals;
--Combine investment and savings using union all
select user_id,amount as financial_amoutn,'Investment' as Source from investment union all select user_id,target_amount,'Saving_goals' from savings_goals;
--Compare Budget vs Actual Expenses
select u.user_id,u.name,b.category,b.monthly_limit as budget_amount,ifnull(sum(t.amount),0) as actual_expense,(b.monthly_limit-ifnull(sum(t.amount),0)) as remaining_budget from users u join budget b on u.user_id=b.user_id join accounts a on u.user_id=a.user_id left join transactions t on a.account_id=t.account_id where t.category=b.category and t.type='expense' group by u.user_id,u.name,b.category,b.monthly_limit order by u.user_id;
--Compare Income vs Investment Amount
select u.user_id,u.name,sum(case when t.type='Income' then t.amount else 0 end) Total_income,ifnull(sum(i.amount),0) as total_investment from users u join accounts a on u.user_id=a.user_id join transactions t on a.account_id=t.account_id left join investment i on u.user_id=i.user_id group by u.user_id,u.name order by total_income desc;