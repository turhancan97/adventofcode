from itertools import cycle

with open("instructions.txt", "r") as f:
    lines = f.read()

    directions, connections = lines.split("\n\n")
    directions = cycle(0 if d == "L" else 1 for d in directions)
    graph = {}
    for connection in connections.split("\n"):
        graph[connection[:3]] = [connection[7:10], connection[12:15]]

    node = "AAA"
    for steps, d in enumerate(directions, start=1):
        node = graph[node][d]
        if node == "ZZZ":
            break

print("Number of steps required to reach ZZZ:", steps)
