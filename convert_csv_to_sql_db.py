import pandas as pd
from pandas.io import sql
import sqlite3

con = sqlite3.connect("books_50.db")

df = pd.read_csv('books_50.csv')
df.to_sql('books_50', con, if_exists='replace', index=False)

sql_statement = """
SELECT * FROM books_50
LIMIT 10"""

print(sql.read_sql(sql_statement, con = con))
