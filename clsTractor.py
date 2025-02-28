"""================================================================================================
Institute....: Universidad Técnica Nacional
Headquarters.: Pacífico
Career.......: Tecnologías de Información
Period.......: 3-2024
Document.....: clsVehiculo.py
Goals........: Oriented Object Programming, multi heritage sample
Professor....: Jorge Ruiz (york)
Student......:
================================================================================================"""


from clsMotor import clsMotor
from clsChasis import clsChasis
from clsLocomocion import clsLocomocion
from clsAcople import clsAcople
from clsUsoMaquinaria import clsUsoMaquinaria

#Class with variables to add tractor data

class clsTractor(clsMotor, clsChasis):


    def __init__(self, placa, capacidad, vimM, cilindros, combustible, minHP, maxHP, vimC, material, peso, velocidad,
                 modelo, locomocion, acoples, uso):
        clsMotor.__init__(self, vimM, cilindros, combustible, minHP, maxHP)
        clsChasis.__init__(self, vimC, material)
        self.__placa = placa
        self.__capacidad = capacidad
        self.__peso = peso
        self.__velocidad = velocidad
        self.__modelo = modelo
        self.__locomocion = locomocion
        self.__acoples = acoples
        self.__uso = uso

    @property
    def placa(self): return self.__placa

    @property
    def capacidad(self): return self.__capacidad

    @property
    def peso(self): return self.__peso

    @property
    def velocidad(self): return self.__velocidad

    @property
    def modelo(self): return self.__modelo

    @property
    def locomocion(self): return self.__locomocion

    @property
    def acoples(self): return self.__acoples

    @property
    def uso(self): return self.__uso