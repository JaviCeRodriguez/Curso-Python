# ///---- canguros_buenos.py ----///
# Alumno: Javier Ceferino Rodriguez
# E-mail: javicerodriguez@gmail.com

#! Canguros buenos

class Canguro:
    '''
    Clase: Canguro
    Metodos: __init__, meter_en_marsupio, __str__
    '''
    def __init__(self, nombre, contenido_marsupio=[]):
        '''
        __init__(string nombre, list marsupio)
        Defino nombre y contenido en marsupio del canguro
        '''
        self.nombre = nombre
        self.contenido_marsupio = contenido_marsupio
    
    def meter_en_marsupio(self, coso):
        '''
        meter_en_marsupio(string coso)
        Ingreso objetos en marsupio. Devuelve lista contenido_marsupio
        '''
        self.contenido_marsupio.append(coso)

    def __str__(self):
        '''
        __str__()
        Crea lista de strings con datos del canguro
        '''
        inventario = [self.nombre + ' tiene en su marsupio: ']
        for cosito in self.contenido_marsupio:
            inventario.append('\t'*2 + '-> ' + cosito)
        return '\n'.join(inventario)
    
madre = Canguro('Mamá Canguro')
hijo = Canguro('Burise')
madre.meter_en_marsupio('Choripan')
madre.meter_en_marsupio('Termidor Blanco')
madre.meter_en_marsupio(hijo.nombre)
print(madre)



#! canguro_malo.py
"""Este código continene un 
bug importante y dificil de ver
"""

class Canguro:
    """Un Canguro es un marsupial."""
    
    def __init__(self, nombre, contenido=[]):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        self.contenido_marsupio = contenido

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)


madre_canguro = Canguro('Madre')
cangurito = Canguro('gurito')
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')
#madre_canguro.meter_en_marsupio(cangurito)
madre_canguro.meter_en_marsupio(cangurito.nombre)

print(madre_canguro)

# Entiendo que es meter al cangurito y supuestamente el no guarda nada
#por lo tanto, la solucion a esto seria la linea 84 (o la que sigue de la
# linea comentada!)
