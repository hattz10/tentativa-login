login = "admin"
senha = "admin"
tentativas = 0
print("Seja bem vindo")

acesso = int(input("Você já é cadastrado? Digite: \n1 - SIM \n2 - NÃO \n"))

if acesso == 1:
    while tentativas < 3:
        login = str(input("Digite seu login: \n"))
        senha = input("Digite sua senha: \n")
        if login == "admin" and senha == "admin":
            print("Seja bem vindo %s" %{login})
            break
        elif login != "admin" or senha != "admin":
            print("Login ou senha incorretas, tente novamente")
            tentativas = tentativas +1
    else:
        print("Tentativas excedidas")
elif acesso == 2:
    newlogin = input("Crie seu login: \n")
    newsenha = input("Crie sua senha: \n")
    while tentativas < 3:
        login = str(input("Digite seu login: \n"))
        senha = input("Digite sua senha: \n")

        if login == newlogin and senha == newsenha:
            print("Seja bem vindo {}".format(login))
            break
        elif login != "admin" or senha != "admin":
            print("Login ou senha incorretas, tente novamente")
            tentativas = tentativas +1
    else:
        print("Tentativas excedidas")