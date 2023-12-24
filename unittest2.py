#cambiar los numeros en las pruebas

def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def ejecutar_pruebas():
    # Prueba 1: Suma
    resultado_suma = suma(2, 3)
    if resultado_suma != 5:
        print(f"Error en la suma: Se esperaba 5 pero se obtuvo {resultado_suma}")

    # Prueba 2: Resta
    resultado_resta = resta(5, 2)
    if resultado_resta != 3:
        print(f"Error en la resta: Se esperaba 3 pero se obtuvo {resultado_resta}")

    # Prueba 3: Multiplicación
    resultado_multiplicacion = multiplicacion(4, 6)
    if resultado_multiplicacion != 24:
        print(f"Error en la multiplicación: Se esperaba 24 pero se obtuvo {resultado_multiplicacion}")

    # Verificar si alguna prueba falló
    if (
        resultado_suma == 5 and
        resultado_resta == 3 and
        resultado_multiplicacion == 24
    ):
        print("Todas las pruebas han pasado con éxito")

ejecutar_pruebas()
