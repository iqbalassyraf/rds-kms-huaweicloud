from datetime import datetime

# Function to generate a SQL script file
def generate_sql_script():
    # Open the SQL script file in write mode
    with open('example_database.sql', 'w') as f:
        # Write SQL commands to create the table
        f.write('''CREATE TABLE wallets (
                     id INTEGER PRIMARY KEY,
                     private_wallet_name TEXT,
                     owner_name TEXT,
                     last_opened_date TEXT
                  );
                  ''')

        # Write SQL commands to insert sample data
        wallets_data = [
            ('Wallet1', 'John Doe', datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
            ('Wallet2', 'Jane Smith', datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
            ('Wallet3', 'Alice Johnson', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        ]
        for wallet in wallets_data:
            f.write("INSERT INTO wallets (private_wallet_name, owner_name, last_opened_date) VALUES ('{}', '{}', '{}');\n".format(wallet[0], wallet[1], wallet[2]))

    print("SQL script generated successfully.")

if __name__ == "__main__":
    generate_sql_script()
