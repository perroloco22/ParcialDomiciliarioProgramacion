from functools import reduce
from functions import *
from jugador import Jugador
from estadisticas import Estadisticas
import json 

RUTA_FILES = './Files/'

class Equipo:
   def __init__(self, root: str):
      #Atributos
      self.__ruta = root
      self.__jugadores = []
      self.__nombre_equipo = ''
      self.__cantidad_jugadores = len(self.__jugadores)
      self.__jugador_actual = None

   #Getters and setters
   @property
   def Ruta(self):
       return self.__ruta
   @Ruta.setter
   def Ruta(self,n_ruta):
       self.__ruta = n_ruta

   @property
   def Jugadores(self):
       return self.__jugadores
   @Jugadores.setter
   def Jugadores(self, n_jugadores):
      self.__jugadores = n_jugadores

   @property
   def Nombre_equipo(self):
      return self.__nombre_equipo 

   @property
   def Cantidad_jugadores(self):
      return self.__cantidad_jugadores
   @Cantidad_jugadores.setter
   def Cantidad_jugadores(self, n_cantidad):
      self.__cantidad_jugadores = n_cantidad    
   
   #Metodos privados
   def __Imprimir_jugador_posicion(self, jg: Jugador) -> None:
      '''
      Esta función privada imprime el nombre y la posición de un jugador.
      Recibe: Jugador
      Retorna: None
      '''
      print(f'{jg.Nombre} - {jg.Posicion}')

   def __Crear_estadistica(self,estadisticas: dict) -> Estadisticas:
      '''
      Crea una instancia de la clase Estadisticas y la retorna
      Recibe: un diccionario
      Retorna: Un objeto Estadisticas
      '''
      temporadas = estadisticas.get('temporadas')
      puntos_totales = estadisticas.get('puntos_totales')
      promedio_puntos_por_partido = estadisticas.get('promedio_puntos_por_partido')
      rebotes_totales = estadisticas.get('rebotes_totales')
      promedio_rebotes_por_partido = estadisticas.get('promedio_rebotes_por_partido')
      asistencias_totales = estadisticas.get('asistencias_totales')
      promedio_asistencias_por_partido = estadisticas.get('promedio_asistencias_por_partido')
      robos_totales = estadisticas.get('robos_totales')
      bloqueos_totales = estadisticas.get('bloqueos_totales')
      porcentaje_tiros_de_campo = estadisticas.get('porcentaje_tiros_de_campo')
      porcentaje_tiros_libres = estadisticas.get('porcentaje_tiros_libres')
      porcentaje_tiros_triples = estadisticas.get('porcentaje_tiros_triples')

      estadistica =\
           Estadisticas(temporadas,puntos_totales,promedio_puntos_por_partido,rebotes_totales,
                        promedio_rebotes_por_partido,asistencias_totales,promedio_asistencias_por_partido,
                        robos_totales,bloqueos_totales,porcentaje_tiros_de_campo,porcentaje_tiros_libres,porcentaje_tiros_triples)
      return estadistica

   def __Crear_jugador(self, jugador: dict) -> Jugador:
      '''
      Crea una instancia de la clase Jugador y la retorna
      Recibe: un diccionario
      Retorna: Un objeto Jugador
      '''
      jugador_transformado = Jugador()
      jugador_transformado.Nombre = jugador.get('nombre')
      jugador_transformado.Posicion = jugador.get('posicion')
      jugador_transformado.Logros = jugador.get('logros')
      estadisticas_diccionario = jugador.get('estadisticas')  
      estadisticas = self.__Crear_estadistica(estadisticas_diccionario)
      jugador_transformado.Estadisticas = estadisticas
      return jugador_transformado

   def __Crear_formate_csv(self)->str:
      '''
      Retorna el un string en formato csv con los campos nombre,posicion y las estadisticas del jugador actual
      Recibe: None
      Retorna: str
      '''
      jugador = self.__jugador_actual   
      encabezado = f'Nombre,Posicion,'
      estadisticas = jugador.Estadisticas.Get_estadisticas()
      claves_de_estadisticas = estadisticas.keys()
      encabezado = encabezado + ','.join(claves_de_estadisticas) + '\n'
      cuerpo = f'{jugador.Nombre},{jugador.Posicion}'
      for clave in claves_de_estadisticas:
         cuerpo += f',{estadisticas.get(clave)}'
      cuerpo += '\n'
      return encabezado + cuerpo

   def __Obtener_jugador_y_promedio_pts_por_partido(self)-> dict:
      '''
      Esta función devuelve un diccionario que contiene los nombres de los jugadores y sus promedios de puntos por partido.
      Recibe: None
      Retorna: dict
      '''

      jugadores_y_promedios= []
      if not self.__jugadores:
         return jugadores_y_promedios
      jugadores = self.__jugadores
      jugadores_y_promedios= [{'Nombre':jugador.Nombre,'Promedio de puntos por partido': jugador.Estadisticas.Promedio} for jugador in jugadores]
      return jugadores_y_promedios

   def __Ordenar_por_nombre(self, jugadores_a_ordenar: list[dict]) -> list[dict]:
      '''
      Ordena jugadores de manera ascendente por el nombre de cada jugador
      Recibe: list[dict]
      Retorna: list[dict]
      '''
      jugadores_ordenados_por_nombres = quick_sort(jugadores_a_ordenar,'Nombre','asc')
      return jugadores_ordenados_por_nombres
   
   def __Calcular_promedio(self, jugadores: list[dict]) -> float:  
      '''
      Calcula el promedio de puntos por partidos de una lista de jugadores
      Recibe: list[dict]
      Retorna: float
      ''' 
      cantidad_jugadores = len(jugadores)
      sumatoria = reduce(lambda acumulador,jugador: acumulador + jugador.get('Promedio de puntos por partido'),jugadores,0)
      return sumatoria / cantidad_jugadores

   def __Buscar_jugador_por_nombre(self,nombre: str):
      '''
      Busca un jugador por su nombre y lo retorna
      Recibe: str
      Retorna: Jugador
      '''
      jugadores = self.__jugadores
      jugador_encontrado = None
      
      for jugador in jugadores:
         if nombre.lower() == jugador.Nombre.lower():
            jugador_encontrado = jugador
            break
      return jugador_encontrado

   #Metodos publicos

   def Crear_equipo(self) -> bool:
      '''
      Esta función carga datos de un archivo JSON para crear un equipo de baloncesto.
      Recibe: None
      Retorna: Bool: True si la creación del equipo fue exitosa, False en caso contrario.
      '''
      if self.__ruta == '':
         return False
      try:
        with open(self.__ruta, 'r',encoding='utf-8') as file:
         data = json.load(file)
         self.__nombre_equipo = data.get('equipo')
         jugadores = data.get('jugadores')
         self.__jugadores = [ self.__Crear_jugador(jugador) for jugador in jugadores]
         self.__cantidad_jugadores = len(self.__jugadores)         
      except:
        print('Ocurrio un error en la creacion del equipo')
        return False
      else:
        return True 
      
   
   def Mostrar_Jugadores(self):
      '''
      Esta función imprime los nombres y posiciones de los jugadores del equipo.
      Recibe: None
      Retorna: str
      '''
      if not self.__jugadores:
         return ''  
      for jugador in self.__jugadores:
         self.__Imprimir_jugador_posicion(jugador)
   
   def Ver_estadisticas_del_jugador(self, index: str) -> None:
      '''
      Esta función muestra las estadísticas de un jugador en el equipo.
      Recibe: index (str): El índice del jugador cuyas estadísticas se desean ver.
      Retorna: None
      '''
      if self.__jugadores and es_digito(index) and int(index) < self.__cantidad_jugadores:         
         self.__jugador_actual = self.__jugadores[int(index)-1]         
         estadisticas = self.__jugador_actual.Estadisticas.Get_estadisticas()
         for key,value in estadisticas.items():
            print(f'{key}: {value}')
      else:
         print('Indice ingresado incorrecto')
         
   def Guardar_estadisticas(self):
      '''
      Esta función guarda las estadísticas de un jugador en un archivo CSV.
      Recibe: None
      Retorna: None
      ''' 
      if not self.__jugador_actual:
         print('Primero debe seleccionar un jugador en la opcion 2')
         return
      texto_a_guardar = self.__Crear_formate_csv()
      try:
         with open(f'{RUTA_FILES}Estadisticas_{self.__jugador_actual.Nombre}.csv', 'w') as file:
           file.write(texto_a_guardar)
      except:
        print('Ocurrio un error en el intento de guardar el archivo ')
      
      
   def Ver_logros_de_un_jugador(self, nombre: str) -> None:
      '''
      Esta función muestra los logros de un jugador en el equipo.
      Recibe: str
      Retorna: None
      '''
      if not self.__jugadores:
         return
      if not es_nombre_valido(nombre):
         print('Nombre de jugador invalido')
         return      
      jugador_encontrado = self.__Buscar_jugador_por_nombre(nombre)      
      for logro in jugador_encontrado.Logros:
         print(logro)
         
   def Calcular_y_mostrar_promedio_orndenado(self):
      '''
      Esta función calcula el promedio de puntos por partido de los jugadores en el equipo, los ordena por nombre y muestra el resultado.
      Recibe: None
      Retorna: None
      '''
      jugadores = self.__Obtener_jugador_y_promedio_pts_por_partido()
      promedio_de_puntos = round(self.__Calcular_promedio(jugadores),2)
      jugadores_ordenados = self.__Ordenar_por_nombre(jugadores)
      clave_promedio ='Promedio de puntos por partido'      
      print(f'{clave_promedio}: {promedio_de_puntos}')
      for jugador in jugadores_ordenados:
         for clave,valor in jugador.items():
            print(f'{clave}: {valor}')
       
   def Pertenece_al_salon_de_la_fama(self) -> str:
      '''
      Esta función verifica si un jugador pertenece al Salón de la Fama del baloncesto y devuelve un mensaje indicando el resultado.
      Recibe: None
      Retorna: str.
      '''

      if not self.__jugadores:
         return 'No hay jugadores en el equipo'
      
      nombre_a_buscar = input('Ingrese el nombre del jugador a comprobar...')
      nombre_validado = es_nombre_valido(nombre_a_buscar)
      if not nombre_validado:
         return 'Nombre invalido'
      
      jugador_buscado = self.__Buscar_jugador_por_nombre(nombre_validado.group())
      if jugador_buscado and 'Miembro del Salon de la Fama del Baloncesto' in jugador_buscado.Logros:
         return f'El jugador {jugador_buscado.Nombre} esta en el salon de la fama del baloncesto'
      return f'El jugador {nombre_validado.group()} no esta en el salon de la fama del baloncesto'
      
   def Jugador_con_mas_rebotes(self):
      '''
      Esta función encuentra y muestra el jugador con la mayor cantidad de rebotes totales en el equipo.
      Recibe: None
      Retorna: None
      '''
      if not self.__jugadores:
         return None
      jugadores = [{'Nombre': jugador.Nombre, 'Rebotes totales': jugador.Estadisticas.Rebotes_totales } for jugador in self.__jugadores]
      jugadores_ordenados_desc = quick_sort(jugadores,'Rebotes totales','desc')
      bandera_primer_jugador = True
      maximo = 0
      for jugador in jugadores_ordenados_desc:
         if bandera_primer_jugador or jugador.get('Rebotes totales') == maximo:
            maximo = jugador.get('Rebotes totales')
            print(f'Nombre: {jugador.get("Nombre")}')
            print(f'Rebotes totales: {jugador.get("Rebotes totales")}')
            bandera_primer_jugador = False
            continue
         break
 

  

     
# test_equipo = Equipo('./Data/dream_team.json')
# test_equipo.Crear_equipo()
# test_equipo.Mostrar_Jugadores()
# test_equipo.Ver_estadisticas_del_jugador("0")
# test_equipo.Guardar_estadisticas()
# test_equipo.Ver_logros_de_un_jugador("michael Jordan")
# test_equipo.Calcular_y_mostrar_promedio_orndenado()
# print(test_equipo.Pertenece_al_salon_de_la_fama())    
# test_equipo.Jugador_con_mas_rebotes()






       
       
    
