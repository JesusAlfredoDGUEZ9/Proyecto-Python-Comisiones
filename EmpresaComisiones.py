print ("Empresa Fast te da la bienvenida. \nCALCULO DE COMISIONES.")

nombre = input("Estimado trabajador, Ingresa tu nombre completo: ")

venta = int(input("Ingresa tu venta del mes: "))

calculo = venta * 13/100

comision = round(calculo,2)

print(f"Estimado {nombre} tu comisión del mes es: {comision}")