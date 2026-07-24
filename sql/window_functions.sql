--Rank users based on total expenses
select u.user_id,u.name,sum(t.amount) as total_expense,RANK() over(order by sum(t.amount) desc) as expense_rank from users u join accounts a on u.user_id=a.user_id join transactions t on a.account_id=t.account_id where t.type='expense' group by u.user_id,u.name;
--Find the Dense Rank of users based on income
select u.user_id,u.name,sum(t.amount) as total_income,dense_rank() over(order by sum(t.amount) desc) as income_rank from users u join accounts a on u.user_id=a.user_id join transactions t on a.account_id=t.account_id where t.type='income' group by u.user_id,u.name;
--Assign Row Numbers to every transaction
select transaction_id,account_id,transaction_date,amount,category ,type,row_number() over(order by transaction_date) as row_num from transactions;
--Find the previous transaction amount using LAG()
select transaction_id,account_id,transaction_date,amount,category,lag(amount) over(partition by account_id order by transaction_date) as previous_amount from transactions;
--Find the next transaction amount using LEAD()
select transaction_id,account_id,transaction_date,amount,lead(amount) over(partition by account_id order by transaction_date) as next_amount from transactions;
--Display the first transaction amount for every account using FIRST_VALUE()
select transaction_id,account_id,transaction_date,amount,first_value(amount) over(partition by account_id order by transaction_date) as first_transaction from transactions;
--Display the latest transaction amount for every account using LAST_VALUE()
select transaction_id,account_id,transaction_date,amount,last_value(amount) over(partition by account_id order by transaction_date rows between unbounded preceding and unbounded following) as last_transaction from transactions;
--Calculate the running total of expenses for each account
select account_id,transaction_date,amount,sum(amount) over(partition by account_id order by transaction_date) as running_total from transactions where type='expense';
--Calculate the moving average of expenses for each account
select account_id,transaction_date,amount,avg(amount) over(partition by account_id order by transaction_date rows between 2 preceding and current row) as moving_average from transactions where type='expense';
--Divide users into four spending groups using NTILE()
select user_id,name,total_expense,ntile(4) over(order by total_expense desc) as spending_group from (select u.user_id,u.name,sum(t.amount) as total_expense from users u join accounts a on u.user_id=a.user_id join transactions t on a.account_id=t.account_id where t.type='expense' group by u.user_id,u.name) as expense_summary;
--Calculate the cumulative number of transactions for each account
select account_id,transaction_date,amount,count(*) over(partition by account_id order by transaction_date) as transaction_count from transactions;
--Find the percentile rank of users based on total expenses
select user_id,name,total_expense,percent_rank() over(order by total_expense)as percentile_rank from (select u.user_id,u.name,sum(t.amount) as total_expense from users u join accounts a on u.user_id=a.user_id join transactions t on a.account_id=t.account_id where t.type='expense' group by u.user_id,u.name) as expense_summary;
--Calculate the cumulative distribution of users based on total income
select user_id,name,total_income,cume_dist() over(order by total_income)as cumulative_distribution from (select u.user_id,u.name,sum(t.amount) as total_income from users u join accounts a on u.user_id=a.user_id join transactions t on a.account_id=t.account_id where t.type='income' group by u.user_id,u.name) as income_summary;
--Display the second transaction amount for each account using NTH_VALUE()
select account_id,transaction_id,transaction_date,amount,nth_value(amount,2) over(partition by account_id order by transaction_date rows between unbounded preceding and unbounded following) as 2nd_transaction from transactions;
--Compare each transaction amount with the average transaction amount of its account
select account_id,transaction_id,transaction_date,amount,avg(amount) over(partition by account_id) as avg_amount,amount-avg(amount) over(partition by account_id) as Diff_from_avg from transactions;