import re
from jugador import Jugador

def es_digito(numero: str):
    '''
    Verifica si una cadena es un número de uno o dos dígitos.
    Recibe: str
    Retorna: objeto match si supera la validacion casi contrario None
    '''
    patron = r'^\d{1,2}$'
    return re.match(patron, numero)

def reemplazar_guinoes_por_espacios(string: str) -> str:
    '''
    Reemplaza guiones bajos por espacios en una cadena.
    Recibe: str
    Retorna: str
    '''
    patron = r'_'
    nuevo_texto = re.sub(patron,' ',string)
    return nuevo_texto

def quick_sort(lista: list[dict], key: str,modo: str) -> list[dict] :
    '''
    Ordena una lista de diccionarios usando el algoritmo de Quick Sort. Los ordena segun la clave que reciba como parametro. Segun el modo recibido los ordena de manera descendente("des") o ascendente("asc")
    '''
    if len(lista) < 2:
        return lista
    else:
        lista_copia = lista.copy()
        jugador_pivot = lista_copia.pop()
        mas_grandes = []
        mas_chicos = []

        for jugador in lista_copia:
            if jugador[key] > jugador_pivot[key]:
                mas_grandes.append(jugador)
            elif jugador[key] <= jugador_pivot[key]:
                mas_chicos.append(jugador)
        if modo == 'asc':
            return quick_sort(mas_chicos, key,modo) + [jugador_pivot] + quick_sort(mas_grandes, key,modo)
        return quick_sort(mas_grandes, key,modo) + [jugador_pivot] + quick_sort(mas_chicos, key,modo)
        
def es_nombre_valido(nombre: str):
    patron = r'^[a-zA-z][a-zA-Z ]+[a-z]$'
    return re.match(patron,nombre)

def validar_nombre_archivo(nombre: str):
    patron = r'^[a-zA-z0-9_]+$'
    return re.match(patron,nombre)

def obtener_porcentaje(parte: float, total: float)->float:
    return round((parte/total) * 100,2)


