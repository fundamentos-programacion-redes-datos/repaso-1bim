# Problemática: Sistema de reservaciones de habitaciones en un hotel

**Asignatura:** Fundamentos de Programación  
**Tema:** Condicionales, ciclos `while` y arreglos unidimensionales paralelos.

## Descripción del problema

Un hotel ubicado en la ciudad de Loja desea desarrollar un programa para registrar las reservaciones de habitaciones realizadas por sus huéspedes. El hotel aplica descuentos de acuerdo con la cantidad de noches de alojamiento y necesita obtener un reporte de los pagos registrados.

## Entrada de datos

Antes de registrar las reservaciones, el programa debe solicitar cuántas reservaciones se van a procesar.

Para cada reservación se debe ingresar:

- Nombre del huésped.
- Apellido del huésped.
- Cantidad de noches de alojamiento.
- Precio de la habitación por noche.

El precio por noche puede variar de una reservación a otra, pero se mantiene constante durante la estadía de cada huésped.

## Cálculo de descuentos

El hotel aplica los siguientes descuentos según la cantidad de noches reservadas:

| Cantidad de noches | Descuento |
|---|---:|
| 1 noche | 5 % |
| 2 o 3 noches | 12 % |
| 4 o 5 noches | 18 % |
| 6 o más noches | 30 % |

## Cálculo de los pagos

Para cada reservación se debe calcular:

- **Subtotal:** `cantidad de noches × precio por noche`.
- **Descuento:** `subtotal × porcentaje de descuento`.
- **Total a pagar:** `subtotal − descuento`.

El programa debe mostrar estos tres valores al finalizar el registro de cada reservación.

## Registro de múltiples reservaciones

El sistema debe permitir registrar varias reservaciones mediante un ciclo `while`. El número de reservaciones se ingresa antes de iniciar el ciclo.

En cada repetición se debe ingresar la información del huésped, calcular los valores correspondientes y almacenar los datos de la reservación.

## Almacenamiento de información

Se deben utilizar **cinco arreglos unidimensionales paralelos** para registrar:

1. Nombres de los huéspedes.
2. Apellidos de los huéspedes.
3. Cantidad de noches reservadas.
4. Precio de la habitación por noche.
5. Total a pagar por cada huésped.

Las posiciones de los arreglos deben corresponder a una misma reservación. Por ejemplo, la posición `0` representa la primera reservación.

## Reporte final

Al terminar el registro, el programa debe:

1. Mostrar el detalle de cada reservación: nombre, apellido, cantidad de noches, precio por noche y total a pagar.
2. Calcular y mostrar el **total recaudado** por el hotel.
3. Calcular y mostrar el **promedio de los pagos** de las reservaciones.
4. Identificar y mostrar el **monto de la reservación más alta** y el **monto de la reservación más baja**.

## Consideraciones para el desarrollo

Utilizar los conceptos estudiados hasta el momento:

- Variables, entrada y salida de datos y operaciones aritméticas.
- Estructuras condicionales `if-else` anidadas.
- Ciclos `while`.
- Contadores y acumuladores.
- Arreglos unidimensionales paralelos y acceso mediante índices.

**Restricciones:** No utilizar funciones propias, clases, diccionarios, ciclos `for` ni funciones como `sum()`, `max()` o `min()`.

Se considera que se registrará **al menos una reservación**, que la cantidad de noches será mayor que cero y que el precio por noche será positivo.

## Ejemplo de cálculo

Un huésped reserva una habitación durante **4 noches**, a **$40 por noche**:

| Concepto | Valor |
|---|---:|
| Cantidad de noches | 4 |
| Precio por noche | $40,00 |
| Subtotal | $160,00 |
| Descuento (18 %) | $28,80 |
| **Total a pagar** | **$131,20** |
