from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.dto.atendimento_validation_dto import (
    AtendimentoValidationDTO
)

from app.repositories.paciente_repository import (
    PacienteRepository
)

from app.repositories.consulta_repository import (
    ConsultaRepository
)

from app.services.atendimento_validation_service import (
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
        PacienteRepository(db)
    )

    consulta_repository = (
        ConsultaRepository(db)
    )

    service = (
        AtendimentoValidationService(
            paciente_repository,
            consulta_repository
        )
    )

    permitido = (
        service.pode_ser_atendido(
            dto
        )
    )

    return {
        "atendimento_liberado": permitido
    }