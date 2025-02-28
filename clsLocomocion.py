#class to define how it moves

class clsLocomocion:


    def __init__(self, tipo, distribucion, traccion):
        self.__tipo = tipo
        self.__distribucion = distribucion
        self.__traccion = traccion

    @property
    def tipo(self): return self.__tipo

    @property
    def distribucion(self): return self.__distribucion

    @property
    def traccion(self): return self.__traccion