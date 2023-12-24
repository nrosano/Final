# Función que concatena dos cadenas
#cambiar las cadenas en las pruebas

def concatenar_cadenas(cadena1, cadena2):
    return cadena1 + cadena2

def realizar_pruebas_concatenacion():
    # Prueba 1: Concatenación exitosa
    resultado_prueba_1 = concatenar_cadenas("Hola, ", "mundo!")
    if resultado_prueba_1 != "Hola, mundo!":
        print(f"Error en la prueba 1: Se esperaba 'Hola, mundo!' pero se obtuvo '{resultado_prueba_1}'")

    # Prueba 2: Cadena vacía
    resultado_prueba_2 = concatenar_cadenas("", "Python")
    if resultado_prueba_2 != "Python":
        print(f"Error en la prueba 2: Se esperaba 'Python' pero se obtuvo '{resultado_prueba_2}'")

    # Prueba 3: Cadenas vacías
    resultado_prueba_3 = concatenar_cadenas("", "")
    if resultado_prueba_3 != "":
        print(f"Error en la prueba 3: Se esperaba una cadena vacía pero se obtuvo '{resultado_prueba_3}'")

    # Verificar si alguna prueba falló
    if (
        resultado_prueba_1 == "Hola, mundo!" and
        resultado_prueba_2 == "Python" and
        resultado_prueba_3 == ""
    ):
        print("Todas las pruebas han pasado con éxito")

realizar_pruebas_concatenacion()
