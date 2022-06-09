from funcoes import limpartela, mostrarPalavraForca

dicas = list
palavraForca = list
letrasChutadas = list
erroContador = int
acertoContador = int
msgMenu = str
desafiante = str
competidor = str
perdedor = str
vencedor = str


def main():
    global desafiante, competidor, perdedor, vencedor

    def startGame():
        global dicas, palavraForca, letrasChutadas, erroContador, acertoContador, msgMenu, desafiante, competidor, perdedor, vencedor

        dicas = []
        palavraForca = []
        letrasChutadas = []
        erroContador = 5
        acertoContador = 0
        msgMenu = 'BEM-VINDO NO JOGA DA FORCA!!'
        desafiante = ''
        competidor = ''
        perdedor = ''
        vencedor = ''

    def palpitar():
        global erroContador, acertoContador, msgMenu
        palpite = str(input('Digite uma letra OU chute a palavra:').upper())
        if len(palpite) > 1:
            if palpite == ''.join(palavraForca):
                acertoContador = len(palavraForca)
                return
            else:
                msgMenu = '{} não é a palavra correta.'.format(palpite)
                erroContador -= 1
                return
        if palpite in letrasChutadas:
            msgMenu = 'Você ja chutou essa letra'
            return
        else:
            letrasChutadas.append(palpite)

        if palpite in palavraForca:
            acertoContador += 1
            msgMenu = 'A letra {} faz parte da palavra!'.format(palpite.upper())
        else:
            erroContador -= 1
            msgMenu = 'A letra {} não faz parte da palavra!'.format(palpite.upper())
        print('\n')
            
    startGame()
    limpartela()
    print('-=-'* 14)
    print('       BEM-VINDO AO JOGO DA FORCA!!  ')
    print('-=-'* 14)
    desafiante = str(input('Digite o nome do desafiante:'))
    competidor = str(input('Digite o nome do competidor:'))
    limpartela()
    palavraForca = list(str(input('DIGITE A PALAVRA DA FORCA!!:').upper()))
    dicas.append(str(input('Primeira dica:').upper()))
    dicas.append(str(input('Segunda dica:').upper()))
    dicas.append(str(input('Terceira dica:').upper()))
    limpartela()
    while acertoContador < len(palavraForca) and erroContador > 0:
        print('Acertos:{}'.format(acertoContador))
        mostrarPalavraForca(palavraForca, letrasChutadas)
        print('\n{}'.format(msgMenu))
        print('Chances restantes:{}'.format(erroContador))
        print('[1] PARA JOGAR!')
        print('[2] PARA PEDIR DICA!')
        opcao = int

        try:
            opcao = int(input('Qual a sua opção:'))
            if opcao == 1:
                limpartela()
                palpitar()
            elif opcao == 2:
                if len(dicas) > 0:
                    limpartela()
                    print(dicas[0])
                    dicas.pop(0)
                if len(dicas) > 0:
                    print('Você so tem mais {} dicas'.format(len(dicas)))
                else:
                    print('Você não tem mais dicas!')
                palpitar()
        except:
            limpartela()
            print('Opção invalida!')
        limpartela()

    if erroContador == 0:
        perdedor = 'Competidor ' + competidor.capitalize()
        vencedor = 'Desafiante ' + desafiante.capitalize()
        print('Você perdeu!!!\n')
    elif acertoContador == len(palavraForca):
        perdedor = 'Desafiante ' + desafiante.capitalize()
        vencedor = 'Competidor ' + competidor.capitalize()
        print('Parabénss!! Você ganhouu!!!\n')
    w = open('historico.txt', 'a')
    w.write('Palavra: {} - Vencedor: {}, Perdedor: {}\n'.format(''.join(palavraForca).capitalize(), vencedor, perdedor))
    w.close()
    r = open('historico.txt', 'r')
    print('-=-'* 14)
    print('     Historico de partidas!')
    print('-=-'* 14)
    print(r.read())
    print('[1] Para jogar novamente!!')
    print('[2] Sair do game\n')
    quitGame = int
    while quitGame != 1 or quitGame != 2: 
        try:
            quitGame = int(input('Qual a sua opção:'))
            if quitGame == 1:
                main()
            elif quitGame == 2:
                break
        except:
            limpartela()
            print('Opção invalida')

main()