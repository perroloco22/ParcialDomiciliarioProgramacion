import sqlite3


class BdConexion:
    def __init__(self, cadena_de_conexion: str):
        self.__cadena_de_conexion = cadena_de_conexion 
        self.__formatos_equivalentes ={'int':'integer','string': 'text','float': 'real'}
    
    def __Limpiar_tabla(self, nombre_tabla: str):
        with sqlite3.connect(self.__cadena_de_conexion) as connection:
          try:
            query_delete = f'DELETE FROM {nombre_tabla}'            
            connection.execute(query_delete)
          except sqlite3.OperationalError:
            print(f'La tabla no pudo ser limpiada')


    def __Obtener_tipo_equivalente(self, dato: object)->str:
        '''
        Recibe un objeto y devuelve el objeto equilavente que admite sqlite
        Recibe: object
        Retorna: nombre de objeto equivalente(str)
        '''
        if isinstance(dato,int):
            return self.__formatos_equivalentes['int']
        elif isinstance(dato,float):
            return self.__formatos_equivalentes['float']
        else:
            return self.__formatos_equivalentes['string']

    def Crear_tabla(self,nombre_de_tabla: str, jugador: dict):
        '''
        Crea una tabla en sqlite con el nombre que recibe como parametro. Los campos de la tabla seran las claves que hay en el diccionario que representa un jugador
        Recibe: nombre(str), jugador(dict)
        Retorna: None
        '''
        with sqlite3.connect(self.__cadena_de_conexion) as connection:
          try:
            query = f'create table {nombre_de_tabla}(id integer primary key autoincrement'
            for clave,valor in jugador.items():
                tipo = self.__Obtener_tipo_equivalente(valor)
                query += f',{clave} {tipo}'
            query +=')'
            connection.execute(query)
          except sqlite3.OperationalError:
            print(f'La tabla {nombre_de_tabla} ya existe') 

    def Agregar_registros(self,nombre_de_tabla: str, jugadores: list[dict],agregar: bool):
        '''
        Agrega registros en la tabla. Cada diccionario que representa un jugador sera un registro aniadido en la tabla.
        Recibe: nombre de la tabla(str), jugadores(list[dict])
        Retorna: None
        '''
        try:
            with sqlite3.connect(self.__cadena_de_conexion) as connection:
                if not agregar:
                    self.__Limpiar_tabla(nombre_de_tabla)
                campos = ','.join([clave for clave in jugadores[0].keys()])
                values = ','.join(['?' for clave in jugadores[0].keys()])
                query = f'insert into {nombre_de_tabla}({campos}) values({values})'
                for jugador in jugadores:
                    values = tuple(jugador.values())
                    connection.execute(query,values)                
                connection.commit()
        except sqlite3.OperationalError:
                print('Hubo un error en la ejecucion')
            
