import sqlite3

class PacienteRepository:

    def __init__(self):
        self.db = sqlite3.connect('clinicavida.db')

        cursor = self.db.cursor()

        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.close()

    def buscar_paciente_id(self, paciente_id: int) -> dict | None:
        cursor = self.db.cursor()
        
        try :
            cursor.execute(
                "SELECT id_paciente, nome FROM pacientes WHERE id_paciente = ?", 
                (paciente_id,)
            )
            linha = cursor.fetchone()
            cursor.close()

            if linha:
                return {
                    "id_paciente": linha[0],
                    "nome": linha[1]
                }
            
        except sqlite3.Error as e :
            cursor.close()

            print(f"Erro interno: {e}")
            return None
    
    def paciente_existe(self, paciente_id: int) -> bool:
        paciente = self.buscar_paciente_id(paciente_id)
        return paciente is not None
    
    def salvar(self, paciente):
        cursor = self.db.cursor()

        try :
            cursor.execute(
                """
                INSERT INTO pacientes
                (
                    nome,
                    cpf,
                    telefone,
                    email,
                    endereco,
                    data_nascimento,
                    perfil,
                    tipo_usuario,
                    id_plano
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    paciente.nome,
                    paciente.cpf,
                    paciente.telefone,
                    paciente.email,
                    paciente.endereco,
                    paciente.data_nascimento,
                    paciente.perfil,
                    paciente.tipo_usuario,
                    paciente.id_plano
                )
            )
            self.db.commit()
            return cursor.lastrowid
        
        except sqlite3.IntegrityError as e:
            self.db.rollback()

            print(f"Erro de integridade: {e} já existem" )
            return False

        except sqlite3.OperationalError as e:
            self.db.rollback()

            print(f"Erro de sintaxe no SQL: {e}")
            return False
        
        except sqlite3.Error as e:
            self.db.rollback()

            print(f"Erro no banco: {e}")
            return False

    
    def atualizar(self, paciente):
        cursor = self.db.cursor()

        try :            
            cursor.execute(
                """
                UPDATE pacientes
                SET
                    nome = ?,
                    cpf = ?,
                    telefone = ?,
                    email = ?,
                    endereco = ?,
                    data_nascimento = ?,
                    perfil = ?,
                    tipo_usuario = ?,
                    id_plano = ?

                WHERE id_paciente = ?
                """,
                (
                    paciente.nome,
                    paciente.cpf,
                    paciente.telefone,
                    paciente.email,
                    paciente.endereco,
                    paciente.data_nascimento,
                    paciente.perfil,
                    paciente.tipo_usuario,
                    paciente.id_plano,
                    paciente.id_paciente
                )
            )
            self.db.commit()
            return cursor.rowcount > 0
        
        except sqlite3.Error as e :
            self.db.rollback()

            print(f"Erro ao atualizar os dados do paciente {e}")
            return None
    
    def remover(self, paciente_id: int):
        cursor = self.db.cursor()
        
        try: 
            cursor.execute(
                """
                DELETE FROM pacientes
                WHERE id_paciente = ?
                """,
                (paciente_id,)
            )
            self.db.commit()

            if cursor.rowcount > 0:
                return True
            return False
        
        except sqlite3.IntegrityError as e:
            self.db.rollback()

            print(f"Não foi possível deletar esse paciente pois existem registros atrelados a ele: {e}")
            return False
        except sqlite3.OperationalError as e:
            self.db.rollback()

            print(f"Não foi possível executar a deleção do paciente: {e}")
            return False
        except sqlite3.Error as e:
            self.db.rollback()

            print(f"Erro no banco: {e}")
            return False

    def listar_todos(self):
        cursor = self.db.cursor()

        try:
            cursor.execute(
                """
                SELECT
                    id_paciente,
                    nome,
                    cpf,
                    telefone,
                    email,
                    endereco,
                    data_nascimento,
                    perfil,
                    tipo_usuario,
                    id_plano
                FROM pacientes
                ORDER BY nome
                """
            )
            return cursor.fetchall()
        
        except sqlite3.Error as e:
            cursor.close()

            print(f"Erro ao listar pacientes: {e}")
            return None

    
    def buscar_por_nome(self, nome: str):
        cursor = self.db.cursor()

        pacientes = []

        try :
            cursor.execute(
                """
                SELECT
                    id_paciente,
                    nome,
                    cpf,
                    telefone
                FROM pacientes
                WHERE nome LIKE ?
                """,
                (f"%{nome}%",)
            )

            pacientes == cursor.fetchall() 
            
            cursor.close()

            return [
                {
                    "id_paciente": p[0],
                    "nome": p[1],
                    "cpf": p[2],
                    "telefone": p[3]
                }
                for p in pacientes
            ]
        
        except sqlite3.Error as e :
            cursor.close()

            print(f"Erro interno: {e}")
            return False