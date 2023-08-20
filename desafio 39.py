from datetime import date
atual = date.today().year
idade = int(input('qual foi o ano do seu nascimento?: '))
idadr = atual - idade
if idadr < 18:
    print('você ainda vai se alistar,cuidado em kkkkkkkkkkkk')
elif idadr == 18:
    print('você tem que se alistar,boa sorte kkkkkkkkkkkkkk')
elif idadr > 18:
    print('ja passou do tempo de se alitar animal kkkkkkkkkkkkkkkkkk')