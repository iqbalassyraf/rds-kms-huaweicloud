import mysql.connector
from datetime import datetime

# Function to connect to the MySQL database
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host='119.13.106.119',  # Elastic IP address
            user='root',  # Your RDS login username
            password='Hadad27112022!!',  # Your RDS login password
            database='wallet-private-address'  # Your database name
        )
        print "Connected to MySQL database."
        return conn
    except mysql.connector.Error as e:
        print "Error connecting to MySQL database:", e
        return None

# Function to create a new wallet entry
def create_wallet(conn, private_wallet_name, owner_name, last_opened_date):
    cursor = conn.cursor()
    insert_query = '''INSERT INTO wallets (private_wallet_name, owner_name, last_opened_date) VALUES (%s, %s, %s)'''
    data = (private_wallet_name, owner_name, last_opened_date)
    try:
        cursor.execute(insert_query, data)
        conn.commit()
        print "Wallet entry created successfully."
    except mysql.connector.Error as e:
        print "Error creating wallet entry:", e

# Main function to interact with the user
def main():
    print "Welcome to the Wallet Management App!"
    print "--------------------------------------"

    conn = connect_to_database()
    if not conn:
        return

    while True:
        print "\nMenu:"
        print "1. Create a new wallet entry"
        print "2. Exit"

        choice = raw_input("Please enter your choice: ")

        if choice == '1':
            private_wallet_name = raw_input("Enter the private wallet name: ")
            owner_name = raw_input("Enter the owner's name: ")
            last_opened_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            create_wallet(conn, private_wallet_name, owner_name, last_opened_date)
        elif choice == '2':
            print "Exiting the application. Goodbye!"
            break
        else:
            print "Invalid choice. Please try again."

    conn.close()

if __name__ == "__main__":
    main()
