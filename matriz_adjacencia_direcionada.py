#Obtendo a matriz de adjacências do grafo dirigido
matriz_adj_direcionado = nx.adjacency_matrix(grafo_direcionado).todense()

#Imprimindo a mtriz de adjacências do grafo não dirigido
print('Matriz de adjacências do grafo dirigido:')
print(matriz_adj_direcionado)