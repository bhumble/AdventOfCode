#!/usr/bin/python3

import re
import math
from collections import defaultdict
import heapq as heap

with open('input.txt', 'r') as f:
    alldata = f.readlines()
    f.close()

def dijkstra(G, startingNode):
    visited = set()
    parentsMap = {}
    pq = []
    nodeCosts = defaultdict(lambda: float('inf'))
    nodeCosts[startingNode] = 0
    heap.heappush(pq, (0, startingNode))
 
    while pq:
        # go greedily by always extending the shorter cost nodes first
        _, node = heap.heappop(pq)
        visited.add(node)
 
        for adjNode, weight in G[node].items():
            if adjNode in visited:  continue
                
            newCost = nodeCosts[node] + weight
            if nodeCosts[adjNode] > newCost:
                parentsMap[adjNode] = node
                nodeCosts[adjNode] = newCost
                heap.heappush(pq, (newCost, adjNode))
        
    return parentsMap, nodeCosts

def name(row, col):
    return str(row) + ',' + str(col)

def print_chitons(chitons):
    for row in chitons:
        print(row)

def part1(data):
    nodes = {}
    chitons = []
    for line in data:
        chiton_line = []
        for char in line.strip():
            chiton_line.append(int(char))
        chitons.append(chiton_line)

    for row in range(len(chitons)):
        for col in range(len(chitons[row])):
            node_name = name(row, col)
            if node_name not in nodes:
                nodes[node_name] = {}
            if row > 0:
                nodes[node_name][name(row - 1, col)] = chitons[row - 1][col]
            if row < len(chitons) - 1:
                nodes[node_name][name(row + 1, col)] = chitons[row + 1][col]
            if col > 0:
                nodes[node_name][name(row, col - 1)] = chitons[row][col - 1]
            if col < len(chitons[row]) - 1:
                nodes[node_name][name(row, col + 1)] = chitons[row][col + 1]

    end_name = name(len(chitons) - 1, len(chitons[0]) - 1)
    return dijkstra(nodes, '0,0')[1][end_name]

def part2(data):
    nodes = {}
    chitons = []
    for i in range(5):
        for line in data:
            chiton_line = []
            for j in range(5):
                for char in line.strip():
                    val = int(char) + i + j
                    if val > 9:
                        val -= 9
                    chiton_line.append(val)
            chitons.append(chiton_line)

    for row in range(len(chitons)):
        for col in range(len(chitons[row])):
            node_name = name(row, col)
            if node_name not in nodes:
                nodes[node_name] = {}
            if row > 0:
                nodes[node_name][name(row - 1, col)] = chitons[row - 1][col]
            if row < len(chitons) - 1:
                nodes[node_name][name(row + 1, col)] = chitons[row + 1][col]
            if col > 0:
                nodes[node_name][name(row, col - 1)] = chitons[row][col - 1]
            if col < len(chitons[row]) - 1:
                nodes[node_name][name(row, col + 1)] = chitons[row][col + 1]

    end_name = name(len(chitons) - 1, len(chitons[0]) - 1)
    return dijkstra(nodes, '0,0')[1][end_name]

print(part1(alldata))
print(part2(alldata))