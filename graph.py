"""
Weighted graph
"""

class WeightedGraph:
    """
    """
    def __init__(self) -> None:
        self.adjancent_list = {}
        self.vertex_list = []
    

    def add_vertex(self, vertex: str) -> None:
        if vertex not in self.vertex_list:
            self.vertex_list.append(vertex)

        print(f'vertex, {vertex} alredy exists')
    
    def add_edge(self, vertex1: str, vertex2: str, weight: int) -> None:
        """
        """


            

    def shortest_path(self):
        pass

"""
    graph = {
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