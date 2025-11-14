#Imprimindo matriz de incidências do grafo dirigido
print('Matriz de incidência do grafo dirigido')

matriz_incidencia_direcionada = nx.incidence_matrix(grafo_direcionado, oriented=True).todense()
print(matriz_incidencia_direcionada)