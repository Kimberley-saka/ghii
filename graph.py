"""
Weighted graph
"""
from typing import List, Dict
import sys
from heapq import heapify, heappush


class WeightedGraph:
    """
    Creates a weighted graph
    """

    def __init__(self) -> None:
        self.adjancent_list = {}
        self.vertex = []  # keep track of vertices in graph

    def add_vertex(self, vertex: str) -> None:
        """
        adds vertices
        """
        if vertex not in self.vertex:
            self.vertex.append(vertex)

        else:
            print(f'vertex, {vertex} already exists')

    def add_edge(self, vertex1: str, vertex2: str, weight: int) -> None:
        """
        Adds edges to adjacent list given the graphs vertices and weight
        """
        temp = {}
        if vertex1 in self.vertex and vertex2 in self.vertex:
            if vertex1 not in self.adjancent_list:
                temp = {vertex2: weight}
                self.adjancent_list[vertex1] = temp

            elif vertex1 in self.adjancent_list:
                temp = {vertex2: weight}
                self.adjancent_list[vertex1].update(temp)

        else:
            print('vertex doesnt exist')


def shortest_path(graph: Dict[str, Dict[str, int]], src: str, dest: str) -> None:
    """
    Finds the shortest path from one vertex(district) to another
    in a weighted graph
    """
    infinity = sys.maxsize
    vertex_data = {
        'Mchinji': {'cost': infinity, 'pred': []},
        'Kasungu': {'cost': infinity, 'pred': []},
        'Lilongwe': {'cost': infinity, 'pred': []},
        'Dowa': {'cost': infinity, 'pred': []},
        'Ntchisi': {'cost': infinity, 'pred': []},
        'Nkhotakota': {'cost': infinity, 'pred': []},
        'Salima': {'cost': infinity, 'pred': []},
        'Dedza': {'cost': infinity, 'pred': []},
        'Ntcheu': {'cost': infinity, 'pred': []},
    }

    visited = []
    vertex_data[src]['cost'] = 0
    temp = src

    for _ in range(9):
        if temp not in visited:
            visited.append(temp)

            min_heap = []
            for j in graph[temp]:
                if j not in visited:
                    cost = vertex_data[temp]['cost'] + graph[temp][j]
                    if cost < vertex_data[j]['cost']:
                        vertex_data[j]['cost'] = cost
                        vertex_data[j]['pred'] = vertex_data[temp]['pred'] + [temp]

                    heappush(min_heap, (vertex_data[j]['cost'], j))

        if min_heap:
            heapify(min_heap)
            temp = min_heap[0][1]

    print('Total distance of path:' + str(vertex_data[dest]['cost']))
    print('Shortest path: ' + str(vertex_data[dest]['pred'] + [dest]))
