from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/movie')
def movie():
    return render_template('movie.html')

@app.route('/add_movie', methods = ['POST'])
def addmovie():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    try:
        title = request.form['title']
        releaseyear = request.form['releaseyear']
        description = request.form['description']
        cursor.execute('INSERT INTO movies (title, releaseyear, description) VALUES (?, ?, ?)', (title, releaseyear, description))
        connection.commit()
        message = 'Successfully added information into the movies table'
    except:
        connection.rollback()
        message = 'Failed to add information into the movies table'
    finally:
        connection.close()
        return str(message)

@app.route('/movies')
def movies():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    try:
        cursor.execute('SELECT * FROM movies')
        movies = cursor.fetchall()
        message = 'Movies found'
    except:
        connection.rollback()
        message = 'Failed to find movies'
    finally:
        connection.close()
        return jsonify(movies)

@app.route('/search')
def search():
    return render_template('/search.html')

@app.route('/search_title', methods = ['GET'])
def searchtitle():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    try:
        title = (request.args.get('title'),)
        cursor.execute('SELECT * FROM movies WHERE title = ?', title)
        data = cursor.fetchall()
        return jsonify(data)
    except:
        return "Invalid search"
        connection.close()

app.run(debug = True)
