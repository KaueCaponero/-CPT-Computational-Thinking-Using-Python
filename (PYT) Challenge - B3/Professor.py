from Usuario import Usuario
from Funcoes import Funcoes

class Professor(Usuario):
    def __init__(self, id_usuario=None, cpf_usuario=None, nome_usuario=None, email_usuario=None, cel_usuario=None):
        super().__init__(id_usuario=id_usuario, cpf_usuario=cpf_usuario, nome_usuario=nome_usuario, email_usuario=email_usuario, cel_usuario=cel_usuario)

    def cadastrarProfessor(dicProfessores, id_user):
        # INSTANCIANDO NOVO PROFESSOR - OK
        novo_professor = Professor()
        
        Funcoes.menuCabecalho

        # SETANDO ID DO USUÁRIO - OK
        id_usuario = id_user

        # SETANDO CPF DO USUÁRIO - OK
        cpf_usuario = input("DIGITE O SEU CPF (APENAS NÚMEROS, EXEMPLO: 43102154278): ")
        while (Funcoes.validarCPF(cpf_usuario) == False or cpf_usuario in [professor.cpf_usuario for professor in dicProfessores.values()]):
            print("CPF INVÁLIDO OU JÁ CADASTRADO.")
            cpf_usuario = input("DIGITE O SEU CPF (APENAS NÚMEROS, EXEMPLO: 43102154278): ")

        # SETANDO NOME DO USUÁRIO - OK
        nome_usuario = input("DIGITE O SEU NOME COMPLETO: ").upper()
        nome_usuario = Funcoes.validarPreenchimento("DIGITE O SEU NOME COMPLETO: ", nome_usuario)

        # SETANDO EMAIL DO USUÁRIO - OK
        email_usuario = input("DIGITE O SEU EMAIL: ").upper()
        email_usuario = Funcoes.validarPreenchimento("DIGITE O SEU EMAIL: ", email_usuario)
        while (email_usuario in [professor.email_usuario for professor in dicProfessores.values()]):
            print("EMAIL INVÁLIDO OU JÁ CADASTRADO.")
            email_usuario = input("DIGITE O SEU EMAIL: ").upper()

        # SETANDO CEL DO USUÁRIO - OK
        cel_usuario = input("DIGITE O SEU CELULAR (SOMENTE NÚMEROS, COM DDD, EXEMPLO: 11983050165): ")
        cel_usuario = Funcoes.validarPreenchimento("DIGITE O SEU CELULAR (SOMENTE NÚMEROS, COM DDD, EXEMPLO: 11983050165): ", cel_usuario)
        cel_usuario = Funcoes.validarCel(cel_usuario)
        while (cel_usuario in [professor.cel_usuario for professor in dicProfessores.values()]):
            print("CELULAR INVÁLIDO OU JÁ CADASTRADO.")
            cel_usuario = input("DIGITE O SEU CELULAR: ").upper()
            cel_usuario = Funcoes.validarPreenchimento("DIGITE O SEU CELULAR (SOMENTE NÚMEROS, COM DDD, EXEMPLO: 11983050165): ", cel_usuario)
            cel_usuario = Funcoes.validarCel(cel_usuario)

        print("------------------------------------------")

        # ADICIONANDO O PROFESSOR NO DICIONÁRIO DE PROFESSORES - OK
        novo_professor = Professor(id_usuario = id_usuario, cpf_usuario = cpf_usuario, nome_usuario = nome_usuario, email_usuario = email_usuario, cel_usuario = cel_usuario)
        dicProfessores[novo_professor.id_usuario] = novo_professor

        print("PROFESSOR CADASTRADO COM SUCESSO!")
        input("TECLE ENTER PARA VOLTAR AO MENU INICIAL\n")
    
    def perfilProfessor(professor_buscado):
        retornoPerfil = Funcoes.menuCabecalho()
        retornoPerfil += f"01. ID: {professor_buscado.id_usuario}\n"
        retornoPerfil += f"02. CPF: {Funcoes.formatarCpf(professor_buscado.cpf_usuario)}\n"
        retornoPerfil += f"03. NOME: {professor_buscado.nome_usuario}\n"
        retornoPerfil += f"04. EMAIL: {professor_buscado.email_usuario}\n"
        retornoPerfil += f"05. CELULAR: {Funcoes.formatarCel(professor_buscado.cel_usuario)}\n"
        retornoPerfil += "06. SAIR\n"
        retornoPerfil += Funcoes.menuRodape()
        return retornoPerfil