#NOTE: CLASS CREATED IN ADDITION BECAUSE I THOUGHT IT WAS GOOD TO KNOW HOW TO USE THE MACHINE
#class to define the use of the machine


class clsUsoMaquinaria:

    def __init__(self, tipo_trabajo, terreno, carga_maxima):
        self.__tipo_trabajo = tipo_trabajo
        self.__terreno = terreno
        self.__carga_maxima = carga_maxima

    @property
    def tipo_trabajo(self): return self.__tipo_trabajo

    @property
    def terreno(self): return self.__terreno

    @property
    def carga_maxima(self): return self.__carga_maxima






