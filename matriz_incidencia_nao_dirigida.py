#Imprimindo matriz de incidências do grafo não dirigido
print('Matriz de incidência do grafo não dirigido')

matriz_incidencia_nao_direcionada = nx.incidence_matrix(grafo_nao_direcionado, oriented=False).todense()
print(matriz_incidencia_nao_direcionada)