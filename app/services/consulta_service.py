from app.models.consulta import Consulta
from app.models.pagamento import Pagamento

class ConsultaService :

    def __init__(
        self,
        consulta_repository,
        paciente_repository,
        medico_repository,
        pagamento_repository
    ):

        self.consulta_repository = (
            consulta_repository
        )

        self.paciente_repository = (
            paciente_repository
        )

        self.medico_repository = (
            medico_repository
        )

        self.pagamento_repository = (
            pagamento_repository
        )

    def medico_disponivel(self, id_medico: int, data_hora) -> bool:
        
        return(
            self.medico_disponivel
            .medico_disponivel(
                id_medico,
                data_hora
            )
        )
    
    def agendar(self, dto):
        
        paciente = (
            self.paciente_repository
            .buscar_paciente_id(
                dto.id_paciente
            )
        )

        if paciente is None:

            raise ValueError(
                "Paciente não encontrado, ou não cadastrado."
            )
        
        medico = (
            self.medico_repository
            .buscar_medico_id(
                dto.id_medico
            )
        )

        if medico is None:

            raise ValueError(
                "Médico não encontrado, ou não cadastrado."
            )
        
        if not self.medico_disponivel(
            dto.id_medico,
            dto.data_hora
        ):
            
            raise ValueError(
                "Médico indisponível para o horário."
            )
        
        consulta = Consulta(

            id_paciente=dto.id_paciente,

            id_medico=dto.id_medico,

            data_hora=dto.data_hora,

            queixa_principal=dto.queixa_principal,

            status="agendada"
        )

        consulta = (
            self.pagamento_repository
            .salvar(
                consulta
            )
        )

        pagamento = Pagamento(

            id_paciente=dto.id_paciente,

            id_consulta=consulta.id_consulta,

            data_emissao=date.today(),

            data_vencimento=date.today(),

            status="pendente"
        )

        self.pagamento_repository.criar_cobranca(
            pagamento
        )

        return consulta
    
    def confirmar(self,id_consulta: int):
        
        consulta = (
            self.consulta_repository.buscar_consulta_id(
                id_consulta
            )
        )

        if consulta is None:

            raise ValueError(
                "Consulta não encontrada, ou não cadastrada."
            )
        
        consulta.status = "confirmada"

        return(
            self.consulta_repository
            .atualizar(
                consulta
            )
        )
    
    def cancelar(self,id_consulta: int):
        
        consulta = (
            self.consulta_repository
            .buscar_consulta_id(
                id_consulta
            )
        )

        if consulta is None:

            raise ValueError(
                "Consulta não encontrada"
            )
        
        consulta.status = "cancelada"

        return(
            self.consulta_repository.atualizar(
                consulta
            )
        )
    
    def listar_por_paciente(self,paciente_id: int):

        paciente = (
            self.paciente_repository
            .buscar_paciente_id(
                paciente_id
            )
        )

        if paciente is None:

            raise ValueError(
                "Paciente não encontrado."
            )

        return (
            self.consulta_repository
            .listar_por_paciente(
                paciente_id
            )
        )
    
    
    def listar_por_medico(self,medico_id: int):

        medico = (

            self.medico_repository
            .buscar_medico_id(
                medico_id
            )
        )

        if medico is None:

            raise ValueError(
                "Médico não encontrado."
            )

        return (

            self.consulta_repository
            .listar_por_medico(
                medico_id
            )
        )