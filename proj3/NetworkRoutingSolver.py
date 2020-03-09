#!/usr/bin/python3


from proj3.CS4412Graph import *
from proj3.arrays import binary_heap, unsorted_array
import time


class NetworkRoutingSolver:

    def __init__(self):
        inf = float("inf")
        pass

    def initializeNetwork(self, network):
        assert (type(network) == CS4412Graph)
        self.network = network
        nodes = self.network.nodes
        self.dist = [float("inf")] * len(nodes)
        self.prev = [None] * len(nodes)

    # given a destination, look at the distance structure and reconstruct the path from the source to the given
    # destination.
    def getShortestPath(self, destIndex):
        self.dest = destIndex
        # TODO: RETURN THE SHORTEST PATH FOR destIndex
        #       INSTEAD OF THE DUMMY SET OF EDGES BELOW
        #       IT'S JUST AN EXAMPLE OF THE FORMAT YOU'LL 
        #       NEED TO USE
        path_edges = []
        total_length = 0

        path = []
        src = self.prev[destIndex]
        dest = destIndex
        if self.dist[dest] == float("inf"):
            return {'cost': 'unreachable', 'path': path_edges}
        while src is not None:
            for edge in self.network.nodes[src].neighbors:
                if dest == edge.dest.node_id:
                    path.insert(0, edge)
                    dest = src
                    src = self.prev[src]
        for edge in path:
            path_edges.append((edge.src.loc, edge.dest.loc, '{:.0f}'.format(edge.length)))
            total_length += edge.length

        return {'cost': total_length, 'path': path_edges}

    # This function is running Dijkstras. The result is a dist data structure that has the cost of the shortest path
    # from every node. THat's why the source is given as a parameter. This does not actually create paths.
    def computeShortestPaths(self, srcIndex, use_heap=False):

        self.dist[srcIndex] = 0
        nodes = self.network.nodes
        if use_heap:
            pq = binary_heap(self.dist, srcIndex)
        else:
            pq = unsorted_array(self.dist, srcIndex)

        t1 = time.time()

        while not pq.is_empty():
            curr = pq.delete_min()
            for edge in nodes[curr].neighbors:
                next_id = edge.dest.node_id
                new_weight = self.dist[curr] + edge.length

                # if not pq.still_contains(next_id):
                #     continue
                if self.dist[next_id] > new_weight:
                    self.dist[next_id] = new_weight
                    self.prev[next_id] = curr
                    pq.decrease_key(next_id, new_weight)

        t2 = time.time()
        return t2 - t1
