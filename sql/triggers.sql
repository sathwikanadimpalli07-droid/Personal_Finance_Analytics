--Create a BEFORE INSERT trigger to prevent negative transaction amounts
Delimiter $$ create trigger trg_negative_transaction before insert on transactions for each row begin if NEW.amount<0 then signal sqlstate '45000' set message_text='Transaction amount cannot be negative'; end if; end $$ delimiter ;
--Create a BEFORE INSERT trigger to prevent negative investment amounts
Delimiter $$ create trigger trg_negative_investment before insert on investment for each row begin if NEW.amount<0 then signal sqlstate '45000' set message_text='Investment amount cannot be negative'; end if; end$$ delimiter ;
--Create an AFTER INSERT trigger to update the account balance after an Income transaction
Delimiter $$ create trigger trg_update_after_income after insert on transactions for each row begin if NEW.type='Income' then update accounts set current_balance=current_balance+NEW.amount where account_id=NEW.account_id; end if; end $$ delimiter ;
--Create an AFTER INSERT trigger to deduct the account balance after an Expense transaction
Delimiter $$ create trigger trg_update_after_expense after insert on transactions for each row begin if NEW.type='Expense' then update accounts set current_balance=current_balance-NEW.amount where account_id=NEW.account_id; end if; end $$ delimiter ;
--Create a BEFORE UPDATE trigger to prevent account balance from becoming negative
Delimiter $$ create trigger trg_prevent_negative_balance before update on accounts for each row begin if new.current_balance<0 then signal sqlstate '45000' set message_text='Current balance cannot be negative'; end if; end $$ delimiter ;
--Create a BEFORE UPDATE trigger to prevent the savings goal target amount from being less than the current amount
Delimiter $$ create trigger trg_prevent_target_reduction before update on savings_goals for each row begin if new.target_amount<old.target_amount then signal sqlstate '45000' set message_text='Target amount cannot be reduced'; end if; end $$ delimiter ;
--Automatically update account's last_modified date whenever the balance changes
Delimiter $$ create trigger trg_last_modified after update on accounts for each row begin update accounts set last_updated=now() where account_id=new.account_id; end $$ delimiter ;
--Automatically restore account balance if an expense transaction is deleted
Delimiter $$ create trigger trg_restore_balance after delete on transactions for each row begin if old.type='expense' then update accounts set current_balance=current_balance+old.amount where account_id=old.account_id; end if; end $$ delimiter ;
--Automatically store account balance history after every update
Delimiter $$ create trigger trg_accounts_audit after update on accounts for each row begin insert into account_audit(account_id,old_balance,new_balance,action_time)values(old.account_id,old.current_balance,new.current_balance,now() ); end $$ delimiter ;
--Create an AFTER DELETE trigger to store deleted transactions in an audit table
Delimiter $$ create trigger trg_deleted_transaction after delete on transactions for each row begin insert into transaction_audit(transaction_id,account_id,amount,type,deleted_time)values(old.transaction_id,old.account_id,old.amount,old.type,now()); end $$ delimiter ;