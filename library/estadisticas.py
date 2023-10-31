class Estadisticas:
    def __init__(self, temporadas: int, puntos_totales: int,promedio_puntos_por_partido: float,rebotes_totales: int,promedio_rebotes_por_partido: float,asistencias_totales: int,promedio_asistencias_por_partido: float,robos_totales: int,bloqueos_totales: int,porcentaje_tiros_de_campo: float,porcentaje_tiros_libres: float,porcentaje_tiros_triples: float):

        self.__temporadas = temporadas
        self.__puntos_totales = puntos_totales
        self.__promedio = promedio_puntos_por_partido
        self.__rebotes_totales = rebotes_totales
        self.__promedio_rebotes_por_partido = promedio_rebotes_por_partido
        self.__asistencias_totales = asistencias_totales
        self.__promedio_asistencias_por_partido = promedio_asistencias_por_partido
        self.__robos_totales = robos_totales
        self.__bloqueos_totales = bloqueos_totales
        self.__porcentaje_tiros_de_campo = porcentaje_tiros_de_campo
        self.__porcentaje_tiros_libres = porcentaje_tiros_libres
        self.__porcentaje_tiros_triples = porcentaje_tiros_triples

    @property
    def Temporadas(self):
        return self.__temporadas
    @Temporadas.setter
    def Temporadas(self, n_temporada):
        self.__temporadas = n_temporada

    @property
    def Puntos_totales(self):
        return self.__puntos_totales
    @Puntos_totales.setter
    def Puntos_totales(self, n_puntos):
        self.__puntos_totales = n_puntos

    @property
    def Promedio(self):
        return self.__promedio
    @Promedio.setter
    def Promedio(self,n_promedio):
        self.__promedio = n_promedio

    @property
    def Rebotes_totales(self):
        return self.__rebotes_totales
    @Rebotes_totales.setter
    def Rebotes_totales(self, n_rebote):
        self.__rebotes_totales = n_rebote

    @property
    def Promedio_rebotes_por_partido(self):
        return self.__promedio_rebotes_por_partido
    @Promedio_rebotes_por_partido.setter
    def Promedio_rebotes_por_partido(self, n_promedio_rebotes):
        self.__promedio_rebotes_por_partido = n_promedio_rebotes
    
    @property
    def Asistencias_totales(self):
        return self.__asistencias_totales
    @Asistencias_totales.setter
    def Asistencias_totales(self, n_asistencias):
        self.__asistencias_totales = n_asistencias
        
    @property
    def Promedio_asistencias_por_partido(self):
        return self.__promedio_asistencias_por_partido
    @Promedio_asistencias_por_partido.setter
    def Promedio_asistencias_por_partido(self,n_proimedio):
        self.__promedio_asistencias_por_partido = n_proimedio

    @property
    def Robos_totales(self):
        return self.__robos_totales
    @Rebotes_totales.setter
    def Robos_totales(self, n_robos):
        self.__robos_totales = n_robos

    @property
    def Bloqueos_totales(self):
        return self.__bloqueos_totales
    @Bloqueos_totales.setter
    def Bloqueos_totales(self,n_bloqueos):
        self.__bloqueos_totales = n_bloqueos

    @property
    def Porcentaje_tiros_de_campo(self):
        return self.__porcentaje_tiros_de_campo
    @Porcentaje_tiros_de_campo.setter
    def Porcentaje_tiros_de_campo(self,n_porcentaje):
        self.__porcentaje_tiros_de_campo = n_porcentaje

    @property
    def Porcentaje_tiros_libres(self):
        return self.__porcentaje_tiros_libres
    @Porcentaje_tiros_libres.setter
    def Porcentaje_tiros_libres(self,n_porcentaje):
        self.__porcentaje_tiros_libres = n_porcentaje

    @property
    def Porcentaje_tiros_triples(self):
        return self.__porcentaje_tiros_triples
    @Porcentaje_tiros_triples.setter
    def Porcentaje_tiros_triples(self,n_porcentaje):
        self.__porcentaje_tiros_triples = n_porcentaje

    def Get_estadisticas(self)->dict:
        '''
        Devuelve las estadisticas en forma de diccionario
        Recibe: None
        Retorna: dict
        '''
        return {
            "Temporadas": self.__temporadas,
            "Puntos totales": self.__puntos_totales,
            "Promedio": self.__promedio,
            "Rebotes totales": self.__rebotes_totales,
            "Promedio de rebotes por partido": self.__promedio_rebotes_por_partido,
            "Asistencias totales": self.__asistencias_totales,
            "Promedio de asistencias por partido": self.__promedio_asistencias_por_partido,
            "Robos totales": self.__robos_totales,
            "Bloqueos totales": self.__bloqueos_totales,
            "Porncentaje de tiros de campo": self.__porcentaje_tiros_de_campo,
            "Porcentaje de tiros libres": self.__porcentaje_tiros_libres,
            "Procentaje de tiros triples": self.__porcentaje_tiros_triples
        }