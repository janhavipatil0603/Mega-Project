import sqlite3

def create_db():
    # Connect to SQLite database (it will create the file if it doesn't exist)
    conn = sqlite3.connect('disaster_relief.db')
    cursor = conn.cursor()

    # Create Users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        aadhar_number TEXT UNIQUE NOT NULL,
                        name TEXT NOT NULL)''')

    # Create Distributors table
    cursor.execute('''CREATE TABLE IF NOT EXISTS distributors (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        distributor_status TEXT NOT NULL)''')

    # Create Responses table
    cursor.execute('''CREATE TABLE IF NOT EXISTS responses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        distributor_id INTEGER,
                        resources_received TEXT,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY (user_id) REFERENCES users(id),
                        FOREIGN KEY (distributor_id) REFERENCES distributors(id))''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Create database and tables when running the script
if __name__ == "__main__":
    create_db()
