import pandas as pd
from pandas.io import sql
from sqlalchemy import create_engine
import os


username = os.getenv('DB_USERNAME')
database_name = os.getenv('DB_NAME')
password = os.getenv('DB_PASSWORD')

port = 5432

engine = create_engine(f'postgresql://{username}:{password}@postgres:{port}/{database_name}')
df = pd.read_csv('books_50.csv')
df.to_sql('books_50', engine, if_exists='replace', index=False)

sql_statement = """
SELECT * FROM books_50
LIMIT 10"""

print(sql.read_sql(sql_statement, con=engine))
