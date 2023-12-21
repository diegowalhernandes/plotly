import plotly.express as px
import seaborn as sns

# Carregando o conjunto de dados de pinguins
df_penguins = sns.load_dataset("penguins")

# Criando o gráfico interativo com Plotly Express
fig = px.scatter(df_penguins, x='flipper_length_mm', y='bill_length_mm', color='species',
                 labels={'flipper_length_mm': 'Comprimento da Nadadeira (mm)',
                         'bill_length_mm': 'Comprimento do Bico (mm)',
                         'species': 'Espécie'})

# Adicionando rótulos e título
fig.update_layout(title='Visualização Interativa das Espécies de Pinguins')

# Exibindo o gráfico
fig.show()
