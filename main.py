'''
Ideia de um semaforo simples, feito em Lingaugem Python, isso só mostra a variedade de coisas que podem
ser feitas em programação.;
'''

#imports
import time

#valor semaforo
semaforo1 = 30
semaforo2 = 30


sinal_aberto = True

#semaforo 1
print('A via da direita está com o semaforo na cor verde, por favor aguarde...')
while sinal_aberto == True:
    for cont in range(semaforo1, -1, -1):
        time.sleep(0.3)
        print(cont)
        if cont == 3:
            print('Sinal verde, pode continuar ,boa viagem.')
            time.sleep(2)
        elif cont == 2:
            print('Sinal amarelo, desacelere ou passe se der tempo, atenção!!')
            time.sleep(2)
        elif cont == 1:
            sinal_aberto = False
            print('Sinal Fechou, desacelere e pare o veiculo')

time.sleep(1)
print('O sinal da via esquerda abriu, por favor espere!')

#Semaforo 2
sinal_aberto = True
while sinal_aberto == True:
    for cont in range(semaforo2, -1, -1):
        time.sleep(0.3)
        print(cont)
        if cont == 3:
            print('Sinal verde, pode continuar ,boa viagem.')
            time.sleep(2)
        elif cont == 2:
            print('Sinal amarelo, desacelere ou passe se der tempo, atenção!!')
            time.sleep(2)
        elif cont == 1:
            sinal_aberto = False
            print('Sinal Fechou, desacelere e pare o veiculo...')

#Semaforo 3
print('Chegou sua vez! Ta vendo? sua paciencia evitou muitos acidentes, parabéns!')



