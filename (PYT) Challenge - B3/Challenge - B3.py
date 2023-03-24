# IMPORTANDO CLASSES - OK
from Aluno import Aluno
from Aula import Aula
from Certificado import Certificado
from Funcionario import Funcionario
from Funcoes import Funcoes
from Level import Level
from Login import Login
from Modulo import Modulo
from Movimentacao import Movimentacao
from Produto import Produto
from Professor import Professor
from Questao import Questao
from Resposta import Resposta
from Usuario import Usuario
from Apis import conselhoApi
from Apis import tradutorApi

# CRIANDO LISTAS, DICIONÁRIOS, SETS E TUPLAS - OK
dicAlunos = {}
dicProfessores = {}
dicFuncionarios = {}
dicAlunosExcluidos = []
dicProfessoresExcluidos = []
dicFuncionariosExcluidos = []
listaModulos = []
listaModulosExcluidos = []
listaAulas = []
listaAulasExcluidas = []
listaQuestoes = []
listaQuestoesExcluidas = []
listaProdutos = []
listaMovimentacoes = []
listaCertificados = []
cpfs_cadastrados = set()
emails_cadastrados = set()
cel_cadastrados = set()

# DECLARANDO VARIÁVEIS INICIAIS - OK
iniciar = 1
id_user = 5
id_modulo = 1
id_aula = 1
id_questao = 1

# CRIANDO USUÁRIOS TESTE - OK
Funcoes.cadastrarTestes(cpfs_cadastrados, emails_cadastrados, cel_cadastrados, Aluno, dicAlunos, Professor, dicProfessores, Funcionario, dicFuncionarios)

while (iniciar == 1):
    # MENU INICIAL - OK
    opcao = int(input(Funcoes.menuInicial()))
    opcao = int(Funcoes.validarOpcao(opcao,1,3, Funcoes.menuInicial()))

    if (opcao == 1):
        # (USER) CADASTRAR ALUNO - OK
        Aluno.cadastrarAluno(cpfs_cadastrados, emails_cadastrados, cel_cadastrados, dicAlunos, id_user)
        id_user = id_user + 1

    elif (opcao == 2):
        # (USER) EFETUAR LOGIN - OK
        print("------------------------------------------")
        email_login = input("EMAIL: ").upper()
        senha_login = input("SENHA: ")

        for id_funcionario, funcionario in dicFuncionarios.items():
            if funcionario.email_usuario.upper() == email_login and funcionario.senha_usuario == senha_login:
                admin = 1
                print("------------------------------------------")
                print(f"BEM VINDO, {funcionario.nome_usuario}. DICA DO DIA: {tradutorApi(conselhoApi())}")

                while (admin == 1):
                    # EXIBIR MENU ADMIN - OK
                    opcao = int(input(Funcoes.menuAdmin()))
                    opcao = Funcoes.validarOpcao(opcao, 1, 10, Funcoes.menuAdmin())
                    
                    if (opcao == 1):
                        # (ADMIN) ALUNOS - OK
                        menuAdminAlunos = 1
                    
                        while (menuAdminAlunos == 1):
                            opcao = int(input(Funcoes.menuAdminAlunos()))
                            opcao = Funcoes.validarOpcao(opcao, 1, 5, Funcoes.menuAdminAlunos())

                            if (opcao == 1):
                                # (ADMIN) CADASTRAR ALUNO - OK
                                Aluno.cadastrarAluno(cpfs_cadastrados, emails_cadastrados, cel_cadastrados, dicAlunos, id_user)
                                id_user = id_user + 1

                            elif (opcao == 2):
                                # (ADMIN) EXIBIR ALUNOS - OK
                                Funcoes.exibirUsuariosAdmin(dicAlunos)
                                input("TECLE ENTER PARA VOLTAR AO MENU\n")
                            
                            elif (opcao == 3):
                                # (ADMIN) EDITAR ALUNOS - OK
                                perfilAluno = 1
                                Funcoes.exibirUsuariosAdmin(dicAlunos)
                                id_buscado = int(input("DIGITE O ID DO ALUNO QUE DESEJA EDITAR: \n"))
                                aluno_buscado = Funcoes.buscarPorIdUsuario(id_buscado, dicAlunos)
                                aluno_buscado = Funcoes.validarUsuarioBuscado(aluno_buscado, dicAlunos)

                                while (perfilAluno == 1):
                                    opcao = int(input(Aluno.perfilAluno(aluno_buscado)))
                                    opcao = Funcoes.validarOpcao(opcao, 1, 13, Aluno.perfilAluno(aluno_buscado))

                                    if (opcao == 1):
                                        # (ADMIN) EDITAR ID DO ALUNO  - OK
                                        input(Funcoes.editarNegativo())

                                    elif (opcao == 2):
                                        # (ADMIN) EDITAR O CPF DO ALUNO - OK
                                        input(Funcoes.editarNegativo())
                                    
                                    elif (opcao == 3):
                                        # (ADMIN) EDITAR O NOME DO ALUNO - OK
                                        opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O NOME DO ALUNO {aluno_buscado.nome_usuario}")))
                                        opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O NOME DO ALUNO {aluno_buscado.nome_usuario}")))
                                        
                                        if (opcao == 1):
                                            # (ADMIN) EDITAR O NOME DO ALUNO - SIM - OK
                                            Funcoes.editarNome(aluno_buscado)
                                            input("TECLE ENTER PARA VOLTAR AO MENU.")
                                        
                                        elif (opcao == 2):
                                            # (ADMIN) EDITAR O NOME DO ALUNO - NÃO - OK
                                            input("TECLE ENTER PARA VOLTAR AO MENU.")
                                    
                                    elif (opcao == 4):
                                        # (ADMIN) EDITAR O EMAIL DO ALUNO - OK
                                        opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O EMAIL DO ALUNO {aluno_buscado.nome_usuario}")))
                                        opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O EMAIL DO ALUNO {aluno_buscado.nome_usuario}")))
                                        
                                        if (opcao == 1):
                                            # (ADMIN) EDITAR O EMAIL DO ALUNO - SIM - OK
                                            Funcoes.editarEmail(aluno_buscado, emails_cadastrados, Aluno)
                                            input("TECLE ENTER PARA VOLTAR AO MENU.")
                                        
                                        elif (opcao == 2):
                                            # (ADMIN) EDITAR O EMAIL DO ALUNO - NÃO - OK
                                            input("TECLE ENTER PARA VOLTAR AO MENU.")
                                    
                                    elif (opcao == 5):
                                        # (ADMIN) EDITAR O CELULAR DO ALUNO - OK
                                        opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O CELULAR DO ALUNO {aluno_buscado.nome_usuario}")))
                                        opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O CELULAR DO ALUNO {aluno_buscado.nome_usuario}")))
                                        
                                        if (opcao == 1):
                                            # (ADMIN) EDITAR O CELULAR DO ALUNO - SIM - OK
                                            Funcoes.editarCel(aluno_buscado, cel_cadastrados, Aluno)
                                            input("TECLE ENTER PARA VOLTAR AO MENU.")
                                        
                                        elif (opcao == 2):
                                            # (ADMIN) EDITAR O CELULAR DO ALUNO - NÃO - OK
                                            input("TECLE ENTER PARA VOLTAR AO MENU.")

                                    elif (opcao == 6):
                                        # (ADMIN) EDITAR A DATA DE NASCIMENTO DO ALUNO - OK
                                        opcao = int(input(Funcoes.confirmarAcao(f"EDITAR A DATA DE NASCIMENTO DO ALUNO {aluno_buscado.nome_usuario}")))
                                        opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR A DATA DE NASCIMENTO DO ALUNO {aluno_buscado.nome_usuario}")))
                                        
                                        if (opcao == 1):
                                            # (ADMIN) EDITAR A DATA DE NASCIMENTO DO ALUNO - SIM - OK
                                            Funcoes.editarDataNasc(aluno_buscado)
                                            input("TECLE ENTER PARA VOLTAR AO MENU.")
                                        
                                        elif (opcao == 2):
                                            # (ADMIN) EDITAR O CELULAR DO ALUNO - NÃO - OK
                                            input("TECLE ENTER PARA VOLTAR AO MENU.")
                                    
                                    elif (opcao == 7):
                                        # (ADMIN) EDITAR A DATA DE REGISTRO DO ALUNO - OK
                                        input(Funcoes.editarNegativo())

                                    elif (opcao == 8):
                                        # (ADMIN) EDITAR AS MOEDAS DO ALUNO - OK
                                        opcao = int(input(Funcoes.confirmarAcao(f"EDITAR AS MOEDAS DO ALUNO {aluno_buscado.nome_usuario}")))
                                        opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR AS MOEDAS DO ALUNO {aluno_buscado.nome_usuario}")))

                                        if (opcao == 1):
                                            # (ADMIN) EDITAR AS MOEDAS DO ALUNO - SIM - OK
                                            Funcoes.editarMoedas(aluno_buscado)
                                            input("TECLE ENTER PARA VOLTAR AO MENU.")
                                        
                                        elif (opcao == 2):
                                            # (ADMIN) EDITAR AS MOEDAS DO ALUNO - NÃO - OK
                                            input("TECLE ENTER PARA VOLTAR AO MENU.")

                                    elif (opcao == 9):
                                        # (ADMIN) EDITAR O LEVEL DO ALUNO - OK
                                        opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O LEVEL DO ALUNO {aluno_buscado.nome_usuario}")))
                                        opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O LEVEL DO ALUNO {aluno_buscado.nome_usuario}")))

                                        if (opcao == 1):
                                            # (ADMIN) EDITAR O LEVEL DO ALUNO - SIM - OK
                                            Funcoes.editarLevel(aluno_buscado)
                                            input("TECLE ENTER PARA VOLTAR AO MENU.")
                                        
                                        elif (opcao == 2):
                                            # (ADMIN) EDITAR O LEVEL DO ALUNO - NÃO - OK
                                            input("TECLE ENTER PARA VOLTAR AO MENU.")

                                    elif (opcao == 10):
                                        # (ADMIN) EDITAR A SENHA DO ALUNO - OK
                                        opcao = int(input(Funcoes.confirmarAcao(f"EDITAR A SENHA DO ALUNO {aluno_buscado.nome_usuario}")))
                                        opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR A SENHA DO ALUNO {aluno_buscado.nome_usuario}")))

                                        if (opcao == 1):
                                            # (ADMIN) EDITAR A SENHA DO ALUNO - SIM - OK
                                            Funcoes.editarSenha(aluno_buscado)
                                            input("TECLE ENTER PARA VOLTAR AO MENU.")
                                        
                                        elif (opcao == 2):
                                            # (ADMIN) EDITAR A SENHA DO ALUNO - NÃO - OK
                                            input("TECLE ENTER PARA VOLTAR AO MENU.")
                                    
                                    elif (opcao == 11):
                                        # (ADMIN) EDITAR PRODUTOS DO ALUNO  - OK
                                        input(Funcoes.editarNegativo())

                                    elif (opcao == 12):
                                        # (ADMIN) EDITAR CERTIFICADOS DO ALUNO  - OK
                                        input(Funcoes.editarNegativo())
                                    
                                    elif (opcao == 13):
                                        # (ADMIN) SAIR DO MENU PERFIL ALUNO - OK
                                        perfilAluno = 0
                            
                            elif (opcao == 4):
                                # (ADMIN) EXCLUIR ALUNO - OK
                                Funcoes.excluirUsuario(dicAlunos, dicAlunosExcluidos)
                            
                            elif (opcao == 5):
                                # (ADMIN) SAIR DO MENU DE ALUNOS - OK
                                menuAdminAlunos = 0

                    if (opcao == 2):
                        # (ADMIN) PROFESSORES - OK
                        menuAdminProfessores = 1

                        while (menuAdminProfessores == 1):
                            opcao = int(input(Funcoes.menuAdminProfessores()))
                            opcao = Funcoes.validarOpcao(opcao, 1, 5, Funcoes.menuAdminProfessores())

                            if (opcao == 1):
                                # (ADMIN) CADASTRAR PROFESSOR - OK
                                Professor.cadastrarProfessor(dicProfessores, id_user)
                                id_user = id_user + 1

                            elif (opcao == 2):
                                # (ADMIN) EXIBIR PROFESSORES - OK
                                Funcoes.exibirUsuariosAdmin(dicProfessores)
                                input("TECLE ENTER PARA VOLTAR AO MENU\n")
                            
                            elif (opcao == 3):
                                # (ADMIN) EDITAR PROFESSORES - OK
                                perfilProfessor = 1
                                Funcoes.exibirUsuariosAdmin(dicProfessores)
                                id_buscado = int(input("DIGITE O ID DO PROFESSOR QUE DESEJA EDITAR: \n"))
                                professor_buscado = Funcoes.buscarPorIdUsuario(id_buscado, dicProfessores)
                                professor_buscado = Funcoes.validarUsuarioBuscado(professor_buscado, dicProfessores)

                                while (perfilProfessor == 1):
                                    opcao = int(input(Professor.perfilProfessor(professor_buscado)))
                                    opcao = Funcoes.validarOpcao(opcao, 1, 6, Professor.perfilProfessor(professor_buscado))

                                    if (opcao == 1):
                                        # (ADMIN) EDITAR ID DO PROFESSOR  - OK
                                        input(Funcoes.editarNegativo())

                                    elif (opcao == 2):
                                        # (ADMIN) EDITAR O CPF DO PROFESSOR - OK
                                        input(Funcoes.editarNegativo())
                                    
                                    elif (opcao == 3):
                                        # (ADMIN) EDITAR O NOME DO PROFESSOR - OK
                                        opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O NOME DO PROFESSOR {professor_buscado.nome_usuario}")))
                                        opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O NOME DO PROFESSOR {professor_buscado.nome_usuario}")))
                                        
                                        if (opcao == 1):
                                            # (ADMIN) EDITAR O NOME DO PROFESSOR - SIM - OK
                                            Funcoes.editarNome(professor_buscado)
                                            input("TECLE ENTER PARA VOLTAR AO MENU.")
                                        
                                        elif (opcao == 2):
                                            # (ADMIN) EDITAR O NOME DO PROFESSOR - NÃO - OK
                                            input("TECLE ENTER PARA VOLTAR AO MENU.")
                                    
                                    elif (opcao == 4):
                                        # (ADMIN) EDITAR O EMAIL DO PROFESSOR - OK
                                        opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O EMAIL DO PROFESSOR {professor_buscado.nome_usuario}")))
                                        opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O EMAIL DO PROFESSOR {professor_buscado.nome_usuario}")))
                                        
                                        if (opcao == 1):
                                            # (ADMIN) EDITAR O EMAIL DO PROFESSOR - SIM - OK
                                            Funcoes.editarEmail(professor_buscado, emails_cadastrados, Aluno)
                                            input("TECLE ENTER PARA VOLTAR AO MENU.")
                                        
                                        elif (opcao == 2):
                                            # (ADMIN) EDITAR O EMAIL DO PROFESSOR - NÃO - OK
                                            input("TECLE ENTER PARA VOLTAR AO MENU.")
                                    
                                    elif (opcao == 5):
                                        # (ADMIN) EDITAR O CELULAR DO PROFESSOR - OK
                                        opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O CELULAR DO PROFESSOR {professor_buscado.nome_usuario}")))
                                        opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O CELULAR DO PROFESSOR {professor_buscado.nome_usuario}")))
                                        
                                        if (opcao == 1):
                                            # (ADMIN) EDITAR O CELULAR DO PROFESSOR - SIM - OK
                                            Funcoes.editarCel(professor_buscado, cel_cadastrados, Aluno)
                                            input("TECLE ENTER PARA VOLTAR AO MENU.")
                                        
                                        elif (opcao == 2):
                                            # (ADMIN) EDITAR O CELULAR DO PROFESSOR - NÃO - OK
                                            input("TECLE ENTER PARA VOLTAR AO MENU.")

                                    elif (opcao == 6):
                                        # (ADMIN) SAIR DO MENU PERFIL PROFESSOR - OK
                                        perfilProfessor = 0
                            
                            elif (opcao == 4):
                                # (ADMIN) EXCLUIR PROFESSOR - OK
                                Funcoes.excluirUsuario(dicProfessores, dicProfessoresExcluidos)
                            
                            elif (opcao == 5):
                                # (ADMIN) SAIR DO MENU DE PROFESSORES - OK
                                menuAdminProfessores = 0

                    if (opcao == 3):
                        # (ADMIN) FUNCIONÁRIOS - OK
                        menuAdminFuncionarios = 1

                        while (menuAdminFuncionarios == 1):
                            opcao = int(input(Funcoes.menuAdminFuncionarios()))
                            opcao = Funcoes.validarOpcao(opcao, 1, 5, Funcoes.menuAdminFuncionarios())

                            if (opcao == 1):
                                # (ADMIN) CADASTRAR FUNCIONÁRIO - OK
                                Funcionario.cadastrarFuncionario(dicFuncionarios, id_user)
                                id_user = id_user + 1

                            elif (opcao == 2):
                                # (ADMIN) EXIBIR FUNCIONÁRIOS - OK
                                Funcoes.exibirUsuariosAdmin(dicFuncionarios)
                                input("TECLE ENTER PARA VOLTAR AO MENU\n")
                            
                            elif (opcao == 3):
                                # (ADMIN) EDITAR FUNCIONÁRIOS - OK
                                perfilFuncionario = 1
                                Funcoes.exibirUsuariosAdmin(dicFuncionarios)
                                id_buscado = int(input("DIGITE O ID DO FUNCIONÁRIO QUE DESEJA EDITAR: \n"))
                                funcionario_buscado = Funcoes.buscarPorIdUsuario(id_buscado, dicFuncionarios)
                                funcionario_buscado = Funcoes.validarUsuarioBuscado(funcionario_buscado, dicFuncionarios)

                                while (perfilFuncionario == 1):
                                    opcao = int(input(Funcionario.perfilFuncionario(funcionario_buscado)))
                                    opcao = Funcoes.validarOpcao(opcao, 1, 7, Funcionario.perfilFuncionario(funcionario_buscado))

                                    if (opcao == 1):
                                        # (ADMIN) EDITAR ID DO FUNCIONÁRIO  - OK
                                        input(Funcoes.editarNegativo())

                                    elif (opcao == 2):
                                        # (ADMIN) EDITAR O CPF DO FUNCIONÁRIO - OK
                                        input(Funcoes.editarNegativo())
                                    
                                    elif (opcao == 3):
                                        # (ADMIN) EDITAR O NOME DO FUNCIONÁRIO - OK
                                        opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O NOME DO FUNCIONÁRIO {funcionario_buscado.nome_usuario}")))
                                        opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O NOME DO FUNCIONÁRIO {funcionario_buscado.nome_usuario}")))
                                        
                                        if (opcao == 1):
                                            # (ADMIN) EDITAR O NOME DO FUNCIONÁRIO - SIM - OK
                                            Funcoes.editarNome(funcionario_buscado)
                                            input("TECLE ENTER PARA VOLTAR AO MENU.")
                                        
                                        elif (opcao == 2):
                                            # (ADMIN) EDITAR O NOME DO FUNCIONÁRIO - NÃO - OK
                                            input("TECLE ENTER PARA VOLTAR AO MENU.")
                                    
                                    elif (opcao == 4):
                                        # (ADMIN) EDITAR O EMAIL DO FUNCIONÁRIO - OK
                                        opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O EMAIL DO FUNCIONÁRIO {funcionario_buscado.nome_usuario}")))
                                        opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O EMAIL DO FUNCIONÁRIO {funcionario_buscado.nome_usuario}")))
                                        
                                        if (opcao == 1):
                                            # (ADMIN) EDITAR O EMAIL DO FUNCIONÁRIO - SIM - OK
                                            Funcoes.editarEmail(funcionario_buscado, emails_cadastrados, Aluno)
                                            input("TECLE ENTER PARA VOLTAR AO MENU.")
                                        
                                        elif (opcao == 2):
                                            # (ADMIN) EDITAR O EMAIL DO FUNCIONÁRIO - NÃO - OK
                                            input("TECLE ENTER PARA VOLTAR AO MENU.")
                                    
                                    elif (opcao == 5):
                                        # (ADMIN) EDITAR O CELULAR DO FUNCIONÁRIO - OK
                                        opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O CELULAR DO FUNCIONÁRIO {funcionario_buscado.nome_usuario}")))
                                        opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O CELULAR DO FUNCIONÁRIO {funcionario_buscado.nome_usuario}")))
                                        
                                        if (opcao == 1):
                                            # (ADMIN) EDITAR O CELULAR DO FUNCIONÁRIO - SIM - OK
                                            Funcoes.editarCel(funcionario_buscado, cel_cadastrados, Aluno)
                                            input("TECLE ENTER PARA VOLTAR AO MENU.")
                                        
                                        elif (opcao == 2):
                                            # (ADMIN) EDITAR O CELULAR DO FUNCIONÁRIO - NÃO - OK
                                            input("TECLE ENTER PARA VOLTAR AO MENU.")

                                    elif (opcao == 6):
                                        # (ADMIN) EDITAR O CARGO DO FUNCIONÁRIO - OK
                                        opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O CARGO DO FUNCIONÁRIO {funcionario_buscado.nome_usuario}")))
                                        opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O CARGO DO FUNCIONÁRIO {funcionario_buscado.nome_usuario}")))
                                        
                                        if (opcao == 1):
                                            # (ADMIN) EDITAR O CARGO DO FUNCIONÁRIO - SIM - OK
                                            Funcoes.editarCargo(funcionario_buscado)
                                            input("TECLE ENTER PARA VOLTAR AO MENU.")
                                        
                                        elif (opcao == 2):
                                            # (ADMIN) EDITAR O CARGO DO FUNCIONÁRIO - NÃO - OK
                                            input("TECLE ENTER PARA VOLTAR AO MENU.")

                                    elif (opcao == 7):
                                        # (ADMIN) SAIR DO MENU PERFIL FUNCIONÁRIO - OK
                                        perfilFuncionario = 0
                            
                            elif (opcao == 4):
                                # (ADMIN) EXCLUIR FUNCIONÁRIO - OK
                                Funcoes.excluirUsuario(dicFuncionarios, dicFuncionariosExcluidos)
                            
                            elif (opcao == 5):
                                # (ADMIN) SAIR DO MENU DE FUNCIONÁRIOS - OK
                                menuAdminFuncionarios = 0

                    elif (opcao == 4):
                    # (ADMIN) MÓDULOS - EM ANDAMENTO
                        menuAdminModulos = 1

                        while (menuAdminModulos == 1):
                            opcao = int(input(Funcoes.menuAdminModulos()))
                            opcao = Funcoes.validarOpcao(opcao, 1, 5, Funcoes.menuAdminModulos())

                            if (opcao == 1):
                                # (ADMIN) CADASTRAR MÓDULO - TESTAR
                                Modulo.cadastrarModulo(id_modulo, listaModulos, listaAulas)
                                id_modulo = id_modulo + 1

                            elif (opcao == 2):
                                # (ADMIN) EXIBIR MÓDULOS - TESTAR
                                Funcoes.exibirModulosAdmin(listaModulos)
                                input("TECLE ENTER PARA VOLTAR AO MENU\n")
                            
                            elif (opcao == 3):
                                # (ADMIN) EDITAR MÓDULO - FAZER
                                input("FUNCIONALIDADE EDITAR MÓDULO PELO ADMIN / FUNCIONÁRIO. TECLE ENTER PARA VOLTAR AO MENU")
                            
                            elif (opcao == 4):
                                # (ADMIN) EXCLUIR MÓDULO - TESTAR
                                Funcoes.excluirModulo(listaModulos, listaModulosExcluidos)
                            
                            elif (opcao == 5):
                                # (ADMIN) SAIR DO MENU DE MÓDULOS - OK
                                menuAdminModulos = 0

                    elif (opcao == 5):
                    # (ADMIN) AULAS - EM ANDAMENTO
                        menuAdminAulas = 1

                        while (menuAdminAulas == 1):
                            opcao = int(input(Funcoes.menuAdminAulas()))
                            opcao = Funcoes.validarOpcao(opcao, 1, 5, Funcoes.menuAdminAulas())

                            if (opcao == 1):
                                # (ADMIN) CADASTRAR AULA - TESTAR
                                Aula.cadastrarAula(id_aula, listaAulas, listaQuestoes)
                                id_aula = id_aula + 1

                            elif (opcao == 2):
                                # (ADMIN) EXIBIR AULAS - TESTAR
                                Funcoes.exibirAulasAdmin(listaAulas)
                                input("TECLE ENTER PARA VOLTAR AO MENU\n")
                            
                            elif (opcao == 3):
                                # (ADMIN) EDITAR AULA - FAZER
                                input("FUNCIONALIDADE EDITAR MÓDULO PELO ADMIN / FUNCIONÁRIO. TECLE ENTER PARA VOLTAR AO MENU")
                            
                            elif (opcao == 4):
                                # (ADMIN) EXCLUIR AULA - TESTAR
                                Funcoes.excluirAula(listaAulas, listaAulasExcluidas)
                            
                            elif (opcao == 5):
                                # (ADMIN) SAIR DO MENU DE MÓDULOS - OK
                                menuAdminAulas = 0

                    elif (opcao == 6):
                    # (ADMIN) QUESTÕES - EM ANDAMENTO
                        menuAdminQuestoes = 1

                        while (menuAdminQuestoes == 1):
                            opcao = int(input(Funcoes.menuAdminQuestoes()))
                            opcao = Funcoes.validarOpcao(opcao, 1, 5, Funcoes.menuAdminQuestoes())

                            if (opcao == 1):
                                # (ADMIN) CADASTRAR QUESTÃO - OK
                                Questao.cadastrarQuestao(id_questao, listaQuestoes)
                                id_questao = id_questao + 1

                            elif (opcao == 2):
                                # (ADMIN) EXIBIR QUESTÕES - OK
                                Funcoes.exibirDadosQuestoes(listaQuestoes)
                                input("TECLE ENTER PARA VOLTAR AO MENU\n")
                            
                            elif (opcao == 3):
                                # (ADMIN) EDITAR QUESTÃO - FAZER
                                input("FUNCIONALIDADE EDITAR MÓDULO PELO ADMIN / FUNCIONÁRIO. TECLE ENTER PARA VOLTAR AO MENU")
                            
                            elif (opcao == 4):
                                # (ADMIN) EXCLUIR QUESTÃO - OK
                                Funcoes.excluirQuestao(listaQuestoes, listaQuestoesExcluidas)
                            
                            elif (opcao == 5):
                                # (ADMIN) SAIR DO MENU DE MÓDULOS - OK
                                menuAdminQuestoes = 0