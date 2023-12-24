#ir comentando de a uno las pruebas de unittest

# Función que valida un formulario simple
def validar_formulario(nombre, edad):
    if not nombre:
        return print("El nombre no puede estar vacío")
    elif not isinstance(edad, int) or edad <= 0:
        return print("La edad debe ser un número entero positivo")
    elif edad < 18:
        return print("Debes ser mayor de 18 años")
    else:
        return print("Formulario válido")

    # Prueba 1: Nombre vacío
resultado_prueba_1 = validar_formulario("", 25)
if resultado_prueba_1 != "El nombre no puede estar vacío":
  print(f"Fallo en la prueba 1: {resultado_prueba_1}")

    # Prueba 2: Edad no entera
resultado_prueba_2 = validar_formulario("Juan", "veinte")
if resultado_prueba_2 != "La edad debe ser un número entero positivo":
  print(f"Fallo en la prueba 2: {resultado_prueba_2}")

    # Prueba 3: Edad menor de 18 años
resultado_prueba_3 = validar_formulario("Ana", 16)
if resultado_prueba_3 != "Debes ser mayor de 18 años":
  print(f"Fallo en la prueba 3: {resultado_prueba_3}")

    # Prueba 4: Formulario válido
resultado_prueba_4 = validar_formulario("Carlos", 30)
if resultado_prueba_4 != "Formulario válido":
  print(f"Fallo en la prueba 4: {resultado_prueba_4}")
