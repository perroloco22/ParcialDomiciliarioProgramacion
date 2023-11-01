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

    def Transformar_Jugador_a_diccionario(self):
        diccionario = {
            "Nombre": self.__nombre,
            "Posicion": self.__posicion,
            "Temporadas": self.__estadisticas.Temporadas,
            "Puntos totales": self.__estadisticas.Puntos_totales,
            "Promedio": self.__estadisticas.Promedio,
            "Rebotes totales": self.__estadisticas.Rebotes_totales,
            "Promedio de rebotes por partido": self.__estadisticas.Promedio_rebotes_por_partido,
            "Asistencias totales": self.__estadisticas.Asistencias_totales,
            "Promedio de asistencias por partido": self.__estadisticas.Promedio_asistencias_por_partido,
            "Robos totales": self.__estadisticas.Robos_totales,
            "Bloqueos totales": self.__estadisticas.Bloqueos_totales,
            "Porncentaje de tiros de campo": self.__estadisticas.Porcentaje_tiros_de_campo,
            "Porcentaje de tiros libres": self.__estadisticas.Porcentaje_tiros_libres,
            "Procentaje de tiros triples": self.__estadisticas.Porcentaje_tiros_triples,
            "Logros": self.Logros
        }
        return diccionario







