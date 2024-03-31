
class Node:
    def __init__(self, value: int):
        self.value = value
        self.neighbors = []

def buildExampleGraph():
    """
        Builds a graph that looks like this:
                   ┌───┐             
                ┌──┤ 1 ├──┐          
                │  └───┘  │          
        ┌───┐ ┌─┴─┐     ┌─┴─┐        
        │ 9 ├─┤ 3 ├─────┤ 2 │        
        └───┘ └───┘     └─┬─┘         
                        ┌─┴─┐  ┌───┐ 
                        │ 4 ├──┤ 6 │ 
                        └─┬─┘  └─┬─┘ 
                ┌───┐   ┌─┴─┐  ┌─┴──┐
                │ 7 ├───┤ 5 │  │ 10 │
                └─┬─┘   └─┬─┘  └────┘
                  │     ┌─┴─┐        
                  └─────┤ 8 │        
                        └───┘ 
        Graph illustration made with https://asciiflow.com
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
    return one
