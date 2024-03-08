dia = input("ingrese el dia de la compra : (martes, sabado, feriado)")
costo = 30000000

if dia == "martes":
    descuento = 0.12
    costo = costo - descuento
    print("El costo de la moto es igual a", costo)

if dia == "sabado":
    descuento = 0.18
    costo = costo - descuento
    print("El costo de la moto es igual a", costo)

if dia == "feriado":
    descuento = 0.25
    costo = costo - descuento
    print("El costo de la moto es igual a", costo)
