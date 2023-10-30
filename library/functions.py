import re


def es_digito(numero):
    patron = r'^\d{1,2}$'
    return re.match(patron, numero)

def reemplazar_guinoes_por_espacios(string: str) -> str:
    patron = r'_'
    nuevo_texto = re.sub(patron,' ',string)
    return nuevo_texto

def quick_sort(lista: list[dict], key: str,modo: str) -> list[dict] :
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
