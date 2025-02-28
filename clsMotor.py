#class with engine variables

class clsMotor:


    def __init__(self, vim, cilindros, combustible, minHP, maxHP):
        self.__vim = vim
        self.__cilindros = cilindros
        self.__combustible = combustible
        self.__minHP = minHP
        self.__maxHP = maxHP

    @property
    def vim(self): return self.__vim

    @property
    def cilindros(self): return self.__cilindros

    @property
    def combustible(self): return self.__combustible

    @property
    def minHP(self): return self.__minHP

    @property
    def maxHP(self): return self.__maxHP