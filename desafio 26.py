frase = str(input('fale uma frase com a letra a: ')).upper()
ca = frase.count('A')
cf = frase.find('A') + 1
ua = frase.rfind('A')
print(f'sua frase tem {ca} Letras A,a primeira letra A aparece no caracter de número: {cf} e a usa última aparição é no carácter {ua}')