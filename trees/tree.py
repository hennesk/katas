class Node:
    def __init__(self, value: int):
        self.value = value
        self.children = []

def buildExampleTree():
    """
        Builds a graph that looks like this:
                  1
                /    \
               2      3
             /  \    /  \
            4    5  6    7
          /  \  /
         8   9  10
        Graph illustration made with difficulty
    """
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
    one.children.extend([two,three])
    two.children.extend([four,five])
    three.children.extend([six,seven])
    four.children.extend([eight,nine])
    five.children.extend([ten])

    return one
