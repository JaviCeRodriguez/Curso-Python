# obelisco.py
grosor_billete  = 0.11 * 0.001 # 0.11 mm escrito en metros
altura_obelisco = 67.5         # altura en metros
num_billetes    = 1
dia             = 1

while num_billetes * grosor_billete < altura_obelisco:
    print(dia, num_billetes, num_billetes * grosor_billete)
    dia = dia + 1
    num_billetes = num_billetes * 2

print('Cantidad de días', dia)
print('Cantidad de billetes', num_billetes)
print('Altura final', num_billetes * grosor_billete)
