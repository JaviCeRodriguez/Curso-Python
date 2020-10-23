# hipoteca.py

saldo = 500000.0
tasa = 0.05
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
mes = 0
pago_mensual = 2684.11
total_pagado = 0.0

while saldo > 0:
    if (mes >= pago_extra_mes_comienzo) and (mes <= pago_extra_mes_fin):
        pago_mensual = pago_mensual + pago_extra
    else:
        pago_mensual = 2684.11
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    mes = mes + 1
    print(f'{mes}\t{total_pagado:0.2f}\t{saldo:0.2f}')
    #print(mes, '	', round(total_pagado,2), '	', round(saldo,2))

#print('Total pagado', round(total_pagado, 2), 'en', mes, 'meses')
