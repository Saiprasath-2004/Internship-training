BEGIN;

    UPDATE accounts
    SET balance = balance-2000
    WHERE user = 'Sai';

    UPDATE accounts
    SET balance = balance+2000
    WHERE user = 'Rahul';
    
COMMIT;
