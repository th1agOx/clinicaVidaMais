from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.dto.AtendimentoValidationDTO import (
    AtendimentoValidationDTO
)

from app.repositories.paciente_repository import (
    PacienteRepository
)

from app.repositories.consulta_repository import (
    ConsultaRepository
)

from app.services.atendimento_validationService import (
    AtendimentoValidationService
)

router = APIRouter(
    prefix="/atendimento",
    tags=["Atendimento"]
)


@router.post("/validar")
def validar_atendimento(
    dto: AtendimentoValidationDTO,
    db: Session = Depends(get_db)
):

    paciente_repository = (
        paciente_repository(db)
    )

    consulta_repository = (
        consulta_repository(db)
    )

    pagamento_repository = (
        paciente_repository(db)
    )

    medico_repository = (
        medico_repository(db)
    )

    service = (
        AtendimentoValidationService(
            paciente_repository,
            consulta_repository,
            pagamento_repository,
            medico_repository
        )
    )

    resultado = ( 
        service.validar(
            dto
        )
    )

    return {
        "atendimento_liberado": resultado,
    }