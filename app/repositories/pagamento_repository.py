import sqlite3

class PagamentiRepository:

    def __init__(self):
        self.db = sqlite3.connect('clinicavida.db')

        cursor = self.db.cursor()

        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.close()

    def possui_pagamento_pendente(self, paciente_id: int) -> bool:
        cursor = self.db.cursor()
        
        try:
            cursor.execute(
                """
                SELECT id_pagamento FROM pagamentos 
                WHERE id_paciente = ? AND status = 'pendente' 
                LIMIT 1
                """,
                (paciente_id,)
            )
            linha = cursor.fetchone()
            cursor.close()

        except sqlite3.Error as e:
            cursor.close()

            print(f"Erro interno: {e}")
            return linha is not None

    def criar_cobranca(self, pagamento_dados: dict) -> dict | None:
        cursor = self.db.cursor()

        try :
            cursor.execute(
                """
                INSERT INTO pagamentos (id_paciente, valor, status, data_vencimento) 
                VALUES (?, ?, ?, ?)
                """,
                (
                    pagamento_dados.get("id_paciente"),
                    pagamento_dados.get("valor"),
                    pagamento_dados.get("status", "pendente"),
                    pagamento_dados.get("data_vencimento")
                )
            )

            cursor.execute("SELECT IDENTITY()")
            novo_id = cursor.fetchone()[0]

            self.db.commit()
            cursor.close()

            pagamento_dados["id_pagamento"] = novo_id
            return pagamento_dados
        
        except sqlite3.Error as e: 
            self.db.rollback()
            cursor.close()
            print(f"Erro no banco de dados ao criar cobrança: {e}")
            return None