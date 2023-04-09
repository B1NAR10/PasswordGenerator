import random
import string
import gettext

numero_caracteres = int(input("Introduzca Cantos Caracteres quere que teña: "))

minusculas  = string.ascii_lowercase
maiusculas  = string.ascii_uppercase
numeros     = string.digits
simbolos    = string.punctuation
caracteres  = minusculas + maiusculas + numeros + simbolos

xerador     = random.sample(caracteres, numero_caracteres)
print("Contrasinal: " + "".join(xerador))
