horas = float(input('inghrese sus horas trabajadas: '))
tarifa = float(input('ingrese la tarifa de la hora: '))

pago = print("su pago es:" , horas * tarifa)

if horas > 40:
    incremento = tarifa * 0.50
    tarifa = tarifa + incremento
    print(f'la tarifa es de {incremento}')