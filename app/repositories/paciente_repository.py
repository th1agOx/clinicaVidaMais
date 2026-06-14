from database.connection import get_db_connection

class PacienteRepository:

    def __init__(self, db):
        self.db = db

    def buscar_paciente_id(self, paciente_id: int) -> dict | None:
        cursor = self.db.cursor()
        
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
        return None
    
    def paciente_existe(self, paciente_id: int) -> bool:
        paciente = self.buscar_paciente_id(paciente_id)
        return paciente is not None