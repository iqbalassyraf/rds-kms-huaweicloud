CREATE TABLE wallets (
                     id INTEGER PRIMARY KEY,
                     private_wallet_name TEXT,
                     owner_name TEXT,
                     last_opened_date TEXT
                  );
                  INSERT INTO wallets (private_wallet_name, owner_name, last_opened_date) VALUES ('Wallet1', 'John Doe', '2024-02-17 18:17:48');
INSERT INTO wallets (private_wallet_name, owner_name, last_opened_date) VALUES ('Wallet2', 'Jane Smith', '2024-02-17 18:17:48');
INSERT INTO wallets (private_wallet_name, owner_name, last_opened_date) VALUES ('Wallet3', 'Alice Johnson', '2024-02-17 18:17:48');
