# Usá una iteración sobre el string cadena para agregar la sílaba 'pa', 'pe',
#'pi', 'po', o 'pu' según corresponda luego de cada vocal.

# Alumno: Javier Ceferino Rodriguez
# E-mail: javicerodriguez@gmail.com

cadena = 'Geringoso' # Cadena de referencia
capadepenapa = '' # Cadena para rellenar
for c in cadena:
	if c == 'a':
		capadepenapa = capadepenapa + 'apa'
	elif c == 'e':
		capadepenapa = capadepenapa + 'epe'
	elif c == 'i':
		capadepenapa = capadepenapa + 'ipi'
	elif c == 'o':
		capadepenapa = capadepenapa + 'opo'
	elif c == 'u':
		capadepenapa = capadepenapa + 'upu'
	else:
		capadepenapa = capadepenapa + c
print(capadepenapa)

# Otra opcion del for
# for c in cadena:
# 	if c in ('a', 'e', 'i', 'o', 'u'):
#		c = c + 'p' + c
#	capadepenapa += c
# print(capadepenapa)
