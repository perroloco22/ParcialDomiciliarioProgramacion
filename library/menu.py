import re
from equipo import Equipo

#Constantes
RUTA_JSON = './Data/dream_team.json'

class Menu:
  def __init__(self):
    self.__menu = \
'''
Menú:
1-Mostrar la lista de todos los jugadores del Dream Team
2-Ingresar un indice y mostrar las estadisticas del jugador
3-Guardar las estadisticas del jugador de la opcion 2
4-Buscar jugador por su nombre y mostrar sus logros
5-Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente.
6-Buscar un jugador por su nombre y mostrar si es miembro del Salon de la fama del baloncesto
7-Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.
8-Ordenar el listado de manera descendente y mostrarlo, guardarlo en un archivo CSV, guardarlo en un archivo JSON con el nombre que usted desee y guardarlos en una base de datos
9-Mostrar la cantidad deseada de jugadores ordenados por la suma de robos y bloqueos totales con su respectivo porcentaje

0-Salir del menu
'''
    self.__equipo = Equipo(RUTA_JSON)
    self.__equipo_creado = self.__equipo.Crear_equipo()


  #Metodos privados

  def __Validar_opcion_seleccionada(self, opcion: str):
    '''
    Valida si la opción seleccionada.
    Recibe: str
    Retorna: Match si es que supero la validacion, caso contrario None
    '''
    patron = r'^[0-9]$'
    return re.match(patron,opcion)
    
  
  def __Seleccionar_opcion(self):
    '''
    Solicita al usuario que ingrese una opción del menú.
    Recibe: None
    Retorna: str.
    '''
    return input('Ingrese la opcion deseada..\n')

  #Metodos publicos

  def Mostrar_menu(self) -> None:
    '''
    Muestra y gestiona el menú interactivo.
    Recibe: None
    Retorna: None
    '''
    if not self.__equipo_creado:
      print('Hay un error en la creacion del equipo')
      return
      
    
    while True:
      print(self.__menu)
      opcion_seleccionada = self.__Validar_opcion_seleccionada(self.__Seleccionar_opcion())
      if not opcion_seleccionada:
        print('Ingrese una opcion entre 0 y 10')
        continue
      opcion_seleccionada = opcion_seleccionada.group()
      if opcion_seleccionada == "1":
        self.__equipo.Mostrar_Jugadores()
      elif opcion_seleccionada == "2":
        indice = input("Ingresar el indice de un jugador")
        self.__equipo.Ver_estadisticas_del_jugador(indice)
      elif opcion_seleccionada == "3":
        self.__equipo.Guardar_estadisticas()
      elif opcion_seleccionada == "4":
        nombre_del_jugador = input('Ingrese el nombre del jugador deseado')
        self.__equipo.Ver_logros_de_un_jugador(nombre_del_jugador)
      elif opcion_seleccionada == "5":
        self.__equipo.Calcular_y_mostrar_promedio_orndenado()
      elif opcion_seleccionada == "6":
        print(self.__equipo.Pertenece_al_salon_de_la_fama())
      elif opcion_seleccionada == "7":
        self.__equipo.Jugador_con_mas_rebotes()
      elif opcion_seleccionada == "8":
        self.__equipo.Mostrar_jugadores_ordenados_por_temporadas_desc()
        self.__equipo.Guardar_jugadores_ordenados_por_temporadas_desc()
        self.__equipo.Guardar_jugadores_ordenados_por_temporadas_desc_Json()
        self.__equipo.Guardar_en_base_datos_jugadores_ordenados_por_temporadas_desc()
      elif opcion_seleccionada == "9":
        self.__equipo.Mostrar_jugadores_segun_robo_mas_bloqueos()
      elif opcion_seleccionada == "10":
        self.__equipo.Guardar_tabla_posiciones()           
      else:
        print('Nos volveremos a encontrar, adios!')
        break      

    
  
    

    



