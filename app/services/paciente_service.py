from app.models.paciente import Paciente
from app.repositories.paciente_repository import PacienteRepository

class PacienteService :

    def __init__(self, paciente_repository):
        self.paciente_repository = ( paciente_repository )

    def calcular_media_idade_pacientes(self) -> float:
        idades = self.paciente_repository.listar_idades()

        total_pacientes = len(idades)
        if total_pacientes == 0:
            return 0.0
        
        soma_idades = sum(idades)
        media = soma_idades / total_pacientes

        return round(media, 2)