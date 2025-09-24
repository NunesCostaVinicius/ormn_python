from mysql.connector import (connection)
from mysql.connector import errorcode
import os
from load_dotenv import load_dotenv
load-dontv()
senha = os.getenv('SENHA_SQL')

bd_conexao = connection.MySQLConnection(
    host='localhost',
    user='root',
    password='root',
    database='bd_python'
)