import time
v1 = int(input('me informe o primeiro valor: '))
v2 = int(input('me informe o segundo valor: '))
print('MENU:\n[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair')
comando = str(input('Me informe o que deseja realizar: '))
while comando != '5':
    if comando == '1':
        print(v1 + v2)
        print('======' * 15)
        time.sleep(2)
        print('MENU:\n[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair')
        comando = str(input('Me informe o que deseja realizar: '))
    if comando == '2':
        print(v1 * v2)
        print('=====' * 15)
        time.sleep(2)
        print('MENU:\n[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair')
        comando = str(input('Me informe o que deseja realizar: '))
    if comando == '3':
        if v1 > v2:
            print(v1)
            print('=====' * 15)
            time.sleep(2)
            print('MENU:\n[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair')
            comando = str(input('Me informe o que deseja realizar: '))
        elif v1 == v2:
            print('iguais.')
            print('=====' * 15)
            time.sleep(2)
            print('MENU:\n[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair')
            comando = str(input('Me informe o que deseja realizar: '))
        else:
            print(v2)
            print('=====' * 15)
            time.sleep(2)
            print('MENU:\n[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair')
            comando = str(input('Me informe o que deseja realizar: '))
    if comando == '4':
        v1 = int(input('digite o novo valor: '))
        v2 = int(input('digite o novo valor: '))
        print('=====' * 15)
        time.sleep(2)
        print('MENU:\n[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair')
        comando = str(input('Me informe o que deseja realizar: '))
