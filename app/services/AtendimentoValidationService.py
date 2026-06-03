from app.dto.AtendimentoValidationDTO import (
    AtendimentoValidationDTO
)

class AtendimentoValidationService:

    def __init__(
        self,
        paciente_repository,
        consulta_repository
    ):

        self.paciente_repository = (
            paciente_repository
        )

        self.consulta_repository = (
            consulta_repository
        )

    def documentos_validos(
        self,
        paciente_id: int
    ) -> bool:

        paciente = (
            self.paciente_repository
            .buscar_por_id(
                paciente_id
            )
        )

        if paciente is None:
            return False

        if not paciente.nome:
            return False

        if not paciente.cpf:
            return False

        return True

    def possui_agendamento(
        self,
        paciente_id: int
    ) -> bool:

        return (
            self.consulta_repository
            .possui_agendamento(
                paciente_id
            )
        )

    def pode_ser_atendido(
        self,
        dto: AtendimentoValidationDTO
    ) -> bool:

        return (

            self.documentos_validos(
                dto.id_paciente
            )

            and

            self.possui_agendamento(
                dto.id_paciente
            )
        )