print('Bem vindo a lanchonete do Allan Figueiredo')
print('********** Opções de lanches ********** ')
print('| Código |      Descrição         |   Valor |')
print('|   100  |    Cachorro-Quente     | R$ 9.00 |')
print('|   101  |  Cachorro-Quente Duplo | R$ 11.00|')
print('|   102  |        X-Egg           | R$ 12.00|')
print('|   103  |       X-Salada         | R$ 13.00|')
print('|   104  |        X-Bacon         | R$ 14.00|')
print('|   105  |         X-Tudo         | R$ 17.00|')
print('|   200  |    Refrigerante Lata   | R$ 5.00 |')
print('|   201  |       Chá Gelado       |  R$ 4.00|')
subtotal=0
while True:
    codigo=input(' Entre com o código do lanche: ')
    if codigo == '100':
        subtotal=subtotal + 9
    elif codigo == '101':
        subtotal = subtotal + 11
    elif codigo == '102':
        subtotal = subtotal + 12
    elif codigo == '103':
        subtotal = subtotal + 13
    elif codigo == '104':
        subtotal = subtotal + 14
    elif codigo == '105':
        subtotal = subtotal + 17
    elif codigo == '200':
        subtotal = subtotal + 5
    elif codigo == '201':
        subtotal = subtotal + 4
    else:
        print(' Digite o código corretamente ')
        continue
    print('O valor a ser pago está em {:.2f}'.format(subtotal))
    resposta = input(' Deseja comprar mais algo? (s/n)')
    if resposta =='s':
       continue
    else:
        print('O valor final da conta é: {:.2f}'.format(subtotal))
        break

