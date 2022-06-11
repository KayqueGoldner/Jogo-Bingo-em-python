import random, time

# CORES
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

print(BOLD+f'\n{10 *" "}JOGO BINGO{10 *" "}\n'+RESET)

# ESCOLHA DA CARTELA DO USUARIO
def esc_jogador():
    print(CYAN+'Digite '+GREEN+"R"+RESET+CYAN+' para números aleatórios!'+RESET)
    print(CYAN+'Digite '+GREEN+"P"+RESET+CYAN+' para personalizar!'+RESET)
    esc_1 = input('\nDESEJA PERSONALIZAR SUA CARTELA? ').upper()
    return esc_1

# CARTELA PERSONALIZADA PELO USÚARIO SENDO CRIADA
cartelaper = []
cartelaper.sort()
def cartela_per():
    try:
        print(GREEN+'------NÃO PODE NÚMEROS REPETIDOS!!!-------'+RESET)
        numeros = int(input('DIGITE UM NÚMERO DE CADA VEZ DE 1 Á 100: '))
    except:
        print(RED+'\nESCOLHA INVÁLIDA!\n'+RESET)
        cartela_per()

    if numeros in cartelaper:
        print(GREEN+'\n------O NÚMERO JÁ EXISTE!!!------'+RESET)
        cartela_per()
    cartelaper.append(numeros)
    if len(cartelaper) < 12:
        print(RED+f'\nFaltam {len(cartelaper) - 12} números'+RESET)
        cartela_per()

# ESCOLHA DO USÚARIO PARA CARTELA ALEATÓRIA OU PERSONALIZADA
esc_1 = esc_jogador()
cont = True
if esc_1 == 'R':
    cartelaran = random.sample(range(0, 101), 12)
    cartelaran.sort()
    cartelaper = cartelaran
    pass
elif esc_1 == 'P':
    print(len(cartelaper))
    if len(cartelaper) < 12:
        cartela_per()
    else:
        pass
else:
    print(RED+'\nESCOLHA INVÁLIDA!'+RESET)
    quit()

cartela = cartelaper
cartela.sort()

# CARTELA DA MAQUINA SENDO CRIADA
cartelarobo = random.sample(range(0, 101), 12)
cartelabot = cartelarobo
cartelabot.sort()

time.sleep(1)
# MOSTRANDO NA TELA A CARTELA DO USÚARIO
print(BLUE+f"""
        CARTELA DO USÚARIO:
            {cartela[0]} - {cartela[1]} - {cartela[2]}
            {cartela[3]} - {cartela[4]} - {cartela[5]}
            {cartela[6]} - {cartela[7]} - {cartela[8]}
            {cartela[9]} - {cartela[10]} - {cartela[11]}
            """,RESET)

# MOSTRANDO NA TELA A CARTELA DA MAQUINA
print(BLUE+f"""
        CARTELA DO ROBÔ:
            {cartelabot[0]} - {cartelabot[1]} - {cartelabot[2]}
            {cartelabot[3]} - {cartelabot[4]} - {cartelabot[5]}
            {cartelabot[6]} - {cartelabot[7]} - {cartelabot[8]}
            {cartelabot[9]} - {cartelabot[10]} - {cartelabot[11]}
            """+RESET)

time.sleep(5)
print(BOLD+'\n________   O JOGO COMEÇOU!  _______\n',RESET)
time.sleep(3)

# GERANDO A LISTA COM NÚMEROS QUE SERÃO SORTEADOS AO DECORRER DO JOGO
lista = random.sample(range(0, 101), 100)
lista.sort()

# VERIFICANDO QUEM SERÁ O VENCEDOR
def ganhou(numero):
    resultado = numero
    if resultado == 1:
        print(GREEN+'\nO USÚARIO GANHOU!'+RESET)
        quit()
    elif resultado == 2:
        print(GREEN+'\nO ROBÔ GANHOU!'+RESET)
        quit()
    # CASO OCORRA UM EMPATE, OS NÚMEROS DA CARTELA SERÃO SOMADOS E O JOGADOR COM MAIOR NÚMERO VENCE
    else:
        print(RED+'O USÚARIO E O ROBÔ COMPLETARAM A CARTELA!\n'+RESET)
        print(RED+'SERÃO SOMADOS TODOS OS NÚMEROS DA CARTELA DOS DOIS E QUAL TIVER O MAIOR VENCE!'+RESET)
        usuario = cartela[0]+cartela[1]+cartela[2]+cartela[3]+cartela[4]+cartela[5]+cartela[6]+cartela[7]+cartela[8]
        robo = cartelabot[0]+cartelabot[1]+cartelabot[2]+cartelabot[3]+cartelabot[4]+cartelabot[5]+cartelabot[6]+cartelabot[7]+cartelabot[8]
        usuario = int(usuario)
        robo = int(robo)
        print(GREEN,f'\nSOMANDO OS NÚMEROS DA CARTELA DO USÚARIO RESULTARAM EM:',usuario,RESET)
        print(GREEN,f'\nSOMANDO OS NÚMEROS DA CARTELA DO ROBÔ USÚARIO RESULTARAM EM:',robo,RESET)
        if usuario > robo:
            print(BLUE,f'\nSENDO ASSIM, O "USUÁRIO" VENCEU! COM A DIFERENÇA DE{usuario - robo} NÚMEROS!',RESET)
            quit()
        else:
            print(BLUE,f'\nSENDO ASSIM, O "ROBÔ" VENCEU! COM A DIFERENÇA DE{robo - usuario} NÚMEROS!',RESET)
            quit()

resultado = 0
conti = True

# PARTE ONDE OCORRE O JOGO EM SI
while conti == True:
    sorteado = random.choice(lista)
    lista.remove(sorteado)
    print(GREEN+'\nO NÚMERO SORTEADO FOI:',RESET, sorteado)
    time.sleep(3)
    for b in range(0, len(cartela)):
        if sorteado == cartela[b]:
            print("\n")
            print(25 * '--')
            print(BOLD+f'\nA CARTELA DO USÚARIO POSSUI O NÚMERO:',RESET+BLUE,sorteado,RESET,'\n')
            print(BOLD+f'\nLETRA X FOI COLOCADO NO NÚMERO'+RESET, GREEN,sorteado,RESET)
            time.sleep(2)
            cartela[b] = 'x'
            print(BLUE,f"""
        CARTELA DO USÚARIO:
            {cartela[0]} - {cartela[1]} - {cartela[2]}
            {cartela[3]} - {cartela[4]} - {cartela[5]}
            {cartela[6]} - {cartela[7]} - {cartela[8]}
            {cartela[9]} - {cartela[10]} - {cartela[11]}
                """, RESET)
            time.sleep(4)

            if cartela[0] == 'x' and cartela[1] == 'x' and cartela[2] == 'x' and cartela[3] == 'x' and \
                    cartela[4] == 'x' and cartela[5] == 'x' and cartela[6] == 'x' and cartela[7] == 'x' and \
                        cartela[8] == 'x' and cartela[9] == 'x' and cartela[10] == 'x' and cartela[11] == 'x':
                            resultado = 1
    for c in range(0, len(cartelabot)):
        if sorteado == cartelabot[c]:
            print("\n")
            print(25 * '--')
            print(BOLD+f'\nA CARTELA DO ROBÔ POSSUI O NÚMERO:',RESET+BLUE,sorteado,RESET,'\n')
            print(BOLD+f'\nLETRA X FOI COLOCADO NO NÚMERO'+RESET, GREEN,sorteado,RESET,'\n')
            time.sleep(2)
            cartelabot[c] = 'x'
            print(BLUE,f"""
        CARTELA DO ROBÔ:
            {cartelabot[0]} - {cartelabot[1]} - {cartelabot[2]}
            {cartelabot[3]} - {cartelabot[4]} - {cartelabot[5]}
            {cartelabot[6]} - {cartelabot[7]} - {cartelabot[8]}
            {cartelabot[9]} - {cartelabot[10]} - {cartelabot[11]}
                """, RESET)
            time.sleep(4)

            if cartelabot[0] == 'x' and cartelabot[1] == 'x' and cartelabot[2] == 'x' and cartelabot[3] == 'x' and \
                    cartelabot[4] == 'x' and cartelabot[5] == 'x' and cartelabot[6] == 'x' and cartelabot[7] == 'x' and \
                        cartelabot[8] == 'x' and cartelabot[9] == 'x' and cartelabot[10] == 'x' and cartelabot[11] == 'x':
                            resultado += 2
    print(25 * '--')
    if resultado > 0:
        ganhou(resultado)
    print(RED+'SORTEANDO OUTRO NÚMERO!'+RESET)
    time.sleep(3)

print('\n')
print(25 * '--')
   
