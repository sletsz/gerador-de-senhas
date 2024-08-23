import random
import string

def entrada_de_dados():
    senha = input(str("Deseja gerar uma nova senha(sim/nao): "))
    senha = senha.upper()
    if (senha == 'S') or (senha == 'SIM'):
        tamanho = int(input('Quantos caracteres você deseja: '))
    else:
        tamanho = 0
    return tamanho

def gerador_de_senhas(tamanho_da_senha):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(tamanho_da_senha))
    return password
        
def salvar_senha(password, filename="senhas.txt"):
    with open(filename, "a") as file:  # "a" para append, não sobrescreve o arquivo
        file.write(password + "\n")

def senhas_anteriores(filename="senhas.txt"):
    try:
        with open(filename, "r") as file:
            passwords = file.readlines()
            return [password.strip() for password in passwords]
    except FileNotFoundError:
        return []
