"""
https://docs.python.org/3/library/sqlite3.html
"""
import sqlite3

con = sqlite3.connect("tutorial.db")  # connection to the database (implicitly creating it if it does not exist)
cur = con.cursor()  # vytvoření kurzoru pro práci s databází
# create a database table movie with columns for title, release year, and review score:
cur.execute("CREATE TABLE movie(title, year, score)")
