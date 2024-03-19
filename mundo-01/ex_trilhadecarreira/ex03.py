salario = float(input("Digite o seu salário: "))
if salario >= 4664.68:
    print(f"Para sua faixa de renda a aliquota é de 27,5% e a dedução é de R$869,36!")
elif salario >= 3751.06:
    print(f"Para sua faixa de renda a aliquota é de 22,5% e a dedução é de R$636,13!")
elif salario >= 2826.66:
    print(f"Para sua faixa de renda a aliquota é de 15% e a dedução é de R$354,80!")
elif salario >= 1903.99:
    print(f"Para sua faixa de renda a aliquota é de 7,5% e a dedução é de R$142,80!")
elif salario < 1903.99:
    print(f"Você está isento de pagar Imposto sobre a Renda")