def converter_mes_para_extenso(data):
    mes = '''janeiro fevereiro março abril maio junho julho agosto setembro outubro dezembro'''.split()
    d, m, a = data.split('/')
    mes_extenso = mes[int(m) - 1]
    return f'{d} de {mes_extenso} de {a}'

date = input('Digite um data que deseja converter no formato (dd/mm/aaaa): ')
print(converter_mes_para_extenso(date))

