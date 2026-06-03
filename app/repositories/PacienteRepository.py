from app.models import paciente
from models.paciente import Paciente
from sqlalchemy.orm import Session

class PacienteRepository:

    def __init__(self, db: Session):
        self.db = db

    def buscar_paciente_id(
        self,
        paciente_id: int
    ) -> Paciente | None:
        
        return(
            self.db
            .query(Paciente)
            .filter(
                Paciente.id_paciente == paciente_id
            )
            .first()
        )
    
    def paciente_existe(
        self,
        paciente_id: int
    ) -> bool:
        
        paciente = self.buscar_paciente_id(
            paciente_id
        )

        return paciente is not None