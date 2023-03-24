from enum import Enum
from typing import List
from Funcoes import Funcoes
from Resposta import Resposta

class Questao:
    def __init__(self, id_questao: int, pergunta: str, altA: str, altB: str, altC: str, altD: str, altE: str ,resposta: Enum):
        self._id_questao = id_questao
        self._pergunta = pergunta
        self._altA = altA
        self._altB = altB
        self._altC = altC
        self._altD = altD
        self._altE = altE
        self._resposta = resposta

    @property
    def id_questao(self) -> int:
        return self._id_questao

    @property
    def pergunta(self) -> str:
        return self._pergunta

    
    @property
    def altA(self) -> str:
        return self._altA

    @altA.setter
    def altA(self, value: str):
        self._altA = value

    @property
    def altB(self) -> str:
        return self._altB

    @altB.setter
    def altB(self, value: str):
        self._altB = value

    @property
    def altC(self) -> str:
        return self._altC

    @altC.setter
    def altC(self, value: str):
        self._altC = value

    @property
    def altD(self) -> str:
        return self._altD

    @altD.setter
    def altD(self, value: str):
        self._altD = value

    @property
    def altE(self) -> str:
        return self._altE

    @altE.setter
    def altE(self, value: str):
        self._altE = value

    @property
    def resposta(self) -> Enum:
        return self._resposta

    @staticmethod
    def from_dict(questao_dict: dict) -> 'Questao':
        from enum import Enum
        return Questao(
            questao_dict['id_questao'],
            questao_dict['pergunta'],
            Enum(questao_dict['resposta'])
        )

    @staticmethod
    def to_dict(questao: 'Questao') -> dict:
        return {
            'id_questao': questao.id_questao,
            'pergunta': questao.pergunta,
            'resposta': questao.resposta.name
        }

    @staticmethod
    def from_list(questao_list: List[dict]) -> List['Questao']:
        return [Questao.from_dict(questao_dict) for questao_dict in questao_list]

    @staticmethod
    def to_list(questao: List['Questao']) -> List[dict]:
        return [Questao.to_dict(q) for q in questao]

    def cadastrarQuestao(id_questao, listaQuestoes):
        Funcoes.menuCabecalho

        # SETANDO ID DA QUESTÃO - OK
        id_questao = id_questao

        # SETANDO PERGUNTA DA QUESTÃO - OK
        pergunta = input("DIGITE A PERGUNTA DA QUESTÃO: ").upper()
        pergunta = Funcoes.validarPreenchimento("DIGITE A PERGUNTA DA QUESTÃO: ", pergunta)

        # SETANDO RESPOSTA DA QUESTÃO - OK
        print("ALTERNATIVAS: " + "\n" +
            "01. A" + "\n" +
            "02. B" + "\n" + 
            "03. C" + "\n" + 
            "04. D" + "\n" + 
            "05. E")

        print("------------------------------------------")                    
        opcao = int(input("DIGITE A ALTERNATIVA CORRETA DESTA PERGUNTA: "))
        opcao = Funcoes.validarOpcao(opcao, 1, 5, "ALTERNATIVAS: " + "\n" +
            "01. A" + "\n" +
            "02. B" + "\n" + 
            "03. C" + "\n" + 
            "04. D" + "\n" + 
            "05. E" + "\n" + 
            "------------------------------------------" + "\n" + 
            "DIGITE A ALTERNATIVA CORRETA DESTA PERGUNTA: " + "\n")
        if opcao == 1:
            resposta = Resposta.A
        elif opcao == 2:
            resposta = Resposta.B
        elif opcao == 3:
            resposta = Resposta.C
        elif opcao == 4:
            resposta = Resposta.D
        elif opcao == 5:
            resposta = Resposta.E
        print("------------------------------------------")

        # ADICIONANDO A QUESTÃO NA LISTA DE QUESTÕES - OK
        nova_questao = Questao(id_questao = id_questao, pergunta = pergunta, resposta = resposta)
        listaQuestoes.append(nova_questao)

        print("QUESTÃO CADASTRADA COM SUCESSO!")
        input("TECLE ENTER PARA VOLTAR AO MENU INICIAL\n")

    def editarPergunta(questao_buscada, id_questao, listaQuestoes):
        if Funcoes.confirmarAcao("EDITAR PERGUNTA"):
            nova_pergunta = input("DIGITE A NOVA PERGUNTA DA QUESTÃO: ")
            nova_pergunta = Funcoes.validarPreenchimento("DIGITE A NOVA PERGUNTA DA QUESTÃO: ", nova_pergunta)
            questao_buscada.pergunta = nova_pergunta
        print("QUESTÃO EDITADA COM SUCESSO!")
        input("TECLE ENTER PARA VOLTAR AO MENU INICIAL\n")

    def editarResposta(questao_buscada, id_questao, listaQuestoes):
        if Funcoes.confirmarAcao("EDITAR RESPOSTA"):
            print("ALTERNATIVAS: ")
            print("01. A")
            print("02. B")
            print("03. C")
            print("04. D")
            print("05. E")
            opcao = int(input("DIGITE A NOVA ALTERNATIVA CORRETA DESTA PERGUNTA: "))
            Funcoes.validarOpcao(opcao, 1, 5, "menuQuestoesAdmin")
            if opcao == 1:
                nova_resposta = Resposta.A
            elif opcao == 2:
                nova_resposta = Resposta.B
            elif opcao == 3:
                nova_resposta = Resposta.C
            elif opcao == 4:
                nova_resposta = Resposta.D
            elif opcao == 5:
                nova_resposta = Resposta.E

            questao_buscada.resposta = nova_resposta
            print("RESPOSTA EDITADA COM SUCESSO!")
            input("TECLE ENTER PARA VOLTAR AO MENU INICIAL\n")
    
    def perfilQuestao(questao_buscada):
        retornoPerfil = Funcoes.menuCabecalho()
        retornoPerfil += f"01. ID: {questao_buscada.id_questao}\n"
        retornoPerfil += f"02. PERGUNTA: {questao_buscada.pergunta}\n"
        retornoPerfil += f"03. RESPOSTA: {questao_buscada.resposta}\n"
        retornoPerfil += "04. SAIR\n"
        retornoPerfil += Funcoes.menuRodape()
        return retornoPerfil
            
