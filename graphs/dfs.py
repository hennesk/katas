
from graph import Node

def dfs(head: Node, soughtValue: int):
    """DFS the graph"""
    print("Depth-first searching the graph for {}".format(soughtValue))
    queue = [head]
    visited = set()
    
    while(True):
        current_node = queue.pop()
        print("Visited node with value {}".format(current_node.value))
        visited.add(current_node)
        if current_node.value == soughtValue:
            print("Found the sought value {} in node {} with value {}".format(soughtValue, current_node, current_node.value))
            return current_node
        for n in current_node.neighbors:
            if n not in visited:
                visited.add(n)
                queue.append(n)
        if len(queue) == 0:
            break
    print("Did not find the value in the given graph.")
    return None
