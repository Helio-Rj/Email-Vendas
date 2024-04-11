import pandas as pd

# Importar base de Dados (database)
tabela_vendas = pd.read_excel('Vendas.xlsx')

#  Visualização de Database
pd.set_option('display.max_columns', None) # Exibir sem restrições todas as colunas da base de dados
print(tabela_vendas)

#  Faturamento por Loja

#  Quantidade de produtos vendidos por Loja

#  ‘Ticket’ médio de produtos vendidos por Loja

#  Envio de Email com Relatório
