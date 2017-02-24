from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/movie', methods = ['POST'])
def movie():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    try:
        title = request.form['title']
        releaseyear = request.form['releaseyear']
        description = request.form['description']
        print('hello')
        cursor.execute('INSERT INTO movie (title, releaseyear, description) VALUES (?, ?, ?)', (title, releaseyear, description))
        connection.commit()
        message = 'Successfully added information into movies table'
    except:
        connection.rollback()
        message = 'Failed to add information into movies table'
    finally:
        connection.close()
        return str(message)

app.route('movies')
def movies():
    return render_tempplate('movies.html')

app.run(debug = True)
