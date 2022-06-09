import os
import sys
def limpartela():
    os.system('cls')

def mostrarPalavraForca(palavraForca, letrasChutadas):
    for i in range(len(palavraForca)): 
        if (palavraForca[i] in letrasChutadas):
            sys.stdout.write(palavraForca[i])
        else: 
            sys.stdout.write('_')
        sys.stdout.write(' ')