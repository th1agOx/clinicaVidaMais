from pydantic import BaseModel


class AtendimentoValidationDTO(BaseModel):
    id_paciente: int