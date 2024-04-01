
import tree

def dfs_iterative(head: tree.Node, soughtValue: int):
    """DFS the tree"""
    print("Depth-first searching the tree for {}".format(soughtValue))
    stack = [head]
    while(True):
        current_node = stack.pop()
        print("Visited node with value {}".format(current_node.value))
        if current_node.value == soughtValue:
            print("Found the sought value {} in node {} with value {}".format(soughtValue, current_node, current_node.value))
            return current_node
        for n in current_node.children:
            stack.append(n)
        if len(stack) == 0:
            break
    print("Did not find the value in the given graph.")
    return None

def dfs(current_node: tree.Node, soughtValue: int):
    """DFS the tree"""
    print("Visited node with value {}".format(current_node.value))
    if current_node.value == soughtValue:
        print("Found the sought value {} in node {} with value {}".format(soughtValue, current_node, current_node.value))
        return current_node
    for n in current_node.children:
        found = dfs(n, soughtValue)
        if found:
            return found
    return None

if __name__ == '__main__':
    root = tree.buildExampleTree()
    dfs_iterative(root,10)
    dfs(root, 10)