class MenuMedico:

    def __init__(self, consulta_service, receita_service):

        self.consulta_service = (
            consulta_service
        )

        self.receita_service = (
            receita_service
        )

    def cancelar(self):

        id_consulta = int(
            input(
                "Informe o ID da consulta: "
            )
        )

        self.consulta_service.cancelar(
            id_consulta
        )

    print(
        "Consulta cancelada."
    )

    def gerar_receita(self):

        id_consulta = int(
            input(
                "Informe o ID da consulta: "
            )
        )

        self.receita_service.gerar_receita(
            id_consulta
        )

    def executar(self):

        while True:

            self.exibir_menu()

            opcao = input(
                "------------ SISTEMA CLÍNICA VIDA+ ------------ " \
                " " \
                "1. Cancelar consulta " \
                "2 - Gerar Receita" \
                "0 - Sair" \
                f"Escolha uma opção :{opcao}"
            )

            match opcao:

                case "1":
                    self.cancelar()

                case "2":
                    self.gerar_receita()

                case "0":
                        break

                case _:
                    print(
                        "Opção inválida."
                    )