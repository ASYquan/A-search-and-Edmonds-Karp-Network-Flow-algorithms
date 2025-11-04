# pylint: disable=trailing-whitespace
import numpy as np
from typing import List

class Flow:
    def __init__(self, array: np.ndarray) -> None:
        self.array = array
        self.max_flow = 0
        self.cut = []
        self.flow_matrix = np.zeros_like(array)
        self.source = None
        self.sink = None 
        self.visited = None
        
    def find_source_sink(self) -> None:
        """
        A help-method which finds source and sink in our solve-method, since
        there is none given from the assignment
        """
        array = self.array
        # Sum of flows on incoming edges for each node
        incoming_flow = array.sum(axis=0)
        # Sum of flows on outgoing edges for each node
        outgoing_flow = array.sum(axis=1)
        source_candidates = np.where(incoming_flow == 0)[0]
        
        # Sink node has no outgoing flow, hence outgoing_flow[sink] == 0
        sink_candidates = np.where(outgoing_flow == 0)[0]
        
        # Might be multiple source or sink candidates,
        # so additional logic might be needed to choose the correct one.
        # For simplicity, we assume the first one is chosen.
        
        self.source = source_candidates[0] if source_candidates.size > 0 else None
        self.sink = sink_candidates[0] if sink_candidates.size > 0 else None

    def BFS(self, source: int, sink: int, parent: list) -> bool:
        """
        A help-method for solve-method which is an
        implementation of BFS for Ford-Fulkerson algorithm (proposal 2)
        """
        # Mark all the vertices as not visited
        visited = [False]*(self.array.shape[0]) 

        queue = []
 
        queue.append(source)
        visited[source] = True
    
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.array[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == sink:
                        self.visited = visited
                        return True
        self.visited = visited
        return False
    
    def solve(self) -> int:
        """
        An implementeion of the Ford-Fulkerson algorithm (proposal 2)

        Returns:
            int: The found maximum flow for a network 
        """
        parent = [-1]*(self.array.shape[0])
        self.find_source_sink()
        source = self.source
        sink = self.sink
        max_flow = 0 

        while self.BFS(source, sink, parent) :
            path_flow = float("Inf")
            s = sink # Creating temporary variable which uses value of sink
            while(s !=  source):
                path_flow = min(path_flow, self.array[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow +=  path_flow

            v = sink # Creating temporary variable which uses value of sink
            while(v !=  source):
                u = parent[v]
                self.array[u][v] -= path_flow
                self.array[v][u] += path_flow
                v = parent[v]
            
        self.max_flow = max_flow
        return max_flow

    def get_cut(self) -> List[int]:
        """A method which finds the cut for a given Graph

        Returns:
            List[int]: List of all the nodes that are reachable from the source in the residual graph.
        """
        # Implement logic to find the cut
        # Update self.cut
        cut_edges = [i for i, reached in enumerate(self.visited) if reached]
        return cut_edges
        

    
"""if __name__ == "__main__":
    def read_graph_from_file(file_path: str) -> np.ndarray:
        with open(file_path, "r") as f:
            N = int(f.readline().strip())
            graph = np.zeros((N, N), dtype=int)
            for i in range(N):
                graph[i] = list(map(int, f.readline().strip().split()))
        return graph
    
    def test_flow_case1():
        graph = read_graph_from_file("/mnt/e/IN3130/IN3110_oblig2/oblig2/src/test/resources/assignment/testcase1.txt")
        print(graph)
        flow_solver = Flow(graph)
        max_flow = flow_solver.solve()
        assert max_flow == 24
        assert flow_solver.get_cut() == [0, 2]
    test_flow_case1()"""
   
         