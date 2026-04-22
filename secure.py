import sqlite3

conn = sqlite3.connect('nyondo_stock.db')
cursor = conn.cursor()

# -------- VALIDATION --------

def is_valid_name(name):
    if not isinstance(name, str) or len(name) < 2:
        return False
    if '<' in name or '>' in name or ';' in name:
        return False
    return True

def is_valid_username(username):
    if not isinstance(username, str) or username.strip() == "":
        return False
    if " " in username:
        return False
    return True

def is_valid_password(password):
    if not isinstance(password, str) or len(password) < 6:
        return False
    return True

# -------- SECURE FUNCTIONS --------

def search_product_safe(name):
    if not is_valid_name(name):
        print("Invalid product name")
        return None

    cursor.execute("SELECT * FROM products WHERE name LIKE ?", ('%' + name + '%',))
    return cursor.fetchall()


def login_safe(username, password):
    if not is_valid_username(username):
        print("Invalid username")
        return None

    if not is_valid_password(password):
        print("Invalid password")
        return None

    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    return cursor.fetchone()

# -------- TESTS --------

print("Test 1:", search_product_safe('cement'))
print("Test 2:", search_product_safe(''))
print("Test 3:", search_product_safe('<script>'))
print("Test 4:", login_safe('admin', 'admin123'))
print("Test 5:", login_safe('admin', 'ab'))
print("Test 6:", login_safe('ad min', 'pass123'))