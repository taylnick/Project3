#!/usr/bin/python3


from proj3.CS4412Graph import *
from proj3.arrays import *
import time


class NetworkRoutingSolver:
    def __init__( self):
        pass

    def initializeNetwork( self, network ):
        assert( type(network) == CS4412Graph )
        self.network = network

# given a destination, look at the distance structure and reconstruct the path from the source to the given destination.
    def getShortestPath( self, destIndex ):
        self.dest = destIndex
        # TODO: RETURN THE SHORTEST PATH FOR destIndex
        #       INSTEAD OF THE DUMMY SET OF EDGES BELOW
        #       IT'S JUST AN EXAMPLE OF THE FORMAT YOU'LL 
        #       NEED TO USE
        path_edges = []
        total_length = 0
        node = self.network.nodes[self.source]
        edges_left = 3
        while edges_left > 0:
            edge = node.neighbors[2]
            path_edges.append( (edge.src.loc, edge.dest.loc, '{:.0f}'.format(edge.length)) )
            total_length += edge.length
            node = edge.dest
            edges_left -= 1
        return {'cost':total_length, 'path':path_edges}

    # This function is running Dijkstras. The result is a dist data structure that has the cost of the shortest path from every node.
    # THat's why the source is given as a parameter.
    # This does not actually create paths.
    def computeShortestPaths( self, srcIndex, use_heap=False ):
        self.source = srcIndex
        t1 = time.time()
        # TODO: RUN DIJKSTRA'S TO DETERMINE SHORTEST PATHS.
        #       ALSO, STORE THE RESULTS FOR THE SUBSEQUENT
        #       CALL TO getShortestPath(dest_index)
        nodes = self.network.nodes
        dist = [float("inf")] * len(nodes)

        if use_heap:
            pq = binary_heap(dist, srcIndex)
        else:
            pq = unsorted_array(dist, srcIndex)

        prev = [None] * len(nodes)

        while not pq.is_empty():
            curr = pq.delete_min()
            for edge in curr.neighbors:
                next_id = edge.dest.node_id
                curr_id = curr.node_id
                new_weight = pq[curr_id] + edge.length
                if pq[next_id] > new_weight:
                    pq[next_id] = new_weight
                    prev[next_id] = curr_id
                    pq.decrease_key(next_id, new_weight)


        t2 = time.time()
        return (t2-t1)

