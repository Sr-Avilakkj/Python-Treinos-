from random import randint

soma = 0
chutes = 0
numero_sorteado = 0

def menu():
    num = int(input('— Digite um numero inteiro entre 1 e 100: '))
    return num

while True:
    num = menu()
    
    if num < 1 or num > 100:
        print('– O numero escolhido é invalido. Escolha um numero inteiro entre 1 e 100')
        
    else:
        while num != numero_sorteado:
            numero_sorteado = randint(1, 100)
            print(numero_sorteado)
            soma += numero_sorteado
            chutes += 1
        media = soma / chutes
        print(f'•Foram necessários {chutes} chutes \n•A soma deles é igual a {soma} \n•E a sua média é igual a {media}')
    break