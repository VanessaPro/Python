from random import randint
from time import sleep
computador = randint(0,5)
print("-=-" * 10)
print("Vou pensar em um número entre 0 e 5 . Tente advinhar....")
print("-=-"* 10)
jogador=int(input("Em que número pensei?"))
print("Processando.....")
sleep(1)
if jogador==computador:
    print("Parabéns você ganhou!Também pensei no número {}".format(jogador))
else:
    print("Você perdeu! Penseu no número {}".format(computador))