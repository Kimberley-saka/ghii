"""
test file
"""
from graph import WeightedGraph, shortest_path


if __name__ == '__main__':
    
    graph = WeightedGraph()

    graph.add_vertex('Mchinji')
    graph.add_vertex('Kasungu')
    graph.add_vertex('Lilongwe')
    graph.add_vertex('Dowa')
    graph.add_vertex('Ntchisi')
    graph.add_vertex('Nkhotakota')
    graph.add_vertex('Salima')
    graph.add_vertex('Dedza')
    graph.add_vertex('Ntcheu')

    graph.add_edge('Mchinji', 'Kasungu', 141)
    graph.add_edge('Mchinji', 'Lilongwe', 109)
    graph.add_edge()

    print(graph.adjancent_list)
   

    test_graph = {
    'Mchinji': {'Kasungu': 141, 'Lilongwe': 109},
    'Kasungu': {'Mchinji': 141, 'Dowa': 117, 'Ntchisi': 66},
    'Lilongwe': {'Dowa': 55, 'Mchinji':109, 'Dedza': 92},
    'Dowa': {'Kasungu': 117, 'Ntchisi': 38, 'Lilongwe':55, 'Salima': 67},
    'Ntchisi': {'Nkhotakota': 66, 'Dowa': 38, 'Kasungu':66},
    'Nkhotakota': {'Salima': 112, 'Ntchisi': 66},
    'Salima': {'Dedza': 96, 'Dowa': 67, 'Nkhotakota': 112}, 
    'Dedza': {'Ntcheu': 74, 'Salima': 96, 'Lilongwe': 92},
    'Ntcheu': {'Dedza': 74}
    }


    print (shortest_path(graph, 'Mchinji', 'Nkhotakota'))