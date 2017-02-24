import sqlite3

connection = sqlite3.connect('database.db')
print('Database opened successfully')

connection.execute('CREATE TABLE IF NOT EXISTS movies (title TEXT, releaseyear INTEGER, description TEXT)')
print('Table created successfully')

connection.close()
