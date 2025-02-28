#class to define the coupling of the machine and whether it can be removed

class clsAcople:

    def __init__(self, nombre, permanente, uso):
        self.__nombre = nombre
        self.__permanente = permanente # El acople se puede quitar o no
        self.__uso = uso

    @property
    def nombre(self): return self.__nombre

    @property
    def permanente(self): return self.__permanente

    @property
    def uso(self): return self.__uso
