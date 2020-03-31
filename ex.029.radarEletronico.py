velocidade = int(input("Digite a velocidade atual do carro (Km/h): "))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print("Você foi multado em R$ {:.2f}, pois a velocidade da via é de 80Km/h.".format(multa))
print("Tenha um bom dia!! Dirija com segurança!")