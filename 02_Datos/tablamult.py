# informe.py

# Alumno: Javier Ceferino Rodriguez
# E-mail: javicerodriguez@gmail.com

sumRef = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # Lista para sumar
sumBase = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # Lista con resultados de sumas

print(end=f"{'    |':^4s}")

for x in range(0,10):
    print(end=f"{x:^4d}")
print(end='\n--------------------------------------------')
for x in range(0,10):
    print(end=f'\n{x:^4d}|')
    if x == 0:
        for i in range(0,10):
            print(end=f"{sumBase[i]:^4d}")
    else:
        for i in range (0,10):
            sumBase[i] += sumRef[i]
            print(end=f"{sumBase[i]:^4d}")