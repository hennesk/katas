
import tree

def bfs(head: tree.Node, soughtValue: int):
    """BFS the tree"""
    print("Breadth-first searching the tree for {}".format(soughtValue))
    queue = [head]
    while(True):
        current_node = queue.pop(0)
        print("Visited node with value {}".format(current_node.value))
        if current_node.value == soughtValue:
            print("Found the sought value {} in node {} with value {}".format(soughtValue, current_node, current_node.value))
            return current_node
        for n in current_node.children:
            queue.append(n)
        if len(queue) == 0:
            break
    print("Did not find the value in the given graph.")
    return None

if __name__ == '__main__':
    root = tree.buildExampleTree()
    bfs(root,10)