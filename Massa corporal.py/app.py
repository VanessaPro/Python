peso=float(input("Qual é o seu peso?(KG)"))
altura=float(input("Qual é a sua altura"))
imc = peso/ (altura ** 2)
print(" O IMC desta pessoa é de {:.1f}".format(imc))
if imc<18.5:
    print("Você está abaixo do peso normal")
elif imc>=18.5 and imc <25:
   print("Seu peso está ideal")
elif imc >=25 and imc <30:
    print("Você está em sobrepeso")

elif 30<= imc <40:
    print("Você está em obesidade, cuidado!")
elif imc>=40:
    print("Você está em obesidade morbida, cuidado!")