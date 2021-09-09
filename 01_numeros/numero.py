import random

def elegirNumeroDel1Al100():
    return random.randint(1, 100)

def pedirNumero():
    print('Escribí un número del 1 al 100:')
    return int(input())

def decirAcertaste():
    print('Acertaste')

def decirMasBajo():
    print('Es más bajo')

def decirMasAlto():
    print('Es más alto')

numeroElegido = elegirNumeroDel1Al100()
numeroLeido = None

while numeroElegido != numeroLeido:
    numeroLeido = pedirNumero()

    if numeroElegido == numeroLeido:
        decirAcertaste()
    elif numeroElegido < numeroLeido:
        decirMasBajo()
    else:
        decirMasAlto()    
        