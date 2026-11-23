# Solución de la problemática: reservaciones de habitaciones en un hotel
# Arreglos unidimensionales paralelos

# Ingreso del número de reservaciones
numero_reservaciones = int(input('Ingrese el número de reservaciones a registrar: '))

# Arreglos para almacenar los datos de cada reservación
nombres = []
apellidos = []
noches = []
precios = []
totales = []

contador = 0
acumulador = 0

# Registro de reservaciones mediante arreglos paralelos
while contador < numero_reservaciones:
    print('REGISTRO DE RESERVACIÓN', contador + 1)
    nombre = input('Ingrese el nombre del huésped: ')
    apellido = input('Ingrese el apellido del huésped: ')
    cantidad_noches = int(input('Ingrese la cantidad de noches: '))
    precio = float(input('Ingrese el precio por noche: '))

    subtotal = cantidad_noches * precio

    # Determinación del descuento según la cantidad de noches
    if cantidad_noches == 1:
        porcentaje = 0.05
    else:
        if cantidad_noches >= 2 and cantidad_noches <= 3:
            porcentaje = 0.12
        else:
            if cantidad_noches >= 4 and cantidad_noches <= 5:
                porcentaje = 0.18
            else:
                porcentaje = 0.30

    descuento = subtotal * porcentaje
    total = subtotal - descuento

    # Almacenar cada reservación en la misma posición de los arreglos
    nombres.append(nombre)
    apellidos.append(apellido)
    noches.append(cantidad_noches)
    precios.append(precio)
    totales.append(total)

    acumulador = acumulador + total
    print(f'Subtotal: {subtotal:.2f}')
    print(f'Descuento: {descuento:.2f}')
    print(f'Total a pagar: {total:.2f}')
    contador = contador + 1

# Cálculo del promedio y búsqueda de mayor y menor
promedio = acumulador / numero_reservaciones
mayor = totales[0]
menor = totales[0]
indice = 1
while indice < numero_reservaciones:
    if totales[indice] > mayor:
        mayor = totales[indice]
    if totales[indice] < menor:
        menor = totales[indice]
    indice = indice + 1

# Reporte final de todas las reservaciones
print('REPORTE FINAL DE RESERVACIONES')
indice = 0
while indice < numero_reservaciones:
    print(f'Reservación: {indice + 1}')
    print(f'Nombre: {nombres[indice]}')
    print(f'Apellido: {apellidos[indice]}')
    print(f'Cantidad de noches: {noches[indice]}')
    print(f'Precio por noche: {precios[indice]:.2f}')
    print(f'Total a pagar: {totales[indice]:.2f}')
    indice = indice + 1

print('RESUMEN')
print(f'Total recaudado: {acumulador:.2f}')
print(f'Promedio de pagos: {promedio:.2f}')
print(f'Reservación de mayor monto: {mayor:.2f}')
print(f'Reservación de menor monto: {menor:.2f}')
