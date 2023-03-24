from typing import List
from datetime import date
from Aluno import Aluno

class Certificado:
    def __init__(self, id_certificado: int, aluno: Aluno, data_certificado: str, curso: str, carga_horaria: int):
        self.__id_certificado = id_certificado
        self.__aluno = aluno
        self.__data_certificado = self.__converter_para_data(data_certificado)
        self.__curso = curso
        self.__carga_horaria = carga_horaria
    
    @property
    def id_certificado(self):
        return self.__id_certificado
    
    @property
    def aluno(self):
        return self.__aluno
    
    @property
    def data_certificado(self):
        return self.__data_certificado
    
    @property
    def curso(self):
        return self.__curso
    
    @property
    def carga_horaria(self):
        return self.__carga_horaria
    
    def __converter_para_data(self, data):
        if isinstance(data, str):
            return date.fromisoformat(data)
        elif isinstance(data, date):
            return data
        else:
            return None
