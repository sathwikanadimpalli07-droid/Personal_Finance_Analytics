LOAD DATA LOCAL INFILE 'C:/Users/nadim/OneDrive/Documents/GitHub/Personal_Finance_Analytics/datasets/savings_goals.csv'
INTO TABLE savings_goals
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(goal_id,user_id,goal_name,target_amount,current_amount,deadline);
select count(*) from savings_goals;
select count(*) from investment;
select count(*) from budget;
select count(*) from transactions;
select count(*) from accounts;
select count(*) from users;