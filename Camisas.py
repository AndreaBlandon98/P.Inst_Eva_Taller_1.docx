compra = int(input("cuantas camisas compro: "))

if compra < 3:
    descuento = compra * 0.10
    compra = compra - descuento
print(f'el descuento es de {compra}')

if compra >= 3:
    descuento = compra * 0.20
    compra = compra - descuento
print(f'el descuento es de {compra}')




