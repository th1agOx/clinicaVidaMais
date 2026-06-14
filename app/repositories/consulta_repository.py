class ConsultaRepository:

    def __init__(self, db):
        
        self.db = db

    def buscar_consulta_id(self, consulta_id: int) -> dict | None:
        cursor = self.db.cursor()
        cursor.execute(
            """
            SELECT id_consulta, id_paciente, id_medico, data_hora, status 
            FROM consultas 
            WHERE id_consulta = ?
            """,
            (consulta_id,)
        )
        linha = cursor.fetchone()
        cursor.close()
        
        if linha:
            return {
                "id_consulta": linha[0],
                "id_paciente": linha[1],
                "id_medico": linha[2],
                "data_hora": str(linha[3]),
                "status": linha[4]
            }
        return None
    
    def listar_por_paciente(self, paciente_id: int) -> list:
        cursor = self.db.cursor()
        cursor.execute(
            """
            SELECT id_consulta, id_paciente, id_medico, data_hora, status 
            FROM consultas 
            WHERE id_paciente = ?
            """,
            (paciente_id,)
        )
        linhas = cursor.fetchall()
        cursor.close()

        consultas = []
        for linha in linhas:
            consultas.append({
                "id_consulta": linha[0],
                "id_paciente": linha[1],
                "id_medico": linha[2],
                "data_hora": str(linha[3]),
                "status": linha[4]
            })
        return consultas
    
    def listar_por_medico(self, medico_id: int) -> list:
        cursor = self.db.cursor()
        cursor.execute(
            """
            SELECT id_consulta, id_paciente, id_medico, data_hora, status 
            FROM consultas 
            WHERE id_medico = ?
            """,
            (medico_id,)
        )
        linhas = cursor.fetchall()
        cursor.close()

        consultas = []
        for linha in linhas:
            consultas.append({
                "id_consulta": linha[0],
                "id_paciente": linha[1],
                "id_medico": linha[2],
                "data_hora": str(linha[3]),
                "status": linha[4]
            })
        return consultas

    def atualizar(self, consulta_dados: dict) -> dict:
        """Atualiza os dados de uma consulta existente (ex: mudar status ou horário)"""
        cursor = self.db.cursor()
        cursor.execute(
            """
            UPDATE consultas 
            SET id_paciente = ?, id_medico = ?, data_hora = ?, status = ? 
            WHERE id_consulta = ?
            """,
            (
                consulta_dados.get("id_paciente"),
                consulta_dados.get("id_medico"),
                str(consulta_dados.get("data_hora")),
                consulta_dados.get("status"),
                consulta_dados.get("id_consulta")
            )
        )
        self.db.commit()
        cursor.close()
        return consulta_dados

    def consulta_valida(self, paciente_id: int) -> bool:
        cursor = self.db.cursor()
        cursor.execute(
            """
            SELECT id_consulta FROM consultas 
            WHERE id_paciente = ? AND status = 'agendada'
            LIMIT 1
            """,
            (paciente_id,)
        )
        consulta = cursor.fetchone()
        cursor.close()
        return consulta is not None
