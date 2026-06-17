from app.services.login_service import LoginService 

class MenuController :

    def executar(self):

        while True:

            self.exibir_menu()

            email = input(
                "Informe seu email: "
            )

            medico = (
                LoginService.autenticar_medico(
                    email
                )
            )

            if medico:

                self.menu_medico(
                    medico
                )

            else:

                self.menu_secretaria()

          