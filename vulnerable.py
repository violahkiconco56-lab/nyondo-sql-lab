import sqlite3

# connect to database
conn = sqlite3.connect('nyondo_stock.db')
cursor = conn.cursor()

# ---------------- ENSURE TABLES EXIST ----------------

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    role TEXT
)
''')

conn.commit()

# ---------------- SECURE FUNCTIONS ----------------

def search_product(name):
    query = "SELECT * FROM products WHERE name LIKE ?"
    rows = cursor.execute(query, (f"%{name}%",)).fetchall()
    print("\nSearch Results:", rows, "\n")
    return rows


def login(username, password):
    query = "SELECT * FROM users WHERE username=? AND password=?"
    row = cursor.execute(query, (username, password)).fetchone()
    print("\nLogin Result:", row, "\n")
    return row


# ---------------- TEST DATA (ONLY IF EMPTY) ----------------

cursor.execute("SELECT COUNT(*) FROM products")
if cursor.fetchone()[0] == 0:
    cursor.executemany(
        "INSERT INTO products (name, description, price) VALUES (?, ?, ?)",
        [
            ("Cement (bag)", "Portland cement", 35000),
            ("Iron sheets", "Roofing sheets", 80000),
            ("Bricks", "Clay bricks", 500)
        ]
    )

cursor.execute("SELECT COUNT(*) FROM users")
if cursor.fetchone()[0] == 0:
    cursor.executemany(
        "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
        [
            ("admin", "admin123", "admin"),
            ("user1", "pass123", "customer")
        ]
    )

conn.commit()

# ---------------- TESTS ----------------

search_product("cement")
login("admin", "admin123")

# close connection
conn.close()