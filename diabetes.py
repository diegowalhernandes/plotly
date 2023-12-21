from dash import Dash, html, dcc
import plotly.express as px

app = Dash(__name__)

# Dados de exemplo
peso = [70, 85, 60, 90, 75, 80]
glicose = [120, 150, 100, 160, 140, 130]
rotulos = [0, 1, 0, 1, 0, 1]  # 0 para sem risco, 1 para em risco

# Criando um DataFrame do Pandas
import pandas as pd
data = pd.DataFrame({'Peso': peso, 'Glicose': glicose, 'Rótulos': rotulos})

# Criando o gráfico de dispersão interativo com Plotly Express
fig = px.scatter(data, x='Peso', y='Glicose', color='Rótulos',
                 color_discrete_map={0: 'blue', 1: 'red'},
                 labels={'Peso': 'Peso', 'Glicose': 'Nível de Glicose', 'Rótulos': 'Diabetes'})

# Adicionando rótulos e título
fig.update_layout(title='Exemplo de Separação de Classes para Previsão de Diabetes',
                  xaxis_title='Peso',
                  yaxis_title='Nível de Glicose')

# Exibindo o gráfico
fig.show()


if __name__ == '__main__':
    app.run_server(debug=True)