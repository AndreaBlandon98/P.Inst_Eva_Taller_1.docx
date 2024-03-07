motocicleta = input("¿Que motocicleta dese comprar? (Honda, Yamaha, Suzuki, Otras marcas)")
precio = float(input("¿Que precio tiene la motocicleta que desea comprar? "))

if motocicleta == "honda":
    des_precio = precio * 0.05
    precio = precio - des_precio
    print(f'el precio es de {precio}')

if motocicleta == "yamaha":
    des_precio = precio * 0.08
    precio = precio - des_precio
    print(f'el precio es de {precio}')

if motocicleta == "suzuki":
    des_precio = precio * 0.10
    precio = precio - des_precio
    print(f'el precio es de {precio}')

if motocicleta == "otra marca":
    des_precio = precio * 0.02
    precio = precio - des_precio
    print(f'el precio es de {precio}')
