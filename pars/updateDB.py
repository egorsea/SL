import sqlite3
import pandas as pd

sql_delete_query = 'DELETE FROM main_inductive'
conn  = sqlite3.connect('dbtest.sqlite3')
cursor = conn.cursor()
cursor.execute(sql_delete_query)
conn.commit()
cursor.close()

with open(f'data/Индуктивные датчики ТЕКО dataframe.csv', encoding = 'utf-8') as f:
    df = pd.read_csv(f)
conn  = sqlite3.connect('dbtest.sqlite3')
df.to_sql(name='main_inductive', con=conn, if_exists='append', index=False)
conn.close()

with open(f'data/Индуктивные датчики SKB Ind dataframe.csv', encoding = 'utf-8') as f:
    df = pd.read_csv(f)
conn  = sqlite3.connect('dbtest.sqlite3')
df.to_sql(name='main_inductive', con=conn, if_exists='append', index=False)
conn.close()
