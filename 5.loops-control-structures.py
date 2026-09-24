"""
--------------------------- CICLOS Y ESTRUCTURAS DE CONTROL ---------------------------
En este taller aprenderás usar los métodos más típicos para dirigir el flujo de ejecuón y la lógica de un algoritmo
"""

"""
--- Ejercicio 1 condicionales  ---
Escribe un programa que pida al usuario una letra y luego imprima un mensaje indicando si es una vocal o una consonante.
"""
# Escribe tu código aquí

letter = input("Enter a letter: ")

if letter in "aeiouAEIOU":
    print("It is a vowel")
else:
    print("It is a consonant")


"""
--- Ejercicio 2  condicionales anidados  ---
Escribe un programa que pida al usuario una nota (entre 0 y 100) y determine si 
es una calificación de "A", "B", "C", "D" o "F".
"""
# Escribe tu código aquí

grade = int(input("Enter a grade between 0 and 100: "))

if grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
elif grade >= 60:
    print("Grade: D")
else:
    print("Grade: F")

"""
--- Ejercicio 3  bucle while  ---
Escribe un programa que pida al usuario un número entero positivo y 
luego imprima la cuenta regresiva desde ese número hasta 1.
"""
# Escribe tu código aquí

number = int(input("Enter a positive integer: "))

while number >= 1:
    print(number)
    number -= 1

"""
--- Ejercicio 4  bucle for  ---
Escribe un programa que imprima todos los caracteres de una cadena de texto ingresada por el usuario.
"""
# Escribe tu código aquí

text = input("Enter a text string: ")

for character in text:
    print(character)

"""
--- Ejercicio 5  bucle for con range ---
Escribe un programa que imprima la tabla de multiplicar del 5 (del 1 al 10).
"""
# Escribe tu código aquí

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

"""
--- Ejercicio 6  bucle for con listas ---
Escribe un programa que pida al usuario 5 palabras, las guarde en una lista y 
luego en una nueva lista guarde todas las palabras en mayúsculas.
"""
# Escribe tu código aquí

words = []
uppercase_words = []

for i in range(5):
    word = input("Enter a word: ")
    words.append(word)

for word in words:
    uppercase_words.append(word.upper())

print(words)
print(uppercase_words)


"""
--- Ejercicio 7  break and continue ---
Escribe un programa que le pida al usuario una mascota y 
si es un perro, que imprima en la consola "Tengo un perro", 
si es un gato, que imprima en la consola "Tengo un gato", 
si es un pájaro, que imprima en la consola "Tengo un pájaro" y 
si no es ninguno de los 3 que imprima "No tengo una mascota convencional"
"""
# Escribe tu código aquí

pet = input("Introduce una mascota: ")

if pet == "perro":
    print("Tengo un perro")
elif pet == "gato":
    print("Tengo un gato")
elif pet == "pájaro":
    print("Tengo un pájaro")
else:
    print("No tengo una mascota convencional")
