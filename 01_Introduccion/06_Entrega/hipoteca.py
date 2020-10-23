# hipoteca.py

# Alumno: Javier Ceferino Rodriguez
# E-mail: javicerodriguez@gmail.com

# /-------- Variables --------/
saldo = 500000.0
tasa = 0.05
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 0 # Antes era 1000, ajuste para que el saldo se acerque a 0
mes = 0
pago_mensual = 2684.11
total_pagado = 0.0

# /-------- Calculos --------/
# Mientras tenga saldo por pagar, entro al ciclo while
print('Mes\t Total pagado\t Saldo restante') # Cabecera de tabla

while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    # Pago extra entre mes 61 y mes 108, entro al siguiente if
    if (mes >= pago_extra_mes_comienzo) and (mes <= pago_extra_mes_fin):
        saldo = saldo - pago_extra
        total_pagado = total_pagado + pago_extra
    mes = mes + 1
    print(f'{mes} \t {total_pagado:0.2f} \t {saldo:0.2f}')
    #print(mes, '\t', round(total_pagado, 2), '\t', round(saldo, 2)) # Filas de tabla

# Informe final
print('Total pagado', round(total_pagado, 2), 'en', mes, 'meses.')
