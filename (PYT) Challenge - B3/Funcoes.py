from datetime import datetime
from Level import Level

class Funcoes:

    # MENUS - OK
    def menuCabecalho():
        return ("==> STOCKWAVE - CHALLENGE B3 - CURSO DE IPO <==\n"
        "------------------------------------------\n")

    def menuRodape():
        return ("------------------------------------------\n"
        "DIGITE A OPÇÃO DESEJADA: \n")

    def menuInicial(): 
        return (Funcoes.menuCabecalho() + 
            "01. CADASTRE-SE\n" 
            "02. LOGIN\n"
            "03. SAIR\n" +
            Funcoes.menuRodape())

    def menuAdmin():
        return (Funcoes.menuCabecalho() +
        "01. ALUNOS\n"
        "02. PROFESSORES\n"
        "03. FUNCIONÁRIOS\n"
        "04. MÓDULOS\n"
        "05. AULAS\n"
        "06. QUESTÕES\n"
        "07. PRODUTOS\n"
        "08. EXIBIR MOVIMENTAÇÕES\n"
        "09. EXIBIR CERTIFICADOS\n"
        "10. SAIR\n" +
        Funcoes.menuRodape())

    def menuAdminAlunos():
        return (Funcoes.menuCabecalho() +
        "01. CADASTRAR ALUNO\n"
        "02. EXIBIR ALUNOS\n"
        "03. EDITAR ALUNO\n"
        "04. EXCLUIR ALUNO\n"
        "05. SAIR\n" +
        Funcoes.menuRodape())

    def menuAdminProfessores():
        return (Funcoes.menuCabecalho() +
        "01. CADASTRAR PROFESSOR\n"
        "02. EXIBIR PROFESSORES\n"
        "03. EDITAR PROFESSOR\n"
        "04. EXCLUIR PROFESSOR\n"
        "05. SAIR\n" +
        Funcoes.menuRodape())

    def menuAdminFuncionarios():
        return (Funcoes.menuCabecalho() +
        "01. CADASTRAR FUNCIONÁRIO\n"
        "02. EXIBIR FUNCIONÁRIOS\n"
        "03. EDITAR FUNCIONÁRIO\n"
        "04. EXCLUIR FUNCIONÁRIO\n"
        "05. SAIR\n" +
        Funcoes.menuRodape())

    def menuAdminModulos():
        return (Funcoes.menuCabecalho() +
        "01. CADASTRAR MÓDULO\n"
        "02. EXIBIR MÓDULOS\n"
        "03. EDITAR MÓDULO\n"
        "04. EXCLUIR MÓDULO\n"
        "05. SAIR\n" +
        Funcoes.menuRodape())

    def menuAdminAulas():
        return (Funcoes.menuCabecalho() +
        "01. CADASTRAR AULA\n"
        "02. EXIBIR AULAS\n"
        "03. EDITAR AULA\n"
        "04. EXCLUIR AULA\n"
        "05. SAIR\n" +
        Funcoes.menuRodape())

    def menuAdminQuestoes():
        return (Funcoes.menuCabecalho() +
        "01. CADASTRAR QUESTÃO\n"
        "02. EXIBIR QUESTÕES\n"
        "03. EDITAR QUESTÃO\n"
        "04. EXCLUIR QUESTÃO\n"
        "05. SAIR\n" +
        Funcoes.menuRodape())

    def menuAdminProdutos(): 
        return (Funcoes.menuCabecalho() +
        "01. CADASTRAR PRODUTO\n"
        "02. EXIBIR PRODUTOS\n"
        "03. EDITAR PRODUTO\n"
        "04. EXCLUIR PRODUTO\n"
        "05. SAIR\n" +
        Funcoes.menuRodape())

    def menuAluno():
        return (Funcoes.menuCabecalho() +
        "01. MEU PERFIL\n"
        "02. APRENDER\n"
        "03. RANKING\n"
        "04. LOJA\n"
        "05. SAIR\n" +
        Funcoes.menuRodape())

    def menuAlunoAprenderEasy():
        return (Funcoes.menuCabecalho() +
        "01. EASY\n"
        "02. SAIR\n" +
        Funcoes.menuRodape())

    def menuAlunoAprenderMedium():
        return (Funcoes.menuCabecalho() +
        "01. EASY\n"
        "02. MEDIUM\n"
        "03. SAIR\n" +
        Funcoes.menuRodape())

    def menuAlunoAprenderHard():
        return (Funcoes.menuCabecalho() +
        "01. EASY\n"
        "02. MEDIUM\n"
        "03. HARD\n"
        "04. SAIR\n" +
        Funcoes.menuRodape())

    def menuRanking():
        return (Funcoes.menuCabecalho() +
        "01. ALUNO 01 - MOEDAS 09\n"
        "02. ALUNO 02 - MOEDAS 06\n"
        "03. ALUNO 03 - MOEDAS 02\n" +
        Funcoes.menuRodape())

    def menuLoja():
        return (Funcoes.menuCabecalho() +
        "01. IPO NUBANK - VALOR: 3 MOEDAS - QUANTIDADE: 10\n"
        "02. IPO VALE - VALOR: 100 MOEDAS - QUANTIDADE: 5\n"
        "03. IPO PETROBRAS - VALOR: 1 MOEDAS - QUANTIDADE: 0\n"
        "04. SAIR\n" +
        Funcoes.menuRodape())

    # CONFIRMAR - OK
    def confirmarAcao(acao):
        return ("TEM CERTEZA QUE DESEJA " + acao + "?\n"
        "01. SIM\n"
        "02. NÃO\n"
        "------------------------------------------\n"
        "DIGITE A OPÇÃO DESEJADA: \n")
    
    # VALIDAR E VERIFICAR - OK
    def validarCPF(cpf_usuario):
        if (cpf_usuario == "00000000000" or cpf_usuario == "11111111111" or cpf_usuario == "22222222222" or cpf_usuario == "33333333333" or cpf_usuario == "44444444444" or cpf_usuario == "55555555555" or cpf_usuario == "66666666666" or cpf_usuario == "77777777777" or cpf_usuario == "88888888888" or cpf_usuario == "99999999999" or (len(cpf_usuario) != 11)):
            return False

        dig10, dig11 = '', ''
        sm, r, peso = 0, 0, 0
        for i in range(9):
            num = int(cpf_usuario[i])
            sm += num * (10 - i)
        r = 11 - sm % 11
        if (r == 10 or r == 11):
            dig10 = '0'
        else:
            dig10 = str(r)

        sm = 0
        peso = 11
        for i in range(10):
            num = int(cpf_usuario[i])
            sm += num * peso
            peso -= 1
        r = 11 - sm % 11
        if (r == 10 or r == 11):
            dig11 = '0'
        else:
            dig11 = str(r)

        if (dig10 == cpf_usuario[9] and dig11 == cpf_usuario[10]):
            return True
        else:
            return False
    
    def validarCel(cel_usuario):
        while (len(cel_usuario) != 11):
            print("CELULAR INVÁLIDO OU JÁ CADASTRADO.")
            cel_usuario = input("DIGITE O SEU CELULAR (SOMENTE NÚMEROS, COM DDD, EXEMPLO: 11983050165): ")
        
        return cel_usuario

    def validarOpcao(opcao, opcao_min, opcao_max, menu):
        while (opcao < opcao_min or opcao > opcao_max or opcao == None):
            input("OPÇÃO INVÁLIDA! TECLE ENTER PARA VOLTAR AO MENU")
            opcao = int(input(menu))
        
        return opcao
    
    def validarPreenchimento(stringRepeticao, campopreenchido) -> str:
        while (len(campopreenchido) == 0) or (campopreenchido == "") or (campopreenchido == None) or (campopreenchido == "\r"):
            print("O PREENCHIMENTO DO CAMPO É OBRIGATÓRIO.")
            campopreenchido = input(stringRepeticao)
            
        return campopreenchido.upper()

    def validarSenha(senha_usuario, conf_senha):
        while (senha_usuario != conf_senha):
            input("SENHAS NÃO CONFEREM. TECLE ENTER PARA CADASTRAR NOVA SENHA")
            senha_usuario = input("DIGITE A SUA SENHA: ")
            conf_senha = input("CONFIRME A SUA SENHA: ")
        return senha_usuario

    def validarUsuarioBuscado(usuario_buscado, lista):
        while (usuario_buscado == None):
            input("ID INVÁLIDO. TECLE ENTER PARA VOLTAR AO MENU")
            Funcoes.exibirUsuariosAdmin(lista)
            id_buscado = int(input("DIGITE O ID DO USUÁRIO NOVAMENTE: \n"))
            usuario_buscado = Funcoes.buscarPorIdDic(id_buscado, lista)
        
        return usuario_buscado

    def validarModuloBuscado(modulo_buscado, listaModulos):
        while (modulo_buscado == None):
            input("ID INVÁLIDO. TECLE ENTER PARA VOLTAR AO MENU")
            Funcoes.exibirModulosAdmin(listaModulos)
            modulo_buscado = int(input("DIGITE O ID DO MÓDULO NOVAMENTE: \n"))
        
        return modulo_buscado

    def validarAulaBuscada(aula_buscada, listaAulas):
        while (aula_buscada == None):
            input("ID INVÁLIDO. TECLE ENTER PARA VOLTAR AO MENU")
            Funcoes.exibirAulasAdmin(listaAulas)
            aula_buscada = int(input("DIGITE O ID DA AULA NOVAMENTE: \n"))
        
        return aula_buscada

    def validarQuestaoBuscada(questao_buscada, listaQuestoes):
        while (questao_buscada == None):
            input("ID INVÁLIDO. TECLE ENTER PARA VOLTAR AO MENU")
            Funcoes.exibirDadosQuestoes(listaQuestoes)
            questao_buscada = int(input("DIGITE O ID DA QUESTÃO NOVAMENTE: \n"))
        
        return questao_buscada

    def verificarCPF(cpf_usuario, cpfs_cadastrados):
        while (cpf_usuario in cpfs_cadastrados or Funcoes.validarCPF(cpf_usuario) == False):
            print("CPF INVÁLIDO OU JÁ CADASTRADO.")
            cpf_usuario = input("DIGITE O SEU CPF (APENAS NÚMEROS, EXEMPLO: 43102154278): ")
        
        return cpf_usuario

    def verificarEmail(email_usuario, emails_cadastrados):
        while (email_usuario in emails_cadastrados or email_usuario == ""):
            print("EMAIL INVÁLIDO OU JÁ CADASTRADO.")
            email_usuario = input("DIGITE O SEU EMAIL: ").upper()
        
        return email_usuario

    def verificarCel(cel_usuario, cel_cadastrados):
        while (cel_usuario in cel_cadastrados or cel_usuario == "" or len(cel_usuario) != 11):
            print("CELULAR INVÁLIDO OU JÁ CADASTRADO.")
            cel_usuario = input("DIGITE O SEU CELULAR (SOMENTE NÚMEROS, COM DDD, EXEMPLO: 11983050165): ")
        
        return cel_usuario

    # FORMATAR - OK
    def formatarCpf(cpf_usuario):
        cpf_usuario_formatado = '{}.{}.{}-{}'.format(cpf_usuario[:3], cpf_usuario[3:6], cpf_usuario[6:9], cpf_usuario[9:])
        return cpf_usuario_formatado

    def formatarCel(cel_usuario):
        cel_usuario_formatado = '({}) {}-{}'.format(cel_usuario[:2], cel_usuario[2:7], cel_usuario[7:11])
        return cel_usuario_formatado

    # BUSCAR - OK
    def buscarPorIdUsuario(id_buscado, lista):
        objeto_buscado = lista.get(id_buscado)
        if objeto_buscado is None:
            return None
        return objeto_buscado
    
    def buscarPorIdModulo(id_buscado, lista):
        for modulo in lista:
            if modulo.id_modulo == id_buscado:
                return modulo
        return None

    def buscarPorIdAula(id_buscado, lista):
        for aula in lista:
            if aula.id_aula == id_buscado:
                return aula
        return None

    def buscarPorIdQuestao(id_buscado, lista):
        for questao in lista:
            if questao.id_questao == id_buscado:
                return questao
        return None

    # CADASTRAR - OK
    def cadastrarTestes(cpfs_cadastrados, emails_cadastrados, cel_cadastrados, Aluno, dicAlunos, Professor, dicProfessores, Funcionario, dicFuncionarios):
        # CADASTRANDO ALUNOS TESTE - OK
        alunokaue = Aluno(id_usuario = 1, cpf_usuario = "43101167876", nome_usuario = "KAUE CAPONERO FIGUEIREDO", email_usuario = "K", cel_usuario = "11983090659", data_nasc_aluno = "22/06/1993", data_registro_aluno = "10/03/2023", senha_usuario = "k", moedas_aluno = 100, level_aluno = Level.HARD, produtos_aluno = [], certificados_aluno = [])
        aluno2 = Aluno(id_usuario = 2, cpf_usuario = "25328392019", nome_usuario = "ALUNO TESTE 2", email_usuario = "EMAIL@TESTE2.COM.BR", cel_usuario = "11982643445", data_nasc_aluno = "12/07/2000", data_registro_aluno = "11/03/2023", senha_usuario = "1", moedas_aluno = 0, level_aluno = Level.EASY, produtos_aluno = [], certificados_aluno = [])
        cpfs_cadastrados.add(alunokaue.cpf_usuario)
        cpfs_cadastrados.add(aluno2.cpf_usuario)
        emails_cadastrados.add(alunokaue.email_usuario)
        emails_cadastrados.add(aluno2.email_usuario)
        cel_cadastrados.add(alunokaue.cel_usuario)
        cel_cadastrados.add(aluno2.cel_usuario)
        dicAlunos[alunokaue.id_usuario] = alunokaue
        dicAlunos[aluno2.id_usuario] = aluno2

        # CADASTRANDO PROFESSORES TESTE - OK
        profkaue = Professor(id_usuario = 3, cpf_usuario = "43101167876", nome_usuario = "KAUE CAPONERO FIGUEIREDO", email_usuario = "K", cel_usuario = "11983090659")
        prof2 = Professor(id_usuario = 4, cpf_usuario = "25328392019", nome_usuario = "PROFESSOR TESTE 2", email_usuario = "EMAIL@TESTE2.COM.BR", cel_usuario = "11982643445")
        dicProfessores[profkaue.id_usuario] = profkaue
        dicProfessores[prof2.id_usuario] = prof2

        # CADASTRANDO FUNCIONÁRIOS TESTE - OK
        funcAdmin = Funcionario(id_usuario = 0, cpf_usuario = "00000000000", nome_usuario = "ADMIN", email_usuario = "ADMIN", cel_usuario = "00000000000", senha_usuario = "admin", cargo_funcionario = "ADMIN")
        dicFuncionarios[funcAdmin.id_usuario] = funcAdmin
    
    # EDITAR - OK
    def editarNegativo():
        return("NÃO É POSSÍVEL EDITAR ESTA OPÇÃO.\n"
            "TECLE ENTER PARA VOLTAR AO MENU")

    def editarNome(usuario_buscado):
        novo_nome = input("DIGITE O NOVO NOME: ").upper()
        novo_nome = Funcoes.validarPreenchimento("DIGITE O NOVO NOME: ", novo_nome)
        usuario_buscado.nome_usuario = novo_nome
        print("NOME DO USUÁRIO EDITADO COM SUCESSO!")

    def editarEmail(usuario_buscado, emails_cadastrados, Aluno):
        novo_email = input("DIGITE O NOVO EMAIL: ").upper()
        novo_email = Funcoes.validarPreenchimento("DIGITE O NOVO EMAIL: ", novo_email)
        novo_email = Funcoes.verificarEmail(novo_email, emails_cadastrados)
        if isinstance(usuario_buscado, Aluno):
            emails_cadastrados.remove(usuario_buscado.email_usuario)
            emails_cadastrados.add(novo_email)
        usuario_buscado.email_usuario = novo_email
        print("EMAIL DO USUÁRIO EDITADO COM SUCESSO!")

    def editarCel(usuario_buscado, cel_cadastrados, Aluno):
        novo_cel = input("DIGITE O NOVO CELULAR DO USUÁRIO (SOMENTE NÚMEROS, COM DDD, EXEMPLO: 11983050165): ").upper()
        novo_cel = Funcoes.validarPreenchimento("DIGITE O NOVO CELULAR DO USUÁRIO (SOMENTE NÚMEROS, COM DDD, EXEMPLO: 11983050165): ", novo_cel)
        novo_cel = Funcoes.verificarCel(novo_cel, cel_cadastrados)
        if isinstance(usuario_buscado, Aluno):
            cel_cadastrados.remove(usuario_buscado.cel_usuario)
            cel_cadastrados.add(novo_cel)
        usuario_buscado.cel_usuario = novo_cel
        print("CELULAR DO USUÁRIO EDITADO COM SUCESSO!")

    def editarDataNasc(usuario_buscado):
        nova_data_nasc = input("DIGITE A NOVA DATA DE NASCIMENTO DO USUÁRIO (DD/MM/YYYY, EXEMPLO: 22/06/1993): ").upper()
        nova_data_nasc = Funcoes.validarPreenchimento("DIGITE A NOVA DATA DE NASCIMENTO DO USUÁRIO (DD/MM/YYYY, EXEMPLO: 22/06/1993): ", nova_data_nasc)
        data_formatada = datetime.strptime(nova_data_nasc, '%d/%m/%Y')
        data_formatada = data_formatada.strftime("%d/%m/%Y")
        usuario_buscado.data_nasc_aluno = data_formatada
        print("DATA DE NASCIMENTO DO USUÁRIO EDITADO COM SUCESSO!")

    def editarMoedas(usuario_buscado):
        moedas_adicionar = int(input(f"QUANTAS MOEDAS DESEJA ADICIONAR/SUBTRAIR DO USUÁRIO {usuario_buscado.nome_usuario}? "))
        moedas_adicionar = Funcoes.validarPreenchimento("QUANTAS MOEDAS DESEJA ADICIONAR/SUBTRAIR DO USUÁRIO " + usuario_buscado.nome_usuario + "?", moedas_adicionar)
        novas_moedas = moedas_adicionar + usuario_buscado.moedas_aluno
        usuario_buscado.moedas_aluno = novas_moedas
        print("MOEDAS DO USUÁRIO ATUALIZADAS COM SUCESSO!")

    def editarLevel(usuario_buscado):
        novo_level = ("QUAL O NOVO LEVEL DO USUÁRIO {usuario_buscado['nome_usuario']}?" + "\n" +
                        "01. EASY" + "\n" +
                        "02. MEDIUM" + "\n" + 
                        "03. HARD" + "\n" + 
                        Funcoes.menuRodape())
        
        opcao = int(input(novo_level))

        opcao = int(Funcoes.validarOpcao(opcao, 1, 3, novo_level))

        if (opcao == 1):
            usuario_buscado.level_aluno = Level.EASY

        elif (opcao == 2):
            usuario_buscado.level_aluno = Level.MEDIUM
        
        elif (opcao == 3):
            usuario_buscado.level_aluno = Level.HARD

        print("LEVEL DO USUÁRIO ATUALIZADO COM SUCESSO!")

    def editarSenha(usuario_buscado):
        nova_senha_usuario = input("DIGITE A NOVA SENHA: ")
        nova_senha_usuario = Funcoes.validarPreenchimento("DIGITE A NOVA SENHA: ", nova_senha_usuario)
        conf_senha = input("CONFIRME A NOVA SENHA: ")
        conf_senha = Funcoes.validarPreenchimento("CONFIRME A NOVA SENHA: ", conf_senha)
        nova_senha_usuario = Funcoes.validarSenha(nova_senha_usuario, conf_senha)
        usuario_buscado.senha_usuario = nova_senha_usuario
        print("SENHA DO USUÁRIO EDITADA COM SUCESSO!")

    def editarCargo(usuario_buscado):
        novo_cargo = input("DIGITE O NOVO CARGO: ").upper()
        novo_cargo = Funcoes.validarPreenchimento("DIGITE O NOVO CARGO: ", novo_cargo)
        usuario_buscado.cargo_funcionario = novo_cargo
        print("CARGO DO FUNCIONÁRIO EDITADO COM SUCESSO!")

    # EXCLUIR - OK
    def excluirUsuario(lista, listaExcluidos):
        Funcoes.exibirUsuariosAdmin(lista)
        id_buscado = int(input("DIGITE O ID DO USUÁRIO QUE DESEJA EXCLUIR: \n"))
        usuario_buscado = Funcoes.buscarPorIdDic(id_buscado, lista)
        usuario_buscado = Funcoes.validarUsuarioBuscado(usuario_buscado, lista)
        opcao = int(input(Funcoes.confirmarAcao(f"EXCLUIR O USUÁRIO {usuario_buscado.nome_usuario}")))
        opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EXCLUIR O USUÁRIO {usuario_buscado.nome_usuario}")))
        
        if (opcao == 1):
            del lista[id_buscado]
            listaExcluidos.append(usuario_buscado)
            print("USUÁRIO EXCLUÍDO COM SUCESSO!")
            input("TECLE ENTER PARA VOLTAR AO MENU.")
        
        elif (opcao == 2):
            input("TECLE ENTER PARA VOLTAR AO MENU.")

    def excluirModulo(listaModulos, listaModulosExcluidos):
        Funcoes.exibirModulosAdmin(listaModulos)
        id_buscado = int(input("DIGITE O ID DO MÓDULO QUE DESEJA EXCLUIR: \n"))
        modulo_buscado = Funcoes.buscarPorIdModulo(id_buscado, listaModulos)
        modulo_buscado = Funcoes.validarModuloBuscado(modulo_buscado, listaModulos)
        opcao = int(input(Funcoes.confirmarAcao(f"EXCLUIR O MÓDULO")))
        opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EXCLUIR O MÓDULO")))
        
        if (opcao == 1):
            for i in range(len(listaModulos)):
                if listaModulos[i].id_aula == id_buscado:
                    del listaModulos[i]
                    listaModulosExcluidos.append(modulo_buscado)
                    print("MÓDULO EXCLUÍDO COM SUCESSO!")
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
        
        elif (opcao == 2):
            input("TECLE ENTER PARA VOLTAR AO MENU.")
    
    def excluirAula(listaAulas, listaAulasExcluidas):
        Funcoes.exibirAulasAdmin(listaAulas)
        id_buscado = int(input("DIGITE O ID DA AULA QUE DESEJA EXCLUIR: \n"))
        aula_buscada = Funcoes.buscarPorIdAula(id_buscado, listaAulas)
        aula_buscada = Funcoes.validarAulaBuscada(aula_buscada, listaAulas)
        opcao = int(input(Funcoes.confirmarAcao(f"EXCLUIR A AULA")))
        opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EXCLUIR A AULA")))
        
        if (opcao == 1):
            for i in range(len(listaAulas)):
                if listaAulas[i].id_aula == id_buscado:
                    del listaAulas[i]
                    listaAulasExcluidas.append(aula_buscada)
                    print("AULA EXCLUÍDA COM SUCESSO!")
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
        
        elif (opcao == 2):
            input("TECLE ENTER PARA VOLTAR AO MENU.")
    
    def excluirQuestao(listaQuestoes, listaQuestoesExcluidas):
        Funcoes.exibirDadosQuestoes(listaQuestoes)
        id_buscado = int(input("DIGITE O ID DA QUESTÃO QUE DESEJA EXCLUIR: \n"))
        questao_buscada = Funcoes.buscarPorIdQuestao(id_buscado, listaQuestoes)
        questao_buscada = Funcoes.validarQuestaoBuscada(questao_buscada, listaQuestoes)
        opcao = int(input(Funcoes.confirmarAcao(f"EXCLUIR A QUESTÃO")))
        opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EXCLUIR A QUESTÃO")))
        
        if (opcao == 1):
            for i in range(len(listaQuestoes)):
                if listaQuestoes[i].id_questao == id_buscado:
                    del listaQuestoes[i]
                    listaQuestoesExcluidas.append(questao_buscada)
                    print("QUESTÃO EXCLUÍDA COM SUCESSO!")
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
        
        elif (opcao == 2):
            input("TECLE ENTER PARA VOLTAR AO MENU.")

    # EXIBIR - OK
    def exibirUsuariosAdmin(lista):
        Funcoes.menuCabecalho()

        if len(lista) == 0:
            print("NÃO EXISTEM ALUNOS CADASTRADOS.")
        else:
            for id_usuario, usuario in lista.items():
                print(f"ID: {usuario.id_usuario} | CPF: {Funcoes.formatarCpf(usuario.cpf_usuario)} | NOME: {usuario.nome_usuario}")
                print("------------------------------------------")

    def exibirModulosAdmin(listaModulos):

        Funcoes.menuCabecalho

        if len(listaModulos) == 0:
            print("NÃO EXISTEM MÓDULOS CADASTRADOS.")
        else:
            for i in range(len(listaModulos)):
                print(f"ID: {listaModulos[i]['id_modulo']} | NOME DO MÓDULO: {listaModulos[i]['nome_modulo']}") 
                print(f"------------------------------------------")

    def exibirAulasAdmin(listaAulas):

        Funcoes.menuCabecalho

        if len(listaAulas) == 0:
            print("NÃO EXISTEM AULAS CADASTRADAS.")
        else:
            for aula in listaAulas:
                print(f"ID: {aula.id_aula} | NOME DA AULA: {aula.nome_aula}") 
                print(f"------------------------------------------")
    
    def exibirDadosQuestoes(listaQuestoes):
        
        Funcoes.menuCabecalho

        if len(listaQuestoes) == 0:
            print("NÃO EXISTEM QUESTÕES CADASTRADAS.")
        else:
            for questao in listaQuestoes:
                print(f"ID: {questao.id_questao} | PERGUNTA DA QUESTÃO: {questao.pergunta}") 
                print(f"------------------------------------------")


