from estadisticas import Estadisticas

class Jugador:    
    def __init__(self, nombre: str = None, posicion: str = None, logros: str = None, estadisticas: Estadisticas = None):
        self.__nombre = nombre
        self.__posicion = posicion
        self.__logros = logros
        self.__estadisticas = estadisticas

    @property
    def Nombre(self):
        return self.__nombre

    @Nombre.setter
    def Nombre(self, n_nombre):
        self.__nombre = n_nombre

    @property
    def Posicion(self):
        return self.__posicion
    
    @Posicion.setter
    def Posicion(self, n_posicion):
         self.__posicion = n_posicion

    @property
    def Logros(self):
        return self.__logros
    
    @Logros.setter
    def Logros(self, n_logros):
        self.__logros = n_logros

    @property
    def Estadisticas(self):
        return self.__estadisticas

    @Estadisticas.setter
    def Estadisticas(self,n_estadistica):
        self.__estadisticas = n_estadistica   








