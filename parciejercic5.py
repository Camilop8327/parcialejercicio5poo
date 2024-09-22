#Ejercicio 5
def verificacion_valor(valor):
    if valor is None:
        print(f"el valor no esta asignado (es None). ")
    else:
        print(f"el valor es: {valor}")

verificacion_valor(None)

verificacion_valor(22)