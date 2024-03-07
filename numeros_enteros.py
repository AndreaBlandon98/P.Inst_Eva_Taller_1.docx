num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))
num3 = int(input("ingrese el tercer numero: "))



if num1 < num2 and num3:
    print('el primer numero es menor')

if num2 < num3 and num1:
    print('el segundo numero es menor')

if num3 < num1 and num2:
    print('el tercer numero es menor')


suma = num1 + num2 + num3
print(f"la suma de los numeros es:{suma}")


