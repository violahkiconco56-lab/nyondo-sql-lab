import sqlite3

# connect to database (it will be created if it doesn't exist)
conn = sqlite3.connect('products.db')
cursor = conn.cursor()

# create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price INTEGER
)
""")

# clear old data (so you don’t get duplicates when running again)
cursor.execute("DELETE FROM products")

# insert sample data
cursor.executemany("""
INSERT INTO products (id, name, price) VALUES (?, ?, ?)
""", [
    (1, 'Cement', 35000),
    (2, 'Iron Sheet', 50000),
    (3, 'Nails', 10000),
    (4, 'Roofing Sheet', 45000),
    (5, 'Bricks', 20000)
])

conn.commit()

# ---------------- QUERIES ----------------

# Query A
print("\nQuery A:")
cursor.execute("SELECT * FROM products")
print(cursor.fetchall())

# Query B
print("\nQuery B:")
cursor.execute("SELECT name, price FROM products")
print(cursor.fetchall())

# Query C
print("\nQuery C:")
cursor.execute("SELECT * FROM products WHERE id = 3")
print(cursor.fetchall())

# Query D
print("\nQuery D:")
cursor.execute("SELECT * FROM products WHERE name LIKE '%sheet%'")
print(cursor.fetchall())

# Query E
print("\nQuery E:")
cursor.execute("SELECT * FROM products ORDER BY price DESC")
print(cursor.fetchall())

# Query F
print("\nQuery F:")
cursor.execute("SELECT * FROM products ORDER BY price DESC LIMIT 2")
print(cursor.fetchall())

# Query G (update + confirm)
print("\nQuery G:")
cursor.execute("UPDATE products SET price = 38000 WHERE id = 1")
conn.commit()

cursor.execute("SELECT * FROM products")
print(cursor.fetchall())

# close connection
conn.close()