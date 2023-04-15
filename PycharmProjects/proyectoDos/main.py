# Ejercicio uno
nombre = input("Ingresa el nombre de la persona: ")
horas_estudio = int(input("Ingresa el número de horas que estudia en la semana: "))
total_horas_semana = 168
porcentaje_estudio = (horas_estudio / total_horas_semana) * 100
minutos_estudio = horas_estudio * 60

print("Nombre de la persona: ", nombre)
print("Porcentaje de tiempo dedicado a estudiar: ", porcentaje_estudio, "%")
print("Cantidad de minutos dedicados a estudiar: ", minutos_estudio, "minutos")

#Ejercicio dos

nombre_animal = input("Ingresa el nombre del animal: ")
comida_preferida = input("Ingresa la comida preferida del animal: ")
porciones_diarias = int(input("Ingresa el número de porciones que come el animal al día: "))
valor_porcion = float(input("Ingresa el valor de la porción del animal: "))
costo_diario = porciones_diarias * valor_porcion

print("Nombre del animal: ", nombre_animal)
print("Comida preferida: ", comida_preferida)
print("Número de porciones diarias: ", porciones_diarias)
print("Valor de la porción: $", valor_porcion)
print("Costo de alimentar al animal en el día: $", costo_diario)

#Ejercicio tres

nombre = input("Ingresa tu nombre: ")

edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    mensaje = "Eres mayor de edad."
else:
    mensaje = "Eres menor de edad."

print("Nombre: ", nombre)
print(mensaje)

#Ejercicio cuatro

nombre = input("Ingrese el nombre del estudiante: ")


matricula = float(input("Ingrese el valor de la matrícula: "))


estrato = int(input("Ingrese el estrato del estudiante (1-6): "))


descuento = 0
recargo = 0

if estrato == 1:
    descuento = 0.4
elif estrato == 2:
    descuento = 0.3
elif estrato == 3:
    descuento = 0.1
elif estrato == 4:
    recargo = 0.1
elif estrato == 5:
    recargo = 0.2
elif estrato == 6:
    recargo = 0.4


valor_descuento = matricula * descuento
valor_recargo = matricula * recargo
valor_neto = matricula - valor_descuento + valor_recargo


print("Nombre del estudiante:", nombre)
print("Valor de la matrícula:", matricula)
print("Valor del descuento:", valor_descuento)
print("Valor del recargo:", valor_recargo)
print("Valor neto a pagar:", valor_neto)

#Ejercicio cinco
placa = input("Ingrese la placa del vehículo: ")

tipo = int(input("Ingrese el tipo de vehículo (1=bus, 2=buseta, 3=colectivo, 4=automóvil): "))

num_pasajeros = int(input("Ingrese el número de pasajeros transportados: "))

precio_pasaje = 0
porcentaje_pago_conductor = 0.20

if tipo == 1:
    precio_pasaje = 2200
elif tipo == 2:
    precio_pasaje = 2500
elif tipo == 3:
    precio_pasaje = 3500
elif tipo == 4:
    precio_pasaje = 5500

dinero_recolectado = num_pasajeros * precio_pasaje
pago_conductor = dinero_recolectado * porcentaje_pago_conductor

print("Placa del vehículo:", placa)
print("Dinero recolectado:", dinero_recolectado)
print("Pago para el conductor:", pago_conductor)

#Ejercicio seis

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if num1 > num2:
    print("El primer número ({}) es mayor que el segundo número ({})".format(num1, num2))
elif num1 < num2:
    print("El segundo número ({}) es mayor que el primer número ({})".format(num2, num1))
else:
    print("Los números {} y {} son iguales".format(num1, num2))

#Ejercicio siete
cantidad_pantalones = int(input("Ingrese la cantidad de pantalones a comprar: "))

precio_normal = 60000

descuento = 0

if cantidad_pantalones >= 12:
    descuento = 0.20
elif cantidad_pantalones > 6:
    descuento = 0.10

precio_total = cantidad_pantalones * precio_normal
descuento_total = precio_total * descuento
precio_final = precio_total - descuento_total

print("Descuento: ${}".format(descuento_total))
print("Precio final a pagar: ${}".format(precio_final))

#Ejercicio Ocho ------------

#Ejercicio Nueve


cantidad_docenas = int(input("Ingrese la cantidad de docenas del producto a comprar: "))


precio_docena = 12000


monto_compra = 0
monto_descuento = 0
monto_pagar = 0
unidades_obsequio = 0


monto_compra = cantidad_docenas * precio_docena


if cantidad_docenas > 3:
    descuento = 0.15
    unidades_obsequio = cantidad_docenas - 3
else:
    descuento = 0.10

monto_descuento = monto_compra * descuento
monto_pagar = monto_compra - monto_descuento


print("Monto de la compra: ${}".format(monto_compra))
print("Monto del descuento: ${}".format(monto_descuento))
print("Monto a pagar: ${}".format(monto_pagar))
print("Número de unidades de obsequio: {}".format(unidades_obsequio))

#Ejercicio diez

km_recorridos = float(input("Ingrese la cantidad de kilómetros recorridos: "))

monto_fijo = 300000

monto_adicional_300_1000 = 15000

monto_adicional_1000 = 10000

iva = 0.20

monto_pagar = 0
monto_iva = 0

if km_recorridos <= 300:
    monto_pagar = monto_fijo
elif km_recorridos <= 1000:
    monto_pagar = monto_fijo + (km_recorridos - 300) * monto_adicional_300_1000
else:
    monto_pagar = monto_fijo + 700700 + (km_recorridos - 1000) * monto_adicional_1000

monto_iva = monto_pagar * iva


print("Monto a pagar: ${}".format(monto_pagar))
print("Monto del impuesto (IVA): ${}".format(monto_iva))

# Ejercicio once --------

# Ejercicio doce-----------

#Ejercicio trece

nombre = input("Ingrese el nombre del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))
estudia = input("¿El estudiante estudia? (Sí/No): ").lower() == "sí"
afilado_comfama = input("¿El estudiante está afiliado a Comfama? (Sí/No): ").lower() == "sí"


valor_beca = 0


if edad < 18 and estudia and afilado_comfama:
    valor_beca = 0
elif edad < 18 and not estudia and afilado_comfama:
    valor_beca = 400000
elif edad >= 18 and afilado_comfama:
    valor_beca = 300000
else:
    valor_beca = 50000

print("Nombre del estudiante: {}".format(nombre))
print("Valor de la beca: ${}".format(valor_beca))







