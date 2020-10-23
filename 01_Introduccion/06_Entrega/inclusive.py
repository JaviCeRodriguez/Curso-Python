#Queremos hacer un traductor que cambie las palabras masculinas de una frase
#por su versión neutra. Como primera aproximación, completá el siguiente código
#para reemplazar todas las letras 'o' que figuren en el último o anteúltimo
#caracter de cada palabra por una 'e'. Por ejemplo 'todos somos programadores'
#pasaría a ser 'todes somes programdores'. Guardá tu código en el archivo
#inclusive.py

# Alumno: Javier Ceferino Rodriguez
# E-mail: javicerodriguez@gmail.com

frase = '¿cómo transmitir a los otros el infinito Aleph?'
palabras = frase.split()
#print(palabras) # Para ver como queda la frase luego del split
i = 0
for palabra in palabras:
	if palabra[-1] == 'o':
		palabras[i] = palabra[:-1] + 'e'
	elif (len(palabra) >= 2) and (palabra[-2] == 'o'):
		palabras[i] = palabra[:-2] + 'e' + palabra[-1:]
	i = i + 1
frase_t = ' '.join(palabras)
print(frase_t)
