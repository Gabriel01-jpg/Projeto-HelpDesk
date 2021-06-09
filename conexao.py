import sqlite3


class Conexao:

    def conectar(self):
        conexao = None
        db_path = 'banco.db'
        try:
            conexao = sqlite3.connect(
                db_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)

        except sqlite3.DatabaseError as err:
            print(f"Erro ao conectar o banco de dados {db_path}.")
        return conexao

    # def createTableDepartamento(self,conexao,cursor):
    #     cursor.execute('DROP TABLE IF EXISTS Departamento')

    #     sql = """CREATE TABLE IF NOT EXISTS Departamento (
    #                 id INTEGER PRIMARY KEY AUTOINCREMENT,
    #                 nome varchar NOT NULL);"""

    #     cursor.execute(sql)
    #     conexao.commit()

    # def createTableEmpregado(self,conexao,cursor):
    #     cursor.execute('DROP TABLE IF EXISTS Empregado')

    #     sql = """CREATE TABLE IF NOT EXISTS Empregado (
    #                 id INTEGER PRIMARY KEY AUTOINCREMENT,
    #                 cpf varchar NOT NULL UNIQUE,
    #                 nome varchar NOT NULL,
    #                 salario float NOT NULL,
    #                 fk_Departamento_id int,
    #                 FOREIGN KEY (fk_Departamento_id) REFERENCES Departamento (id));"""

    #     cursor.execute(sql)
    #     conexao.commit()

    # def createTablePlantao(self,conexao,cursor):
    #     cursor.execute('DROP TABLE IF EXISTS Plantao')

    #     sql = """CREATE TABLE IF NOT EXISTS Plantao (
    #                 id INTEGER PRIMARY KEY AUTOINCREMENT,
    #                 semana int NOT NULL,
    #                 data date NOT NULL ,
    #                 fk_Departamento_id int,
    #                 UNIQUE(semana, data ,fk_Departamento_id),
    #                 FOREIGN KEY (fk_Departamento_id) REFERENCES Departamento (id));"""

    #     cursor.execute(sql)
    #     conexao.commit()

    # def createTableEscala(self,conexao,cursor):
    #     cursor.execute('DROP TABLE IF EXISTS Escala')

    #     sql = """CREATE TABLE IF NOT EXISTS Escala (
    #                 fk_Empregado_id int,
    #                 fk_Plantao_id int,
    #                 hora time NOT NULL,
    #                 presenca int,
    #                 PRIMARY KEY (fk_Empregado_id, fk_Plantao_id, hora),
    #                 FOREIGN KEY (fk_Empregado_id) REFERENCES Empregado (id),
    #                 FOREIGN KEY (fk_Plantao_id) REFERENCES Plantao (id));"""

    #     cursor.execute(sql)
    #     conexao.commit()

    # def createTables(self):
    #     conexao = self.conectar()
    #     cursor = conexao.cursor()
    #     self.createTableDepartamento(conexao,cursor)
    #     self.createTableEmpregado(conexao,cursor)
    #     self.createTablePlantao(conexao,cursor)
    #     self.createTableEscala(conexao,cursor)
