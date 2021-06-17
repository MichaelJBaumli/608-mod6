#Program Name: 608-ch17-part2.py
#Assignment Module 6
#Class 44680 Block 44599 Section 01
#Michael Baumli
#Date: 20210616


#Import Section
import sqlite3

connection = sqlite3.connect('books.db')

import pandas as pd

pd.options.display.max_columns = 10

results = pd.read_sql('SELECT * FROM authors', connection, index_col=['id'])

print(results)

results = pd.read_sql('SELECT * FROM titles',connection)

print(results)

df = pd.read_sql('SELECT * FROM author_ISBN',connection)

df.head()

results = pd.read_sql("""SELECT id,first, last FROM authors WHERE last LIKE 'Q%'""",connection, index_col=['id'])

print(results)

results = pd.read_sql('SELECT title FROM titles ORDER BY title ASC',connection)

print(results)

results = pd.read_sql("""SELECT id,first,last FROM authors ORDER BY last, first""",connection, index_col=['id'])

print(results)

results = pd.read_sql("""SELECT id,first,last FROM authors ORDER BY last DESC, first ASC""",connection, index_col=['id'])

print(results)

results = pd.read_sql("""SELECT isbn,title,edition,copyright FROM titles WHERE title LIKE '%How to Program' ORDER BY title""",connection)

print(results)