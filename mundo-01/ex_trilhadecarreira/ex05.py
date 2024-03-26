valor = float(input('Digite o valor de venda do produto: '))
quantidade = int(input('Número de produtos vendidos: '))
moeda = input('Moeda em que foi realizada a venda: ').lower()
while moeda != 'dolar' or moeda != 'euro' or moeda != 'real':
        if moeda == 'dolar' or moeda == 'euro' or moeda == 'real':
             break
        moeda = input('Moeda invalida, digite novamente (Moedas em que trabalhamos: Dolar, Real ou Euro): ').lower
desconto = float(input('Digite um valor de desconto, apenas números (exemplo 10%: 10): '))

def  calculo_venda(valor, quantidade, moeda='real', desconto=0):
    if moeda == 'dolar':
        convertValor = valor * 5.00
    if moeda == 'euro':
        convertValor = valor * 5.70
    if moeda == 'real':
        convertValor = valor
    valorFinal = convertValor * quantidade
    if desconto != 0:
         valorFinal = valorFinal * desconto / 100
    return f'{convertValor}, {quantidade} e vendida em {moeda.capitalize()} , {valorFinal}'
    
print(calculo_venda(valor, quantidade, moeda))
