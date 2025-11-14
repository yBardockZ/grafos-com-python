import networkx as nx
import matplotlib.pyplot as plt
import random

#Criando um grafo dirigido
grafo_direcionado = nx.DiGraph()

#Adicionado 5 vértices aos grafos
num_vertices = 5
grafo_direcionado.add_nodes_from(range(num_vertices))

#Adicionado 10 arestas com rótulos e pesos ao grafo não dirigido
num_arestas = 10
arestas_adicionadas = 0
while arestas_adicionadas < num_arestas:
  vertice_origem = random.randint(0, num_vertices - 1)
  vertice_destino = random.randint(0, num_vertices - 1)

  #Verificando se não é um laço e se a aresta já existe
  if vertice_origem != vertice_destino and not grafo_direcionado.has_edge(vertice_origem, vertice_destino):
    peso = random.randint(0, 10)
    grafo_direcionado.add_edge(vertice_origem, vertice_destino, weight=peso)
    grafo_direcionado[vertice_origem][vertice_destino]['label'] = f'Peso: {peso}'
    arestas_adicionadas += 1
  
#Imprimindo o grafo dirigido:
print('Grafo não dirigido:')
print(grafo_direcionado.edges(data=True))

#Desenhando o grafo dirigido:
plt.figure(figsize=(6, 6))
pos = nx.spring_layout(grafo_direcionado)
nx.draw_networkx(grafo_direcionado, pos, with_labels=True, node_color='skyblue', font_weight='bold')
edge_labels = nx.get_edge_attributes(grafo_direcionado, 'label')
nx.draw_networkx_edge_labels(grafo_direcionado, pos, edge_labels=edge_labels)
plt.title('Grafo direcionado')
plt.axis('off')
plt.show()