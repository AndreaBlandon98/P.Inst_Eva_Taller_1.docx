sueldo = input("ingrese su sueldo: ")

if sueldo <= 1000:
   descuento = sueldo * 0.10
   sueldo = sueldo - descuento
   print(f"su sueldo es de {sueldo}")

if sueldo == 2000:
    descuento = sueldo * 0.5
    sueldo = sueldo - descuento
    print(f"su sueldo es de {sueldo}")

if sueldo > 2000:
    descuento = sueldo * 0.3
    sueldo = sueldo - descuento
    print(f"su sueldo es de {sueldo}")


