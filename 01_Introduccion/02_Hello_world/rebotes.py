#	Una pelota de goma es arrojada desde una altura de 100 metros
# y cada vez que toca el piso salta 3/5 de altura desde la que cayo.
# Escribi un programa repotes.py que imprima una tabla mostrando las
# alturas de alcanza luego de sus primeros diez rebotes.

altura		= 100	# altura maxima luego del rebote
rebotes	= 0	# numero de rebotes

while rebotes < 10:
	rebotes = rebotes + 1
	altura = (3/5) * altura
	print (rebotes, round(altura,4))

