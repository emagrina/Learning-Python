import time
import os
from random import choice

palabras_secretas = ['disciplina', 'profesor', 'deberes', 'programar']
letras_correctas = []
letras_incorrectas = []
numero_intentos = 6
numero_aciertos = 0
juego_terminado = False

def palabra_random(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))

    return palabra_elegida, letras_unicas

def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abc = 'abcdefghijklmnñopqrstuvwxyz'

    while not es_valida:
        letra_elegida = input('Inserte una letra: ').lower()
        if letra_elegida in abc and len(letra_elegida) == 1:
            es_valida = True
        else:
            print('No has insertado una letra, inserte una letra exemplos: a, b, c...')

    return letra_elegida

def mostrar_nuevo_tablero(palabra_elegida):
    global numero_intentos
    match numero_intentos:
        case 6:
            print('\n___________\n|/       \n|       \n|       \n|__________________________')
        case 5:
            print('\n___________\n|/       o\n|       \n|       \n|__________________________')
        case 4:
            print('\n___________\n|/       o\n|       /\n|       \n|__________________________')
        case 3:
            print('\n___________\n|/       o\n|       /|\n|       \n|__________________________')
        case 2:
            print('\n___________\n|/       o\n|       /|\\\n|       \n|__________________________')
        case 1:
            print('\n___________\n|/       o\n|       /|\\\n|       /\n|__________________________')
        case 0:
            print('\n___________\n\t|/       o\n|       /|\\\n|       / \\\n|__________________________')

    lista_oculta = []

    for x in palabra_elegida:
        if x in letras_correctas:
            lista_oculta.append(x)
        else:
            lista_oculta.append('_')

    print(' '.join(lista_oculta))

def validar_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
    fin = False
    if letra_elegida in palabra_oculta:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1

    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)

    return vidas, fin, coincidencias

def perder():
    print('Lo sentimos has perdido')
    print('La palabra oculta era ' + palabra)

    return True

def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print('¡Felicidades, has ganado!')

    return True

print('Bienvenido al juego del ahorcado, agrega letras y adivina la palabra secreta para salvarte.')

palabra, letras_unicas = palabra_random(palabras_secretas)

while not juego_terminado:
    mostrar_nuevo_tablero(palabra)
    print('Letras incorrectas: ' + ' - '.join(letras_incorrectas))
    print(f'Numero de intentos: {numero_intentos}')


    letra = pedir_letra()

    numero_intentos, terminado, numero_aciertos = validar_letra(letra, palabra, numero_intentos, numero_aciertos)

    juego_terminado = terminado

    if juego_terminado is not True:
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')


