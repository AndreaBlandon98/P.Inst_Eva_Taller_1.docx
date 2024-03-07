num1 = int(input('ingrese el primer numero: '))
num2 = int(input('ingrese el segundo numero: '))
num3 = int(input('ingrese el tercer numero: '))

if num1 > num2 and num3:
    print('el primer numero es mayor')
else:
    print("error")

if num2 > num1 and num3:
    print('el segundo numero es mayor')
else:
    print("error")

if num3 > num1 and num2:
    print("el tercer numero es mayor")
else:
    print("error")



