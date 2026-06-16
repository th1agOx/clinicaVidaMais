class MenuController :

    def executar(self):

        while True:

            self.exibir_menu()

            opcao = input(
                "------------ SISTEMA CLÍNICA VIDA+ ------------ " \
                " " \
                "1. Cadastrar paciente " \
                "2 - Atualizar paciente" \
                "3 - Remover paciente" \
                "4. Buscar paciente " \
                "5. Listar todos os pacientes " \
                "6. Ver estatísticas " \
                "0. Sair" \
                f"7. Escolha uma opção: {opcao}"
            )

            match opcao:

                case "1":
                    self.login()

                case "2":
                    self.cadastrar_paciente()

                case "3":
                    self.remover_paciente()

                case "4":
                    self.buscar_paciente()

                case "5":
                    self.listar_pacientes()

                case "6":
                    self.agendar_consulta()

                case "7":
                    self.validar_atendimento()

                case "0":
                    break

                case _:
                    print(
                        "Opção inválida."
                    )