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
    graph.add_edge('Kasungu', 'Mchinji', 141)
    graph.add_edge('Kasungu', 'Dowa', 117)
    graph.add_edge('Kasungu', 'Ntchisi', 66)
    graph.add_edge('Lilongwe', 'Dowa', 55)
    graph.add_edge('Lilongwe', 'Mchinji', 109)
    graph.add_edge('Lilongwe', 'Dedza', 141)
    graph.add_edge('Dowa', 'Kasungu', 117)
    graph.add_edge('Dowa', 'Ntchisi', 38)
    graph.add_edge('Dowa', 'Lilongwe', 55)
    graph.add_edge('Dowa', 'Salima', 67)
    graph.add_edge('Ntchisi', 'Nkhotakota', 66)
    graph.add_edge('Ntchisi', 'Dowa', 38)
    graph.add_edge('Ntchisi', 'Kasungu', 66)
    graph.add_edge('Nkhotakota', 'Salima', 112)
    graph.add_edge('Nkhotakota', 'Ntchisi', 66)
    graph.add_edge('Salima', 'Dedza', 96)
    graph.add_edge('Salima', 'Dowa', 67)
    graph.add_edge('Salima', 'Nkhotakota', 112)
    graph.add_edge('Dedza', 'Ntcheu', 74)
    graph.add_edge('Dedza', 'Salima', 96)
    graph.add_edge('Dedza', 'Lilongwe', 92)
    graph.add_edge('Ntcheu', 'Dedza', 74)

    #print(graph.adjancent_list)

    print(shortest_path(graph.adjancent_list, 'Mchinji', 'Nkhotakota'))
