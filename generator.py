import random
import string

# Definir as Mensaxes en diferentes Idiomas
messages = {
    'password_length': {
        'en': 'Enter how many characters you want the Password to be:',
        'es': 'Introduce la longitud deseada de la Contraseña: ',
        'gl': 'Introduce a Lonxitude desexada do Contrasinal: ',
        'ca': 'Introdueix la Longitud desitjada de la Contrasenya: ',
        'eu': 'Sartu Pasahitzaren luzera nahi Duzuna: ',
        'pt': 'Insira o comprimento desejado da Senha: ',
        'fr': 'Entrez la longueur souhaitée du mot de Passe : ',
        'de': 'Geben Sie die gewünschte Länge des Passworts ein: '
    },
    'password': {
        'en': 'Password: ',
        'es': 'Contraseña: ',
        'gl': 'Contrasinal: ',
        'ca': 'Contrasenya: ',
        'eu': 'Pasahitza: ',
        'pt': 'Senha: ',
        'fr': 'Mot de Passe: ',
        'de': 'Passwort: '
    }
}

# Función para obter a traducción dun mensaxe nun idioma determinado
def gettext(message, lang):
    return messages.get(message, {}).get(lang, message)

# Solicitar o Idioma desexado polo Usuario
lang = input('Choose your language (en/es/gl/ca/eu/pt/fr/de): ')

# Solicitar a Lonxitude da Contrasinal ao Usuario
numero_caracteres = int(input(gettext('password_length', lang)))

# Definir os Caracteres que se utilizarán para Xerar a Contrasinal
minusculas  = string.ascii_lowercase
maiusculas  = string.ascii_uppercase
numeros     = string.digits
simbolos    = string.punctuation
caracteres  = minusculas + maiusculas + numeros + simbolos

# Xerar unha Contrasinal Aleatoria
xerador = random.sample(caracteres, numero_caracteres)

# Imprimir a Contrasinal no Idioma Seleccionado
print(gettext('password', lang) + "".join(xerador))
