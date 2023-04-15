#Ejercicio uno

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Hola, " + nombre + ". Puedes ingresar.")
else:
    print("Hola, " + nombre + ". Eres menor de edad, no puedes ingresar.")

#Ejercicio dos

nombre_animal = input("Ingresa el nombre del animal: ")

comida_preferida = input("Ingresa la comida preferida del animal: ")

precio_comida = float(input("Ingresa el precio de la comida en pesos: "))

veces_comida_semana = int(input("Ingresa la cantidad de veces que come en la semana: "))

valor_semana = precio_comida * veces_comida_semana

if valor_semana <= 50000:
    print("Eres un animal económico")
else:
    print("Tus gastos animales son muy altos")

#Ejercicio tres

numero1 = float(input("Ingresa el primer número: "))

numero2 = float(input("Ingresa el segundo número: "))

if numero1 > numero2:
    print("El primer número es el mayor:", numero1)
elif numero1 < numero2:
    print("El segundo número es el mayor:", numero2)
else:
    print("Los números son iguales.")

#Ejercio cuatro

nombre = input("Ingresa el nombre del estudiante: ")

valor_matricula = float(input("Ingresa el valor de la matrícula: "))

estrato = int(input("Ingresa el estrato del estudiante: "))


if estrato < 4:
    descuento = valor_matricula * 0.40
else:
    descuento = valor_matricula * 0.05

total_pagar = valor_matricula - descuento

print("Nombre del estudiante: ", nombre)
print("Valor de la matrícula: ", valor_matricula)
print("Estrato: ", estrato)
print("Valor del descuento: ", descuento)
print("Total a pagar: ", total_pagar)

#Ejercicio 5

placa = input("Ingresa la placa de la moto: ")

horas = int(input("Ingresa el número de horas que estará la moto en el parqueadero: "))

if horas > 5:
    valor_pagar = 10000
else:
    valor_pagar = 2800 * horas

print("Placa de la moto: ", placa)
print("Número de horas: ", horas)
print("Valor a pagar: ", valor_pagar)



