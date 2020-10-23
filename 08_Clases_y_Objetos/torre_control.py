# ///---- torre_control.py ----///
# Alumno: Javier Ceferino Rodriguez
# E-mail: javicerodriguez@gmail.com


class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''
    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0


class TorreDeControl():
    '''
    Simulacion de Torre de control
    '''
    def __init__(self):
        '''
        Defino arribos y partidas de tipo Cola
        '''
        self.arribos = Cola()
        self.partidas = Cola()

    def nuevo_arribo(self, arribo):
        '''
        Inserto en arribos el proximo vuelvo.
        Necesito como argumento el nombre del vuelo.
        '''
        return self.arribos.encolar(arribo)
    
    def nueva_partida(self, partida):
        '''
        Inserto en partidas el proximo vuelo
        Necesito como argumento el nombre del vuelo.
        '''
        return self.partidas.encolar(partida)

    def ver_estado(self):
        '''
        Reviso el estado de los vuelos en arribos y partidas
        '''
        if (not self.arribos.esta_vacia()):
            print(f'Vuelos esperando para aterrizar: ', end='')
            print(', '.join(self.arribos.items))
        else:
            print('No hay vuelos esperando para aterrizar')
        if (not self.partidas.esta_vacia()):
            print(f'Vuelos esperando para despegar: ', end='')
            print(', '.join(self.partidas.items))
        else:
            print('No hay vuelos esperando para despegar: ')

    def asignar_pista(self):
        if (not self.arribos.esta_vacia()):
            print(f'El vuelo {self.arribos.desencolar()} aterrizó con éxito')
        elif (not self.partidas.esta_vacia()):
            print(f'El vuelo {self.partidas.desencolar()} despegó con éxito')
        else:
            print('No hay vuelos en espera')


# Pruebas en consola
# py -i torre_control.py
# torre = TorreDeControl()
# torre.nuevo_arribo('AR156')
# torre.nueva_partida('KLM1267')
# torre.nuevo_arribo('AR32')
# torre.ver_estado()
# torre.asignar_pista()
# torre.asignar_pista()
# torre.asignar_pista()
# torre.asignar_pista()