from Cadastro import cereais
from Cadastro import bebidas
from Cadastro import frios
from Cadastro import higiene
from Cadastro import limpeza

operador_caixa = input('Operador: ')

print('Iniciando venda')

cod_inicial = int(input('Digite o código de inicialização do caixa: '))

if cod_inicial == 123456:

    cod_produto = int(input('Digite qualquer número maior que 0 pra começar: '))

    soma_venda = 0
    while cod_produto != 0:

        # testa se é um cereal e faz a soma caso True
        if cod_produto > 110 and cod_produto < 114: # Se for maior que 110 e menor que 114 é um cereal
            for i in range (0, 3): # percorre as colunas, na linha 1 da matriz
                if cod_produto == cereais[2][i]:
                    print(f'Produto: {cereais[0][i]}')
                    print(f'Valor unit: R${cereais[1][i]}')
                    total = cereais[1][i] * quantidade
                    print(f'Valor total: R${total:.2f}')
                    soma_venda = soma_venda + total

        # testa se é uma bebida e faz a soma caso True
        elif cod_produto > 120 and cod_produto < 124:
            for i in range (0, 3):
                if cod_produto == bebidas[2][i]:
                    print(f'Produto: {bebidas [0][i]}')
                    print(f'Valor unit: R${bebidas [1][i]}')
                    total = bebidas[1][i] * quantidade
                    print(f'Valor total: R${total:.2f}')
                    soma_venda = soma_venda + total

        # testa se é um frio e faz a soma caso True
        elif cod_produto > 130 and cod_produto < 134:
            for i in range (0, 3):
                if cod_produto == frios[2][i]:
                    print(f'Produto: {frios [0][i]}')
                    print(f'Valor unit: R${frios[1][i]}')
                    total = frios[1][i] * quantidade
                    print(f'Valor total: R${total:.2f}')
                    soma_venda = soma_venda + total

        # testa se é uma higiene e faz a soma caso True
        elif cod_produto > 140 and cod_produto < 144:
            for i in range (0, 3):
                if cod_produto == higiene[2][i]:
                    print(f'Produto: {higiene [0][i]}')
                    print(f'Valor unit: R${higiene[1][i]}')
                    total = higiene[1][i] * quantidade
                    print(f'Valor total: R${total:.2f}')
                    soma_venda = soma_venda + total

        # testa se é uma limpeza e faz a soma caso True
        elif cod_produto > 150 and cod_produto < 154:
            for i in range (0, 3):
                if cod_produto == limpeza[2][i]:
                    print(f'Produto: {limpeza [0][i]}')
                    print(f'Valor unit: R${limpeza[1][i]}')
                    total = limpeza[1][i] * quantidade
                    print(f'Valor total: R${total:.2f}')
                    soma_venda = soma_venda + total


        else:
            print('Código não encontrado! tente novamente!')

        cod_produto = int(input('Cód Produto: '))
        quantidade = int(input('Quantidade: '))

    print(f'Total da compra = R$ {soma_venda:.2f}')

else:
    print('Código inválido!')

