import random, time
computador=random.randint(0,2)
escolha=int(input('''==== JOKENPÔ ====
[0] Pedra
[1] Papel 
[2] Tesoura
ESCOLHA UMA DAS OPÇÕES: '''))
print('Computador escolhendo também...')
time.sleep(2)
print('\033[2:33mVamos lá')
print('Você:', 'Pedra' if escolha == 0 else '' or 'Papel' if escolha == 1 else '' or 'Tesoura' if escolha ==2 else '')
print('Computador:', 'Pedra' if computador == 0 else '' or 'Papel' if computador == 1 else '' or 'Tesoura'if computador == 2 else '' )
print('\033[m')
time.sleep(1)

if escolha == 1 and computador == 0 :
    print('Você Venceu!')
elif escolha == 0 and computador == 1 :
    print('Você Perdeu!')
elif escolha == 2 and computador == 1 :
    print('Você Venceu!')
elif escolha == 1 and computador == 2 :
    print('Você Perdeu!')
elif escolha == 0 and computador == 2 :
    print('Você Venceu!')
elif escolha == 2 and computador == 0 :
    print('Você Perdeu')
elif escolha == computador :
    if escolha == 0:
        print('Os dois escolheram PEDRA, tente novamente!')
    if escolha == 1:
        print('Os dois escolheram PAPEL, tente novamente!')
    if escolha == 2:
        print('Os dois escolheram TESOURA, tente novamente!')
