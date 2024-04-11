import pandas as pd

# Importar base de Dados (database)
# Linha para ler uma tabela em Excel
tabela_vendas = pd.read_excel('Vendas.xlsx')

# Visualização de Database
# Exibir sem restrições todas as colunas da base de dados
pd.set_option('display.max_columns', None)

# Faturamento por Loja
# Bloco de comando responsavel por Separar as colunas, agurpar itens repetidos e somar os valores
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento)

# Quantidade de produtos vendidos por Loja
# Bloco de comando responsavel por Separar as colunas, agurpar itens repetidos e somar os valores
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(quantidade)

# ‘Ticket’ médio de produtos vendidos por Loja

# Envio de Email com Relatório
