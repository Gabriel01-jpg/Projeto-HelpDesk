import sqlite3
from conexao import Conexao


class Incidentes:

    def cadastrar(
            self, fk_idCliente, fk_idProduto, descricaoIncidente, dataAberturaIncidente):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            cursor.execute("""INSERT INTO Incidentes
                    (fk_idCliente,fk_idProduto,descricaoIncidente,dataAberturaIncidente,statusIncidente)
                    VALUES (?,?,?,?,'Aberto')""", (fk_idCliente, fk_idProduto, descricaoIncidente, dataAberturaIncidente))

            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro no cadastro de Incidentes: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de inegridade: {}".format(e))
            return False

    def consultar(self):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        resultset = cursor.execute('SELECT * FROM incidentes').fetchall()

        cursor.close()
        conexao.close()
        return resultset

    def consultar_detalhes(self, idIncidente):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        resultset = cursor.execute(
            'SELECT * FROM Incidentes WHERE idIncidente = ?', (idIncidente)).fetchone()

        cursor.close()
        conexao.close()
        return resultset

    def consultar_ultimo_id(self):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        resultset = cursor.execute(
            'SELECT MAX(idIncidente) FROM Incidentes').fetchone()

        cursor.close()
        conexao.close()
        return resultset[0]

    def atualizar(self, idIncidente, descricaoIncidente):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            
            cursor.execute("""UPDATE Incidentes
                    SET descricaoIncidente = ?
                    WHERE idIncidente = (?)""", (descricaoIncidente, idIncidente))

            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro na atualização dos Incidentes: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de inegridade: {}".format(e))
            return False

    def excluir(self, idIncidente):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'DELETE FROM Incidentes WHERE idIncidente = (?)'
            cursor.execute(sql, [idIncidente])

            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro na exclusão do insidente: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de inegridade: {}".format(e))
            return False

    def consultaCliente(self):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        resultset = cursor.execute(
            'SELECT idCliente, nomeCliente ||" "|| sobrenomeCliente FROM Clientes').fetchall()

        cursor.close()
        conexao.close()
        return resultset

    def consultaProduto(self):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        resultset = cursor.execute(
            'SELECT idProduto, nomeProduto FROM Produtos').fetchall()

        cursor.close()
        conexao.close()
        return resultset

    def consultarListaCompleta(self, filtro='Geral'):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        sql1 = """
            SELECT
                cast(a.idIncidente as varchar) as idChamado,
                a.fk_idCliente,
                a.fk_idProduto,
                b.nomeCliente || ' ' || b.sobrenomeCliente as Solicitante,
                strftime('%d/%m/%Y', a.dataAberturaIncidente) as Dt_Abertura,
                a.statusincidente,
                a.descricaoIncidente
            FROM Incidentes as a,
                Clientes as b,
                Produtos as c
            WHERE a.fk_idCliente = b.idCliente
                AND a.fk_idProduto = c.idProduto
            ORDER BY b.nomeCliente"""

        sql2 = f"""SELECT
                cast(a.idIncidente as varchar) as idChamado,
                a.fk_idCliente,
                a.fk_idProduto,
                b.nomeCliente || ' ' || b.sobrenomeCliente as Solicitante,
                strftime('%d/%m/%Y', a.dataAberturaIncidente) as Dt_Abertura,
                a.statusincidente,
                a.descricaoIncidente
            FROM Incidentes as a,
                Clientes as b,
                Produtos as c
            WHERE a.fk_idCliente = b.idCliente
                AND a.fk_idProduto = c.idProduto
                AND a.idIncidente = {filtro}
            ORDER BY b.nomeCliente"""

        sql = sql1 if filtro == 'Geral' else sql2

        resultset = cursor.execute(sql).fetchall()

        cursor.close()
        conexao.close()
        return resultset


if __name__ == '__main__':
    valor = Incidentes.consultarListaCompleta()
    print(valor)
