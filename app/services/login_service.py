class LoginService :

    def __init__(self,medico_repository):

        self.medico_repository = ( medico_repository )

    def autenticar_medico(self, email: str):

        medico = (
            self.medico_repository.buscar_por_email(
                email
            )
        )

        if medico is None:

            return None
        
        return medico