from mysql.connector import (connection)
import os
from dotenv import load_dotenv

load_dotenv()
senha = os.getenv('SENHA_SQL')

conecao = connection.MySQLConnection(
    host='localhost',
    user='root',
    password=senha,
    database='bd_python'
)

comando = conecao.cursor()

class Aluno:
    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano
        comando.execute(
            "INSERT INTO ALUNOS (nome, ano) VALUES (%s, %s)",
            (self.nome, self.ano))
        comando.execute("SELECT * FROM ALUNOS")
        self.id = comando.fetchall()[-1]
        print(f'Aluno {self.nome} inserido com ID {self.id[0]}')

    def get(self):
        comando.execute(f"SELECT * FROM ALUNOS WHERE id = {self.id[0]}")
        return comando.fetchone()
    
    def close(self):
        comando.close()
        conecao.close()

    def salvar(self):
        conecao.commit()
        print("Alterações salvas no banco de dados.")