# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

tempe_hoy = float(input("Ingrese la temperatura máxima pronosticada para hoy:"))
tempe_mña = float(input("Ingrese la temperatura máxima pronosticada para mañana:"))
tempe_pasado = float(input("Ingrese la temperatura máxima pronosticada para pasado mañana:"))

if tempe_hoy != (tempe_mña and tempe_pasado) and (tempe_hoy > tempe_mña and tempe_pasado):
    print("La temperatura pronosticada para hoy es la más alta.")
elif (tempe_mña > tempe_hoy) and (tempe_mña > tempe_pasado):
    print("La temperatura pronosticada para mañana es la más alta.")
elif (tempe_pasado > tempe_hoy) and (tempe_pasado > tempe_mña):
    print("La temperatura pronosticada para pasado mañana es la más alta.")
elif (tempe_hoy == tempe_mña) and (tempe_hoy > tempe_pasado):
    print("La temperatura para hoy y mañana son las más altas.")
elif (tempe_hoy == tempe_pasado) and (tempe_hoy > tempe_mña):
    print("La temperatura para hoy y pasado mañana son las más altas.")
elif (tempe_mña == tempe_pasado) and (tempe_mña > tempe_hoy):
    print("Las temperatura de mañana y pasado mañana son las más altas.")
else:
    print("La temperatura para los tres días es la misma, {} grados.".format(tempe_hoy))

if (tempe_hoy != tempe_mña) and (tempe_hoy != tempe_pasado) and (tempe_hoy < tempe_mña and tempe_pasado):
    print("La temperatura pronosticada para hoy es la más baja.")
elif (tempe_mña < tempe_hoy) and (tempe_mña < tempe_pasado):
    print("La temeperatura pronosticada para mañana es la más baja")
elif (tempe_pasado < tempe_hoy) and (tempe_pasado < tempe_mña):
    print("La temperatura pronosticada para pasado mañana es la más baja.")
elif (tempe_hoy == tempe_mña) and (tempe_hoy < tempe_pasado):
    print("La temperatura para hoy y mañana son las más bajas.")
elif (tempe_hoy == tempe_pasado) and (tempe_hoy < tempe_mña):
    print("La temperatura para hoy y pasado mañana son las más bajas.")
elif (tempe_mña == tempe_pasado) and (tempe_mña < tempe_hoy):
    print("Las temperatura de mañana y pasado mañana son las más bajas.")
else:
    print("La temperatura para los tres días es la misma, {} grados".format(tempe_hoy))

prom = (tempe_pasado + tempe_hoy + tempe_mña) / 3
print("La temperatura promedio de los próximos 3 días será {} grados".format(prom))