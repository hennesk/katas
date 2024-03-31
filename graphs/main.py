from graph import buildExampleGraph
from bfs import bfs
from dfs import dfs

graphEntryNode = buildExampleGraph()
bfs(graphEntryNode, 10)
bfs(graphEntryNode, 9)
bfs(graphEntryNode, 45)

dfs(graphEntryNode, 10)
dfs(graphEntryNode, 9)
dfs(graphEntryNode, 45)
