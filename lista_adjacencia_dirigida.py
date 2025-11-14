#Imprimindo a lista de adjacências do grafo dirigido
print('Lista de adjacência do grafo dirigido')

for node in grafo_direcionado.nodes():
  sucessores = list(grafo_direcionado.successors(node))
  predecessores = list(grafo_direcionado.predecessors(node))
  print(f'Vértice {node}, sucessores: {sucessores} | predecessores {predecessores}')