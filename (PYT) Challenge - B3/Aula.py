from typing import List
from Funcoes import Funcoes
from Questao import Questao

class Aula:
    def __init__(self, id_aula=None, nome_aula=None, conteudo_aula=None, questoes_aula=None, comentarios_aula=None):
        self.__id_aula = id_aula
        self.__nome_aula = nome_aula
        self.__conteudo_aula = conteudo_aula
        self.__questoes_aula = questoes_aula if questoes_aula is not None else []
        self.__comentarios_aula = comentarios_aula if comentarios_aula is not None else []
        
    @property
    def id_aula(self):
        return self.__id_aula
    
    @id_aula.setter
    def id_aula(self, id_aula):
        self.__id_aula = id_aula
    
    @property
    def nome_aula(self):
        return self.__nome_aula
    
    @nome_aula.setter
    def nome_aula(self, nome_aula):
        self.__nome_aula = nome_aula
    
    @property
    def conteudo_aula(self):
        return self.__conteudo_aula
    
    @conteudo_aula.setter
    def conteudo_aula(self, conteudo_aula):
        self.__conteudo_aula = conteudo_aula
    
    @property
    def questoes_aula(self):
        return self.__questoes_aula
    
    def add_questao(self, questao):
        self.__questoes_aula.append(questao)
    
    def remove_questao(self, questao):
        self.__questoes_aula.remove(questao)
    
    @property
    def comentarios_aula(self):
        return self.__comentarios_aula
    
    def add_comentario(self, comentario):
        self.__comentarios_aula.append(comentario)
    
    def remove_comentario(self, comentario):
        self.__comentarios_aula.remove(comentario)

    def cadastrarAula(id_aula, listaAulas, listaQuestoes):
        # INSTANCIANDO NOVA AULA - OK
        nova_aula = Aula()

        Funcoes.menuCabecalho

        # SETANDO O ID DA NOVA AULA - OK
        id_aula = id_aula
        nova_aula.id_aula = id_aula

        # SETANDO O NOME DA AULA - OK
        nome_aula = input("DIGITE O NOME DA AULA: ")
        nome_aula = Funcoes.validarPreenchimento("DIGITE O NOME DA AULA: ", nome_aula)
        nova_aula.nome_aula = nome_aula

        # SETANDO O CONTEÚDO DA AULA - OK
        conteudo_aula = input("DIGITE O CONTEÚDO DA AULA: ")
        conteudo_aula = Funcoes.validarPreenchimento("DIGITE O CONTEÚDO DA AULA: ", conteudo_aula)
        nova_aula.conteudo_aula = conteudo_aula

        # SETANDO AS QUESTÕES DA AULA - OK
        selecionar_questoes = 1
        questoes_aula = []

        print("------------------------------------------")
        print("QUESTÕES:")
        while (selecionar_questoes == 1):
            Funcoes.exibirDadosQuestoes(listaQuestoes)
            id_questao = int(input("DIGITE O ID DA QUESTÃO QUE DESEJA ADICIONAR A ESTA NOVA AULA: "))
            id_questao = Funcoes.validarPreenchimento("DIGITE O ID DA QUESTÃO QUE DESEJA ADICIONAR A ESTA NOVA AULA: ", id_questao)
            
            for questao in listaQuestoes:
                if questao.id_questao == id_questao:
                    questao_selecionada = questao
                else:
                    questao_selecionada = None
            
            if questao_selecionada is not None:
                questoes_aula.append(questao_selecionada)
                print("QUESTÃO ADICIONADA COM SUCESSO!")
                input("TECLE ENTER PARA VOLTAR AO MENU")
            else:
                print("QUESTÃO NÃO ENCONTRADA")
                input("TECLE ENTER PARA VOLTAR AO MENU")
            
            print("------------------------------------------") 
            opcao = int(input("DESEJA ADICIONAR NOVA QUESTÃO?" + "\n" +
                            "01. SIM" + "\n" +
                            "02. NÃO" + "\n"))
            opcao = Funcoes.validarOpcao(opcao, 1, 2, "DESEJA ADICIONAR NOVA QUESTÃO?" + "\n" +
                            "01. SIM" + "\n" +
                            "02. NÃO" + "\n")
            
            if (opcao == 1):
                selecionar_questoes = 1
            
            elif (opcao == 2):
                selecionar_questoes = 0 

        # SETANDO OS COMENTÁRIOS DA AULA - OK
        comentarios_aula = []              

        # ADICIONANDO A AULA NA LISTA DE AULAS - OK
        nova_aula = Aula(id_aula = id_aula, nome_aula = nome_aula, conteudo_aula = conteudo_aula, questoes_aula = questoes_aula, comentarios_aula = comentarios_aula)
        listaAulas.append(nova_aula)

        print("AULA CADASTRADA COM SUCESSO!")
        input("TECLE ENTER PARA VOLTAR AO MENU INICIAL\n")
