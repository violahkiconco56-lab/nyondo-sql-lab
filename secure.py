import sqlite3

conn = sqlite3.connect('nyondo_stock.db')
cursor = conn.cursor()

# SAFE search function
def search_product_safe(name):
    query = "SELECT * FROM products WHERE name LIKE ?"
    cursor.execute(query, ('%' + name + '%',))
    return cursor.fetchall()

# SAFE login function
def login_safe(username, password):
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    return cursor.fetchone()


# TESTS (should all fail = safe)
print('Test 1:', search_product_safe("' OR 1=1--"))
print('Test 2:', search_product_safe("' UNION SELECT id,username,password,role FROM users--"))
print('Test 3:', login_safe("admin'--", 'anything'))
print('Test 4:', login_safe("' OR '1'='1", "' OR '1'='1"))