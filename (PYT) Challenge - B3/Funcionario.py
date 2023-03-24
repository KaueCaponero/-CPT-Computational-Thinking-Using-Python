from Usuario import Usuario
from Funcoes import Funcoes

class Funcionario(Usuario):
    def __init__(self, id_usuario=None, cpf_usuario=None, nome_usuario=None, email_usuario=None, cel_usuario=None,
                 senha_usuario=None, cargo_funcionario=None):
        super().__init__(id_usuario=id_usuario, cpf_usuario=cpf_usuario, nome_usuario=nome_usuario,
                         email_usuario=email_usuario, cel_usuario=cel_usuario)
        self.__senha_usuario = senha_usuario
        self.__cargo_funcionario = cargo_funcionario
    
    @property
    def senha_usuario(self):
        return self.__senha_usuario
    
    @senha_usuario.setter
    def senha_usuario(self, senha_usuario):
        self.__senha_usuario = senha_usuario
    
    @property
    def cargo_funcionario(self):
        return self.__cargo_funcionario
    
    @cargo_funcionario.setter
    def cargo_funcionario(self, cargo_funcionario):
        self.__cargo_funcionario = cargo_funcionario

    def cadastrarFuncionario(dicFuncionarios, id_user):
        # INSTANCIANDO NOVO FUNCIONÁRIO - OK
        novo_funcionario = Funcionario()
        
        Funcoes.menuCabecalho

        # SETANDO ID DO USUÁRIO - OK
        id_usuario = id_user

        # SETANDO CPF DO USUÁRIO - OK
        cpf_usuario = input("DIGITE O SEU CPF (APENAS NÚMEROS, EXEMPLO: 43102154278): ")
        while (Funcoes.validarCPF(cpf_usuario) == False or cpf_usuario in [funcionario.cpf_usuario for funcionario in dicFuncionarios.values()]):
            print("CPF INVÁLIDO OU JÁ CADASTRADO.")
            cpf_usuario = input("DIGITE O SEU CPF (APENAS NÚMEROS, EXEMPLO: 43102154278): ")

        # SETANDO NOME DO USUÁRIO - OK
        nome_usuario = input("DIGITE O SEU NOME COMPLETO: ").upper()
        nome_usuario = Funcoes.validarPreenchimento("DIGITE O SEU NOME COMPLETO: ", nome_usuario)

        # SETANDO EMAIL DO USUÁRIO - OK
        email_usuario = input("DIGITE O SEU EMAIL: ").upper()
        email_usuario = Funcoes.validarPreenchimento("DIGITE O SEU EMAIL: ", email_usuario)
        while (email_usuario in [funcionario.email_usuario for funcionario in dicFuncionarios.values()]):
            print("EMAIL INVÁLIDO OU JÁ CADASTRADO.")
            email_usuario = input("DIGITE O SEU EMAIL: ").upper()
            email_usuario = Funcoes.validarPreenchimento("DIGITE O SEU EMAIL: ", email_usuario)

        # SETANDO CEL DO USUÁRIO - OK
        cel_usuario = input("DIGITE O SEU CELULAR (SOMENTE NÚMEROS, COM DDD, EXEMPLO: 11983050165): ")
        cel_usuario = Funcoes.validarPreenchimento("DIGITE O SEU CELULAR (SOMENTE NÚMEROS, COM DDD, EXEMPLO: 11983050165): ", cel_usuario)
        cel_usuario = Funcoes.validarCel(cel_usuario)
        while (cel_usuario in [funcionario.cel_usuario for funcionario in dicFuncionarios.values()]):
            print("CELULAR INVÁLIDO OU JÁ CADASTRADO.")
            cel_usuario = input("DIGITE O SEU CELULAR: ").upper()
            cel_usuario = Funcoes.validarPreenchimento("DIGITE O SEU CELULAR (SOMENTE NÚMEROS, COM DDD, EXEMPLO: 11983050165): ", cel_usuario)
            cel_usuario = Funcoes.validarCel(cel_usuario)

        # SETANDO O CARGO DO FUNCIONÁRIO - OK
        cargo_funcionario = input("DIGITE O CARGO DO FUNCIONÁRIO: ").upper()
        cargo_funcionario = Funcoes.validarPreenchimento("DIGITE O CARGO DO FUNCIONÁRIO: ", cargo_funcionario)

        print("------------------------------------------")

        # ADICIONANDO O FUNCIONÁRIO NO DICIONÁRIO DE FUNCIONÁRIOS - OK
        novo_funcionario = Funcionario(id_usuario = id_usuario, cpf_usuario = cpf_usuario, nome_usuario = nome_usuario, email_usuario = email_usuario, cel_usuario = cel_usuario, cargo_funcionario = cargo_funcionario)
        dicFuncionarios[novo_funcionario.id_usuario] = novo_funcionario

        print("FUNCIONÁRIO CADASTRADO COM SUCESSO!")
        input("TECLE ENTER PARA VOLTAR AO MENU INICIAL\n")
    
    def perfilFuncionario(funcionario_buscado):
        retornoPerfil = Funcoes.menuCabecalho()
        retornoPerfil += f"01. ID: {funcionario_buscado.id_usuario}\n"
        retornoPerfil += f"02. CPF: {Funcoes.formatarCpf(funcionario_buscado.cpf_usuario)}\n"
        retornoPerfil += f"03. NOME: {funcionario_buscado.nome_usuario}\n"
        retornoPerfil += f"04. EMAIL: {funcionario_buscado.email_usuario}\n"
        retornoPerfil += f"05. CELULAR: {Funcoes.formatarCel(funcionario_buscado.cel_usuario)}\n"
        retornoPerfil += f"06. CARGO: {funcionario_buscado.cargo_funcionario}\n"
        retornoPerfil += "07. SAIR\n"
        retornoPerfil += Funcoes.menuRodape()
        return retornoPerfil
