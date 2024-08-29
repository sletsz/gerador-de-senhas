from gerador import gerador_de_senhas, entrada_de_dados, salvar_senha, senhas_anteriores

tamanho = entrada_de_dados() #tamanho da senha
descricao = input(str("Qual a descrição da senha: "))


if tamanho == 0: #senha == 0, o codigo acaba
    pass
else:
    senha = gerador_de_senhas(tamanho) #gera a senha e guarda na variavel "senha"
    
    salvar_senha(senha, descricao) #salva a senha gerada

    senha_salva = senhas_anteriores() #
    for password in senha_salva:
        print(password)