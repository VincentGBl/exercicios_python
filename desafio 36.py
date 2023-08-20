vc = float(input('qual o valor da casa que o senhor quer comprar?: '))
sal = float(input('qual é o seu salário mensal?: '))
anos = float(input('em quantos anos você pretende pagar a casa?: ')) * 12
din = vc / anos
if din > (sal * 0.30):
    print('-------' * 30)
    print(f'a prestação excedeu 30% do seu salário por mês,pedido negado.')
    print('----Pedido Analisado----')
else:
    print('---' * 30)
    print(f'Empréstimo aprovado!!!!\n seu empréstimo saira a R${din:.2f} Reais por mês')
