import matplotlib.pyplot as plt
import numpy as np

# Dados de exemplo
peso = [70, 85, 60, 90, 75, 80]
glicose = [120, 150, 100, 160, 140, 130]
rotulos = [0, 1, 0, 1, 0, 1]  # 0 para sem risco, 1 para em risco

# Dividindo os dados por rótulos
sem_risco = np.array([(peso[i], glicose[i]) for i in range(len(rotulos)) if rotulos[i] == 0])
em_risco = np.array([(peso[i], glicose[i]) for i in range(len(rotulos)) if rotulos[i] == 1])

# Plotando os pontos
plt.scatter(sem_risco[:, 0], sem_risco[:, 1], color='blue', label='Sem Risco')
plt.scatter(em_risco[:, 0], em_risco[:, 1], color='red', label='Em Risco')

# Adicionando rótulos e legendas
plt.xlabel('Peso')
plt.ylabel('Nível de Glicose')
plt.legend()
plt.title('Exemplo de Separação de Classes para Previsão de Diabetes')

# Exibindo o gráfico
plt.show()
