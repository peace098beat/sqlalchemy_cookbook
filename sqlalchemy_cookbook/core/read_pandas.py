import sqlalchemy
import pandas as pd

# この例ではsqliteを使うが、
engine = sqlalchemy.create_engine('sqlite:///example.db')

# 例えば、PostgreSQLをかわりに使いたければ(ただしpsycopg2というライブラリに内部で依存)：
# engine = sqlalchemy.create_engine("postgresql://username:password@host/dbname")

query = 'select * from hoge'
df = pd.io.sql.read_sql(query, engine)
