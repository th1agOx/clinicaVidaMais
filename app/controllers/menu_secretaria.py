from app.dto.AtendimentoValidationDTO import AtendimentoValidationDTO
from app.dto.CriarConsultaDTO import CriarConsultaDTO
from app.dto.PacienteDTO import PacienteDTO
 
class MenuSecretaria:
    
    def __init__(self, paciente_service, consulta_service, atendimento_service):

        self.paciente_service = (
            paciente_service
        )

        self.consulta_service = (
            consulta_service
        )

        self.atendimento_service = (
            atendimento_service
        )

    def cadastrar_paciente(self):

        print(
            "\n--- CADASTRO DE PACIENTE ---\n"
        )

        dto = PacienteDTO(

            nome=input(
                "Nome: "
            ),

            cpf=input(
                "CPF: "
            ),

            telefone=input(
                "Telefone: "
            ),

            email=input(
                "Email: "
            ),

            endereco=input(
                "Endereço: "
            ),

            data_nascimento=input(
                "Data nascimento (AAAA-MM-DD): "
            ),

            perfil="PACIENTE",

            tipo_usuario="PACIENTE",

            id_plano=input(
                "ID Plano (Enter para nenhum): "
            ) or None
        )

        try:

            paciente_id = (
                self.paciente_service
                .cadastrar(
                    dto
                )
            )

            print(
                f"\nPaciente cadastrado com sucesso! ID: {paciente_id}\n"
            )

        except Exception as e:

            print(
                f"\nErro ao cadastrar paciente: {e}\n"
            )

    def atualizar_paciente(self):

        print(
            "\n--- ATUALIZAÇÃO DE PACIENTE ---\n"
        )

        paciente_id = int(
            input(
                "Informe o ID do paciente: "
            )
        )

        paciente = (
            self.paciente_service
            .buscar_por_id(
                paciente_id
            )
        )

        if paciente is None:

            print(
                "\nPaciente não encontrado.\n"
            )

            return

        dto = PacienteDTO(

            id_paciente=paciente_id,

            nome=input(
                f"Nome [{paciente['nome']}]: "
            ) or paciente["nome"],

            cpf=input(
                f"CPF [{paciente['cpf']}]: "
            ) or paciente["cpf"],

            telefone=input(
                f"Telefone [{paciente['telefone']}]: "
            ) or paciente["telefone"],

            email=input(
                f"Email [{paciente['email']}]: "
            ) or paciente["email"],

            endereco=input(
                f"Endereço [{paciente['endereco']}]: "
            ) or paciente["endereco"],

            data_nascimento=input(
                f"Data nascimento [{paciente['data_nascimento']}]: "
            ) or paciente["data_nascimento"],

            perfil=paciente["perfil"],

            tipo_usuario=paciente["tipo_usuario"],

            id_plano=paciente["id_plano"]
        )

        try:

            self.paciente_service.atualizar(
                dto
            )

            print(
                "\nPaciente atualizado com sucesso.\n"
            )

        except Exception as e:

            print(
                f"\nErro ao atualizar paciente: {e}\n"
            )

    def remover_paciente(self):

        paciente_id = int(
            input(
                "Informe o ID do paciente: "
            )
        )

        self.paciente_service.remover(
            paciente_id
        )

    def listar_pacientes(self):

        pacientes = (
            self.paciente_service
            .listar_todos()
        )

        for paciente in pacientes:

            print(paciente)


    def buscar_paciente(self):

        nome = input(
            "Nome do paciente: "
        )

        pacientes = (
            self.paciente_service
            .buscar_por_nome(
                nome
            )
        )

    for paciente in pacientes:

        print(paciente)


    def agendar_consulta(self):

        dto = CriarConsultaDTO(

            id_paciente=int(
                input("Paciente: ")
            ),

            id_medico=int(
                input("Médico: ")
            ),

            data_hora=input(
                "Data/Hora: "
            ),

            queixa_principal=input(
                "Queixa principal: "
            )
        )

        self.consulta_service.agendar(
            dto
        )

    def validar_atendimento(self):

        dto = AtendimentoValidationDTO(

            id_paciente=int(
                input(
                    "Paciente: "
                )
            ),

            tipo_atendimento=input(
                "normal/emergencia: "
            )
        )

        resultado = (
            self.atendimento_service
            .validar(
                dto
            )
        )

        print(
            "Atendimento liberado"
            if resultado
            else
            "Atendimento bloqueado"
        )
    
      
    def executar (self):

        while True :

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
                        "7. Validar Atendimento"
                        "0. Sair" \
                        f"Escolha uma opção: {opcao}"
                    )
            
            match opcao:

                    case "1":
                        self.cadastrar_paciente()

                    case "2":
                        self.atualizar_paciente()

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