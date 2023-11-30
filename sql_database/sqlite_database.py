import sqlite3  # importing the sqlite module

# Connect to the database (creates a new database if it doesn't exixt)
conn = sqlite3.connect("mydatabase.db")

# create a cursor object to execute SQL queries.
cursor = conn.cursor()

# Create a table
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, salary REAL)''')

# insert data into the table
cursor.execute(
    "INSERT INTO employees(name, age, salary) VALUES ('Jane Smith', 23, 5500.0)")
cursor.execute(
    "INSERT INTO employees (name, age, salary) VALUES ('Damien', 32, 8000.0)")

# commit the changes to the database
conn.commit()

# retrieve the data from the table
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()

# print the retrieved data out.
for row in rows:
    print(row)

# update data in the table
cursor.execute("UPDATE employees SET salary = 9500.0 where name = 'Damien' ")
# commit the changes
conn.commit()

# Delete data from the table
cursor.execute("DELETE FROM employees where name = 'Jane Smith'")
conn.commit()

# close the cursor and the connection
cursor.close()
conn.close()
