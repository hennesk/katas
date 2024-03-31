
class Node:
    def __init__(self, value: int):
        self.value = value
        self.neighbors = []

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)
eight = Node(8)
nine = Node(9)
ten = Node(10)
one.neighbors.extend([three,two])
two.neighbors.extend([one,three,four])
three.neighbors.extend([one,two,nine])
four.neighbors.extend([two,five,six])
five.neighbors.extend([seven,eight])
six.neighbors.extend([four,ten])
seven.neighbors.extend([five,eight])
eight.neighbors.extend([five,seven])
nine.neighbors.extend([three])
ten.neighbors.extend([six])

def bfs(head: Node, soughtValue: int):
    """BFS the graph"""
    queue = [head]
    visited = set()
    
    while(True):
        current_node = queue.pop(0)
        print("Visited node with value {}".format(current_node.value))
        visited.add(current_node)
        if current_node.value == soughtValue:
            print("Found the sought value {} in node {} with value {}".format(soughtValue, current_node, current_node.value))
            return current_node
        for n in current_node.neighbors:
            if n not in visited:
                print("Adding {} to the visit queue".format(n.value))
                visited.add(n)
                queue.append(n)
        if len(queue) == 0:
            break
    print("Did not find the value in the given graph.")
    return None

def dfs(head: Node, soughtValue: int):
    """DFS the graph"""
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
                print("Adding {} to the visit queue".format(n.value))
                visited.add(n)
                queue.append(n)
        if len(queue) == 0:
            break
    print("Did not find the value in the given graph.")
    return None

# bfs(one,10)
# bfs(one,45)


dfs(one,10)
dfs(one,9)
dfs(one,45)
