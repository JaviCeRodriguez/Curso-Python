secuencia = 'ATGCCTTTACTTGGGTGAATGCCTTTACTTGGGTGAATGCCTTTACTTGGGTGAATGCCTTTACTTGGGTGA'
secuencias = {} # Diccionario
sec_aux = 'AAA'
num = 1

while (len(secuencia) >= 3):
    if secuencia[0:3] == 'ATG':
        print(f'Se detecto codon de inicio {secuencia[0:3]}')
        sec_aux = secuencia[0:3]

    elif (secuencia[0:3] in ['TAA', 'TAG', 'TGA']):
        if (sec_aux[0:3] == 'ATG'):
            print(f'Se detecto codon de fin {secuencia[0:3]}')
            sec_aux += secuencia[0:3]
            secuencias['secuencia' + str(num)] = sec_aux
            sec_aux = 'AAA'
            num += 1

    else:
        sec_aux += secuencia[0:3]

    secuencia = secuencia[3:]


print(secuencias)