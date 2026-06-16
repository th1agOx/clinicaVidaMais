
class PagamentoService:

    def __init__(
        self,
        pagamento_repository
    ):

        self.pagamento_repository = (
            pagamento_repository
        )
    
    def pagamento_em_dia(
        self,
        paciente_id: int
    ) -> bool:

        return not (
            self.pagamento_repository
            .possui_pagamentos_pendentes(
                paciente_id
        )
    )
    
