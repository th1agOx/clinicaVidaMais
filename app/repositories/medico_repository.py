class MedicoRepository:

    def __init__(self, db):

        self.db = db

    def buscar_medico_id(
        self,
        medico_id: int,
    ) -> dict | None:
        cursor = self.db.cursor()

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
        return None

    def medico_disponivel(
        self,
        medico_id: int,
        data_hora
    ) -> bool:
        cursor = self.db.cursor()

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

        return consulta is None
