# ///---- lote.py ----///
# Alumno: Javier Ceferino Rodriguez
# E-mail: javicerodriguez@gmail.com

class Lote:
    '''
    Clase lote para elaboración de informe de camion
    '''
    def __init__(self, nombre, cajones, precio):
        '''
        Defino mis atributos nombre, cajones y precio
        '''
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio

    def costo(self):
        '''
        Devuelvo costo = cajones * precio
        '''
        return (self.cajones * self.precio)
    
    def vender(self, caj_vender):
        '''
        Vendo cajones y resto del total
        '''
        self.cajones -= caj_vender

    def __repr__(self):
        '''
        Muestro contenido de Lote en memoria
        '''
        return f'Lote({self.nombre}, {self.cajones}, {self.precio})'