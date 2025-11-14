#Obtendo a matriz de adjacências do grafo não dirigido
matriz_adj_nao_direcionado = nx.adjacency_matrix(grafo_nao_direcionado).todense()

#Imprimindo a matriz de adjacências do grafo não dirigido
print("Matriz de adjacências do grafo não dirigido:")
print(matriz_adj_nao_direcionado)