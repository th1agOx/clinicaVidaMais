from sqlalchemy.orm import Session

from app.models.consulta import Consulta


class ConsultaRepository:

    def __init__(self, db: Session):
        self.db = db

    def possui_agendamento(
        self,
        paciente_id: int
    ) -> bool:

        consulta = (
            self.db
            .query(Consulta)
            .filter(
                Consulta.id_paciente == paciente_id,
                Consulta.status == "agendada"
            )
            .first()
        )

        return consulta is not None

        listar_agendadas()

        listar_canceladas()

        listar_por_medico()

        listar_por_paciente()
### metodos da regra de negócio :
        existe_agendamento_paciente()

        verificar_horario_disponivel()

        confirmar_consulta()

        cancelar_consulta()