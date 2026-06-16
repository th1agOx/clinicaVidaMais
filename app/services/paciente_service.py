from app.models.paciente import Paciente

class PacienteService :

    def __init__(
        self,
        paciente_repository
    ):
        
        self.paciente_repository = (
            paciente_repository
        )

    def cadastrar_paciente(dto)