nombre = input("ingrese su nombre")

nota1 = float(input("ingrese su nota de 1 a 5: "))
nota2 = float(input("ingrese su nota de 1 a 5: "))
nota3 = float(input("ingrese su nota de 1 a 5: "))
nota4 = float(input("ingrese su nota de 1 a 5: "))
nota5 = float(input("ingrese su nota de 1 a 5: "))

promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
if promedio >= 5:
    print("aprobo el curso")
else:
    print("reprobo el curso")