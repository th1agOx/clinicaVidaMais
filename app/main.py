from app.controllers.menu_controller import (
    MenuController
    )

from app.controllers.menu_secretaria import (
    MenuSecretaria
)

### REPOSITORY

from app.repositories.paciente_repository import (
    PacienteRepository
)

from app.repositories.consulta_repository import (
    ConsultaRepository
)

from app.repositories.medico_repository import (
    MedicoRepository
)

from app.repositories.pagamento_repository import (
    PagamentoRepository
)

### SERVICE

from app.services.paciente_service import (
    PacienteService
)

from app.services.consulta_service import (
    ConsultaService
)

from app.services.atendimento_validation_service import (
    AtendimentoValidationService
)

import sqlite3

db = sqlite3.connect(
    "clinicavida.db"
)

paciente_repository = (
    PacienteRepository(db)
)

consulta_repository = (
    ConsultaRepository(db)
)

medico_repository = (
    MedicoRepository(db)
)

pagamento_repository = (
    PagamentoRepository(db)
)

paciente_service = (
    PacienteService(
        paciente_repository
    )
)

consulta_service = (
    ConsultaService(
        consulta_repository,
        paciente_repository,
        medico_repository,
        pagamento_repository
    )
)

atendimento_service = (
    AtendimentoValidationService(
        paciente_repository,
        consulta_repository,
        pagamento_repository
    )
)

menu_secretaria = (
    MenuSecretaria(
        paciente_service,
        consulta_service,
        atendimento_service
    )
)

menu_secretaria.executar()

if __name__ == "__main__":

    menu = MenuController()

    menu.executar()