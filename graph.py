"""
Weighted graph
"""
from typing import List, Dict


class WeightedGraph:
    """
    Creates a weighted graph
    """

    def __init__(self) -> None:
        self.adjancent_list = {}
        self.vertex_list = []  # keep track of vertices in graph

    def add_vertex(self, vertex: str) -> None:
        """
        add vertices
        """
        if vertex not in self.vertex_list:
            self.vertex_list.append(vertex)

        else:
            print(f'vertex, {vertex} already exists')

    def add_edge(self, vertex1: str, vertex2: str, weight: int) -> None:
        """
        Add edge to adjacent list given the graphs vertices and weight
        """
        temp_list = []
        if vertex1 in self.vertex_list and vertex2 in self.vertex_list:
            if vertex1 not in self.adjancent_list:
                temp_list.append([vertex2, weight])
                self.adjancent_list[vertex1] = temp_list

            elif vertex1 in self.adjancent_list:
                temp_list.extend(self.adjancent_list[vertex1])
                temp_list.append([vertex2, weight])
                self.adjancent_list[vertex1] = temp_list

        else:
            print('vertex doesnt exist')


def shortest_path(graph: Dict[str, List[str, int]]) -> List:
    """
    Find the shortest path from one district to another
    in given weighted graph
    """


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

print(graph.adjancent_list)

"""
    test_graph = {
        {'Mchinji': {'kasungu': 141, 'Lilongwe': 109}},
        {'kasungu': {'Mchinji': 141, 'Dowa': 117, 'Ntchisi': 66}},
        {'Lilongwe': {'Dowa': 55, 'Mchinji':109, 'Dedza': 92}},
        {'Dowa': {'Kasungu': 117, 'Ntchisi': 38, 'Lilongwe':55, 'Salima': 67}},
        {'Ntchisi': {'Nkhotakota': 66, 'Dowa': 38, 'Kasungu':66}},
        {'Nkhotakota': {'Salima': 112, 'Ntchisi': 66}},
        {'Salima': {'Dedza': 96, 'Dowa': 67, 'Nkhotakota': 112}}, 
        {'Dedza': {'Ntcheu': 74, 'Salima': 96, 'Lilongwe': 92}},
        {'Ntcheu': {'Dedza': 74}}
    }
"""
