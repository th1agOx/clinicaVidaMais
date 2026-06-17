from pydantic import BaseModel

from datetime import date

from app.enums.tipo_usuario import TipoUsuario

class PacienteDTO(BaseModel):

    id_paciente: int

    nome: str

    cpf: str

    telefone: str

    email: str

    endereco: str

    data_nascimento: date

    tipo_usuario: TipoUsuario

    id_plano: int