from itertools import cycle
import re
import math

with open("instructions.txt", "r") as f:
    lines = f.read()

directions, connections = lines.split("\n\n")
directions = [0 if d == "L" else 1 for d in directions]
graph = {}


for connection in connections.split("\n"):
    graph[connection[:3]] = [connection[7:10], connection[12:15]]


starting_nodes = [node for node in graph if node[2] == "A"]
cycles = []
for node in starting_nodes:
    for steps, d in enumerate(cycle(directions), start=1):
        node = graph[node][d]
        if node[2] == "Z":
            cycles.append(steps)
            break
steps = math.lcm(*cycles)

print("Number of steps required to reach ZZZ:", steps)
