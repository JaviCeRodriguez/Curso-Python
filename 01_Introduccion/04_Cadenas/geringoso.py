# Usá una iteración sobre el string cadena para agregar la sílaba 'pa', 'pe', 'pi', 'po', o 'pu' según corresponda luego de cada vocal.

cadena = 'Geringoso'
capadepenapa = ''
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
