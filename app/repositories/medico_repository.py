import sqlite3

class MedicoRepository:

    def __init__(self, db):
        self.db = db

    def buscar_medico_id(self, medico_id: int) -> dict | None:
        cursor = self.db.cursor()

        try :
            cursor.execute(
                "SELECT id_medico, nome, especialidade FROM medicos WHERE id_medico = ?", 
                (medico_id,)
            )
            linha = cursor.fetchone()
            cursor.close()
            
            if linha:
                return {
                    "id_medico": linha[0],
                    "nome": linha[1],
                    "especialidade": linha[2]
                }
        
        except sqlite3.Error as e :
            cursor.close()

            print(f"Erro interno: {e}")
            return None

    def medico_disponivel(self, medico_id: int, data_hora) -> bool:
        cursor = self.db.cursor()

        try :
            cursor.execute(
                """
                SELECT id_consulta FROM consultas 
                WHERE id_medico = ? AND data_hora = ? AND status = 'agendada'
                LIMIT 1
                """,
                (medico_id, str(data_hora))
            )
            consulta = cursor.fetchone()
            cursor.close()
        
        except sqlite3.Error as e:
            cursor.close()

            print(f"Erro Interno: {e}")
            return consulta is None


    def buscar_por_email(self, email: str):
        
        cursor = self.db.cursor()

        cursor.execute(
            """
            SELECT
                id_medico,
                crm,
                nome,
                especialidade,
                email
            FROM medicos
            WHERE email = ?
            """,
            (email,)
        )

        linha = cursor.fetchone()

        cursor.close()

        if linha:

            return {
                "id_medico": linha[0],
                "crm": linha[1],
                "nome": linha[2],
                "especialidade": linha[3],
                "email": linha[4]
            }

        return None