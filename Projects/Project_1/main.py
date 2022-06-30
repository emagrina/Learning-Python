from random import randint

# Primero preguntaremos su nombre
usuario = input('Escribe tu nombre: ')
print(f'Bienvenido {usuario}\nPiensa un número del 1 al 100, cuidado solo tienes 8 intentos para adivinarlo' )

# Vamos a crear un bucle infinito que solo parara si acertamos el valor o fallamos 8 veces
contador_fallos = 0
acerto_el_valor = False
valor_random = randint(1, 100)

while (contador_fallos < 8 and acerto_el_valor == False ) :
    valor_agregado = int(input(f'Escribe un numero del 1 al 100 ({contador_fallos}/8): '))
    if(valor_agregado <= 100 and valor_agregado >= 1):
        if (valor_agregado == valor_random):
            acerto_el_valor = True
        else:
            contador_fallos += 1
            if(valor_agregado > valor_random):
                print(f'El número correcto es menor de {valor_agregado}')
            elif(valor_agregado < valor_random):
                print(f'El número correcto es mayor de {valor_agregado}')
            elif (contador_fallos == 8):
                print('Lo sentimos ya ha fallado 8 veces')
                print(f'/nLo sentimos, has perdido, el valor correcto era {valor_random}')
    else:
        print('ERROR: Inserte un valor entre el 1 y el 100')

if(acerto_el_valor == True):
    print(f'¡Felicidades {usuario}, acertaste el numero!')