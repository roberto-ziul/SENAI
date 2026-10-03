# Biblioteca Pandas
import pandas as pd

# Criando um DataFrame manualmente com um dicionário
dados = {
    "Produto": ["Notebook", "Mouse", "Teclado", "Monitor", "Impressora"],
    "Preco": [4500.00, 150.00, 250.00, 1200, None],
    "Estoque": [5, 20, 15, 8, 40]
}
df = pd.DataFrame(dados)
display(df)
