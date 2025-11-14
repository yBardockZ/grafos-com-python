#Imprimindo a lista de adjacências do grafo não dirigido
print('Lista de Adjacência do Grafo não direcionado:')

for node in grafo_nao_direcionado.nodes():
  vizinhos = list(grafo_nao_direcionado.neighbors(node))
  print(f'Vértice {node} vizinhos: {vizinhos}')