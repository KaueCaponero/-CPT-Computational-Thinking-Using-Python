from Usuario import Usuario
from Funcoes import Funcoes
from datetime import datetime
from Level import Level

class Aluno(Usuario):
    def __init__(self, id_usuario=None, cpf_usuario=None, nome_usuario=None, email_usuario=None, cel_usuario=None, 
                 data_nasc_aluno=None, data_registro_aluno=None, senha_usuario=None, moedas_aluno=None, 
                 level_aluno=None, produtos_aluno=None, certificados_aluno=None):
        
        super().__init__(id_usuario=id_usuario, cpf_usuario=cpf_usuario, nome_usuario=nome_usuario, 
                         email_usuario=email_usuario, cel_usuario=cel_usuario)
        
        self._data_nasc_aluno = data_nasc_aluno
        self._data_registro_aluno = data_registro_aluno
        self._senha_usuario = senha_usuario
        self._moedas_aluno = moedas_aluno
        self._level_aluno = level_aluno
        self._produtos_aluno = produtos_aluno if produtos_aluno is not None else []
        self._certificados_aluno = certificados_aluno

    # GETTERS E SETTERS - DATA DE NASCIMENTO DO ALUNO - OK    
    @property
    def data_nasc_aluno(self):
        return self._data_nasc_aluno
    
    @data_nasc_aluno.setter
    def data_nasc_aluno(self, data_nasc_aluno):
        self._data_nasc_aluno = data_nasc_aluno
    
    # GETTERS E SETTERS - DATA DE REGISTRO DO ALUNO - OK
    @property
    def data_registro_aluno(self):
        return self._data_registro_aluno
    
    @data_registro_aluno.setter
    def data_registro_aluno(self, data_registro_aluno):
        self._data_registro_aluno = data_registro_aluno
    
    # GETTERS E SETTERS - SENHA DO USUÁRIO - OK
    @property
    def senha_usuario(self):
        return self._senha_usuario
    
    @senha_usuario.setter
    def senha_usuario(self, senha_usuario):
        self._senha_usuario = senha_usuario
    
    # GETTERS E SETTERS - MOEDAS DO ALUNO - OK
    @property
    def moedas_aluno(self):
        return self._moedas_aluno
    
    @moedas_aluno.setter
    def moedas_aluno(self, moedas_aluno):
        self._moedas_aluno = moedas_aluno
    
    # GETTERS E SETTERS - LEVEL DO ALUNO - OK
    @property
    def level_aluno(self):
        return self._level_aluno
    
    @level_aluno.setter
    def level_aluno(self, level_aluno):
        self._level_aluno = level_aluno
    
    # GETTERS E SETTERS - PRODUTOS DO ALUNO - OK
    @property
    def produtos_aluno(self):
        return self._produtos_aluno
    
    def add_produto(self, produto):
        self._produtos_aluno.append(produto)
    
    def remove_produto(self, produto):
        self._produtos_aluno.remove(produto)
    
    # GETTERS E SETTERS - CERTIFICADOS DO ALUNO - OK
    @property
    def certificados_aluno(self):
        return self._certificados_aluno
    
    def add_certificado(self, certificado):
        self._certificados_aluno.append(certificado)

    def remove_certificado(self, certificado):
        self._certificados_aluno.remove(certificado)

    # MÉTODOS DA CLASSE ALUNO - OK

    def cadastrarAluno(id_user, dicAlunos, cpfs_cadastrados, emails_cadastrados, cel_cadastrados):
        # INSTANCIANDO NOVO ALUNO - OK
        novo_aluno = Aluno()
        novo_aluno.id_usuario = novo_aluno.setarNomeUser()


    def cadastrarAluno(cpfs_cadastrados, emails_cadastrados, cel_cadastrados, dicAlunos, id_user):
        # INSTANCIANDO NOVO ALUNO - OK
        novo_aluno = Aluno()

        Funcoes.menuCabecalho

        # SETANDO ID DO USUÁRIO - OK
        id_usuario = id_user

        # SETANDO CPF DO USUÁRIO - OK
        cpf_usuario = input("DIGITE O SEU CPF (APENAS NÚMEROS, EXEMPLO: 43102154278): ")
        cpf_usuario = Funcoes.verificarCPF(cpf_usuario, cpfs_cadastrados)
        cpfs_cadastrados.add(cpf_usuario)

        # SETANDO NOME DO USUÁRIO - OK
        nome_usuario = input("DIGITE O SEU NOME COMPLETO: ").upper()
        nome_usuario = Funcoes.validarPreenchimento("DIGITE O SEU NOME COMPLETO: ", nome_usuario)

        # SETANDO EMAIL DO USUÁRIO - OK
        email_usuario = input("DIGITE O SEU EMAIL: ").upper()
        email_usuario = Funcoes.validarPreenchimento("DIGITE O SEU EMAIL: ", email_usuario)
        email_usuario = Funcoes.verificarEmail(email_usuario, emails_cadastrados)
        emails_cadastrados.add(email_usuario)

        # SETANDO CEL DO USUÁRIO - OK
        cel_usuario = input("DIGITE O SEU CELULAR (SOMENTE NÚMEROS, COM DDD, EXEMPLO: 11983050165): ")
        cel_usuario = Funcoes.validarPreenchimento("DIGITE O SEU CELULAR (SOMENTE NÚMEROS, COM DDD, EXEMPLO: 11983050165): ", cel_usuario)
        cel_usuario = Funcoes.verificarCel(cel_usuario, cel_cadastrados)
        cel_cadastrados.add(cel_usuario)

        # SETANDO DATA DE NASCIMENTO DO USUÁRIO - OK
        data_nasc_usuario = input("DIGITE A SUA DATA DE NASCIMENTO (DD/MM/YYYY): ")
        data_nasc_usuario = Funcoes.validarPreenchimento("DIGITE A SUA DATA DE NASCIMENTO (DD/MM/YYYY): ", data_nasc_usuario)
        data_formatada = datetime.strptime(data_nasc_usuario, '%d/%m/%Y')
        data_formatada = data_formatada.strftime("%d/%m/%Y")

        # SETANDO A DATA DE REGISTRO DO USUÁRIO - OK
        data_registro_aluno = datetime.fromtimestamp(datetime.now().timestamp()).strftime('%d/%m/%Y')

        # SETANDO SENHA DO USUÁRIO - OK
        senha_usuario = input("DIGITE A SUA SENHA: ")
        senha_usuario = Funcoes.validarPreenchimento("DIGITE A SUA SENHA: ", senha_usuario)
        conf_senha = input("CONFIRME A SUA SENHA: ")
        conf_senha = Funcoes.validarPreenchimento("CONFIRME A SUA SENHA: ", conf_senha)
        senha_usuario = Funcoes.validarSenha(senha_usuario, conf_senha)

        # SETANDO LEVEL DO USUÁRIO - OK
        level_aluno = Level.EASY

        # SETANDO MOEDAS DO USUÁRIO - OK
        moedas_aluno = 0

        # SETANDO PRODUTOS DO USUÁRIO - OK
        produtos_aluno = []

        # SETANDO CERTIFICADOS DO USUÁRIO - OK
        certificados_aluno = []

        print("------------------------------------------")

        # ADICIONANDO O ALUNO NO DICIONÁRIO DE ALUNOS - OK
        novo_aluno = Aluno(id_usuario = id_usuario, cpf_usuario = cpf_usuario, nome_usuario = nome_usuario, email_usuario = email_usuario, cel_usuario = cel_usuario, data_nasc_aluno = data_formatada, data_registro_aluno = data_registro_aluno, senha_usuario = senha_usuario, level_aluno = level_aluno, moedas_aluno = moedas_aluno, produtos_aluno = produtos_aluno, certificados_aluno = certificados_aluno)
        dicAlunos[novo_aluno.id_usuario] = novo_aluno

        print("USUÁRIO CADASTRADO COM SUCESSO!")
        input("TECLE ENTER PARA VOLTAR AO MENU INICIAL\n")
    
    def perfilAluno(aluno_buscado):
        retornoPerfil = Funcoes.menuCabecalho()
        retornoPerfil += f"01. ID: {aluno_buscado.id_usuario}\n"
        retornoPerfil += f"02. CPF: {Funcoes.formatarCpf(aluno_buscado.cpf_usuario)}\n"
        retornoPerfil += f"03. NOME: {aluno_buscado.nome_usuario}\n"
        retornoPerfil += f"04. EMAIL: {aluno_buscado.email_usuario}\n"
        retornoPerfil += f"05. CELULAR: {Funcoes.formatarCel(aluno_buscado.cel_usuario)}\n"
        retornoPerfil += f"06. DATA DE NASCIMENTO: {aluno_buscado.data_nasc_aluno}\n"
        retornoPerfil += f"07. DATA DE REGISTRO: {aluno_buscado.data_registro_aluno}\n"
        retornoPerfil += f"08. MOEDAS: {aluno_buscado.moedas_aluno}\n"
        retornoPerfil += f"09. LEVEL: {aluno_buscado.level_aluno.value}\n"
        retornoPerfil += f"10. SENHA: {aluno_buscado.senha_usuario}\n"

        retornoPerfil += "11. PRODUTOS COMPRADOS: "
        if len(aluno_buscado.produtos_aluno) == 0:
            retornoPerfil += "NENHUM PRODUTO COMPRADO\n"
        else:
            for produto in aluno_buscado.produtos_aluno:
                retornoPerfil += f"PRODUTO: {produto.nome_produto} | QUANTIDADE: {produto.qtd_produto}\n"

        retornoPerfil += "12. CERTIFICADOS: "
        if len(aluno_buscado.certificados_aluno) == 0:
            retornoPerfil += "VOCÊ NÃO POSSUI CERTIFICADOS\n"
        else:
            for certificado in aluno_buscado.certificados_aluno:
                retornoPerfil += f"ID: {certificado.id_certificado} | DATA: {certificado.data_certificado}\n"

        retornoPerfil += "13. SAIR\n"
        retornoPerfil += Funcoes.menuRodape()
        return retornoPerfil
    
    def setarNomeUser():
        return "teste"