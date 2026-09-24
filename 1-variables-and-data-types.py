"""
--------------------------- VARIABLES / TIPOS DE DATOS ---------------------------
En este taller aprenderás cómo crear variables, trabajar con diferentes tipos de datos.
"""

"""
--- Ejercicio 1 Variables---
Crea una variable llamada "mensaje". 
Asígnale el valor "¡Hola, Mundo!". 
Imprime el valor de la variable en la consola.
"""
# Escribe tu código aquí

mensaje = "¡Hola, Mundo!"

print(mensaje)


"""
--- Ejercicio 2 Variables---
Invoca la variable anterior llamada "mensaje". 
Reasígnale el valor "Hello world!". 
Imprime el valor de la variable en la consola.
Escribe en un comentario de línea lo que sucede.
"""
# Escribe tu código aquí
mensaje = "Hello world!" # La variable cambia su valor anterior por el nuevo.

print(mensaje)

"""
--- Ejercicio 3 Tipos de datos---
Crea variables para cada uno de los siguientes tipos de datos y colecciones: string, int, float, 
bool, list, tuple, dicctionary and set. 
Imprime cada variable y el tipo de dato o colección que almacena en la consola.
"""
# Escribe tu código aquí

text = "Hello world!"
number = 10
decimal = 10.5
boolean = True
my_list = ["apple", "banana", "orange"]
my_tuple = ("red", "green", "blue")
my_dictionary = {"name": "John", "age": 25}
my_set = {"cat", "dog", "bird"}

print(text, type(text))
print(number, type(number))
print(decimal, type(decimal))
print(boolean, type(boolean))
print(my_list, type(my_list))
print(my_tuple, type(my_tuple))
print(my_dictionary, type(my_dictionary))
print(my_set, type(my_set))