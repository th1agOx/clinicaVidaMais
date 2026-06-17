from app.dto.AtendimentoValidationDTO import (
    AtendimentoValidationDTO
)

class AtendimentoValidationService:

    def __init__(
        self,
        paciente_repository,
        consulta_repository,
        pagamento_repository
    ):

        self.paciente_repository = paciente_repository

        self.consulta_repository = consulta_repository

        self.pagamento_repository = pagamento_repository

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
        
        return (
            paciente.nome is not None
            and 
            paciente.cpf is not None
        )

    def consulta_valida( ##pós agendamento
        self,
        paciente_id: int
    ) -> bool:

        return (
            self.consulta_repository
            .consulta_valida(
                paciente_id
            )
        )

    def pagamento_em_dia(
        self,
        paciente_id : int
    ) -> bool:

        return not (
            self.pagamento_repository
            .possui_pagamento_pendente(
                paciente_id
            )
        )
    
    def validar_atendimento_normal(
        self,
        dto
    ) -> bool:

        return (

            self.consulta_valida(
                dto.id_paciente
            )

            and

            self.documentos_validos(
                dto.id_paciente
            )

            and

            self.pagamentos_em_dia(
                dto.id_paciente
            )
        )
    
    def validar_atendimento_emergencial(
        self,
        dto
    ) -> bool:

        return (

            self.consulta_valida(
                dto.id_paciente
            )

            and

            self.documentos_validos(
                dto.id_paciente
            )

            or

            self.pagamentos_em_dia(
                dto.id_paciente
            )
        )
    
    def validar(
        self,
        dto: AtendimentoValidationDTO
    ) -> bool:
        
        if dto.tipo_atendimento == "emergencia":

            return self.validar_atendimento_emergencial(
                dto
            )
        return self.validar_atendimento_normal(
            dto
        )   