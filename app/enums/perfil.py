from enum import Enum

class Perfil(str, Enum):

    SECRETARIA = "secretaria"

    MEDICO = "medico"

    ADMIN = "admin"

    PASCIENTE = "paciente"