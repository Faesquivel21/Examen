class clsChasis:


    def __init__(self, vim, material):
        self.__vim = vim
        self.__material = material

    @property
    def vim(self): return self.__vim

    @property
    def material(self): return self.__material
