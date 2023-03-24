from typing import List
from Aula import Aula
from Level import Level
from Funcoes import Funcoes

class Modulo:
    def __init__(self, id_modulo = None, nome_modulo = None, level_modulo = None):
        self._id_modulo = id_modulo
        self._nome_modulo = nome_modulo
        self._level_modulo = level_modulo
        self._aulas_modulo = []

    def add_aula(self, aula: Aula):
        self._aulas_modulo.append(aula)

    def remove_aula(self, aula: Aula):
        if aula in self._aulas_modulo:
            self._aulas_modulo.remove(aula)

    def listar_aulas(self):
        if not self._aulas_modulo:
            print("Não há aulas cadastradas nesse módulo.")
        else:
            print(f"Lista de aulas do módulo {self.nome_modulo}:")
            for aula in self._aulas_modulo:
                print(f"ID: {aula.id_aula} | Nome: {aula.nome_aula}")

    @property
    def id_modulo(self) -> int:
        return self._id_modulo

    @property
    def nome_modulo(self) -> str:
        return self._nome_modulo

    @property
    def level_modulo(self) -> Level:
        return self._level_modulo

    @property
    def aulas_modulo(self) -> List[Aula]:
        return self._aulas_modulo

    @aulas_modulo.setter
    def aulas_modulo(self, aulas: List[Aula]):
        self._aulas_modulo = aulas

    def cadastrarModulo(id_modulo, listaModulos, listaAulas):
        # INSTANCIANDO NOVO MÓDULO - OK
        novo_modulo = Modulo()

        Funcoes.menuCabecalho

        # SETANDO O ID DO NOVO MÓDULO - OK
        novo_modulo.id_modulo = id_modulo

        # SETANDO O NOME DO NOVO MÓDULO - OK
        nome_modulo = input("DIGITE O NOME DO MÓDULO: ")
        nome_modulo = Funcoes.validarPreenchimento("DIGITE O NOME DO MÓDULO: ", nome_modulo)
        novo_modulo.nome_modulo = nome_modulo

        # SETANDO O LEVEL DO NOVO MÓDULO - OK
        level_modulo = int(input(f"QUAL O LEVEL DO MÓDULO?" + "\n" +
                            "01. EASY" + "\n" +
                            "02. MEDIUM" + "\n" + 
                            "03. HARD" + "\n" + 
                            Funcoes.menuRodape()))

        level_modulo = Funcoes.validarOpcao(level_modulo, 1, 3, level_modulo)
        novo_modulo.level_modulo = level_modulo

        # SETANDO AS AULAS DO NOVO MÓDULO - OK
        selecionar_aulas = 1
        aulas_modulo = []

        while (selecionar_aulas == 1):
            print(Funcoes.exibirAulasAdmin(listaAulas))
            id_aula = int(input("DIGITE O ID DA AULA QUE DESEJA ADICIONAR A ESTE NOVO MÓDULO: "))
            id_aula = Funcoes.validarPreenchimento("DIGITE O ID DA AULA QUE DESEJA ADICIONAR A ESTE NOVO MÓDULO: ", id_aula)

            for aula in listaAulas:
                if aula.id_aula == id_aula:
                    aula_selecionada = aula
            
            if aula_selecionada is not None:
                aulas_modulo.append(aula_selecionada)
            else:
                print("AULA NÃO ENCONTRADA")
            
            print("------------------------------------------")
            opcao = int(input("DESEJA ADICIONAR NOVA AULA?" + "\n" +
                            "01. SIM" + "\n" +
                            "02. NÃO" + "\n"))
            opcao = int(Funcoes.validarOpcao(opcao,1,2, opcao = int(input("DESEJA ADICIONAR NOVA AULA?" + "\n" +
                            "01. SIM" + "\n" +
                            "02. NÃO" + "\n"))))
            
            if (opcao == 1):
                selecionar_aulas = 1
            
            elif (opcao == 2):
                selecionar_aulas = 0                

        # ADICIONANDO O MÓDULO NA LISTA DE MÓDULOS - OK
        novo_modulo = Modulo(id_modulo = id_modulo, nome_modulo = nome_modulo, level_modulo = level_modulo, aulas_modulo = aulas_modulo)
        listaModulos.append(novo_modulo)

        print("MÓDULO CADASTRADO COM SUCESSO!")
        input("TECLE ENTER PARA VOLTAR AO MENU INICIAL\n")
