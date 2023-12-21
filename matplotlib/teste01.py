import matplotlib.pyplot as plt

# Dados de exemplo
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Criando um gráfico de dispersão
plt.scatter(x, y)

# Adicionando rótulos e título
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Gráfico de Dispersão Simples')

# Exibindo o gráfico
plt.show()
