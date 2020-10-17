from random import choice
from time import sleep

print('\033[1;31mJokenpô\033[m')
print('Digite: Pedra, Papel ou Tesoura')

escolha = str(input()).lower().strip().capitalize()
while escolha != 'Pedra' and escolha != 'Papel' and escolha != 'Tesoura':
    print('Não entendi, tente novamente.')
    escolha = str(input()).lower().strip().capitalize()

lista = ['Pedra', 'Papel', 'Tesoura']
comp = choice(lista)
print('Eu escolhi...')
sleep(2)

print(comp)
sleep(1)

if escolha == comp:
    print('Empate')
# JOGADOR PERDE
if escolha == 'Papel' and comp == 'Tesoura':
    print('Maquina ganhou!')
elif escolha == 'Tesoura' and comp == 'Pedra':
    print('Maquina ganhou!')
elif escolha == 'Pedra' and comp == 'Papel':
    print('Maquina ganhou!')
# JOGADOR GANHA
if escolha == 'Pedra' and comp == 'Tesoura':
    print('Jogador ganhou!')
elif escolha == 'Papel' and comp == 'Pedra':
    print('Jogador ganhou!')
elif escolha == 'Tesoura' and comp == 'Papel':
    print('Jogador ganhou!')