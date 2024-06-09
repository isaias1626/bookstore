import psycopg2
import os

try:
    connection = psycopg2.connect(
        database=os.environ.get('SQL_DATABASE'),
        user=os.environ.get('SQL_USER'),
        password=os.environ.get('SQL_PASSWORD'),
        host=os.environ.get('SQL_HOST'),
        port=os.environ.get('SQL_PORT'),
    )
    print("Conexão bem-sucedida!")
except Exception as e:
    print(f"Erro na conexão: {e}")
