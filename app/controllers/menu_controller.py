class MenuController :

    def executar(self):

        while True:

            self.exibir_menu()

            opcao = input(
                "------------ SISTEMA CLÍNICA VIDA+ ------------ " \
                " " \
                "1. Cadastrar paciente " \
                "2. Ver estatísticas " \
                "3. Buscar paciente " \
                "4. Listar todos os pacientes " \
                "5. Sair Escolha uma opção: ${opcao}"
            )

            match opcao:

                case "1":
                    self.login()

                case "2":
                    self.cadastrar_paciente()

                case "3":
                    self.agendar_consulta()

                case "4":
                    self.validar_atendimento()

                case "0":
                    break

                case _:
                    print(
                        "Opção inválida."
                    )