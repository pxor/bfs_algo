import os
from bfs import bfs
from pathlib import Path
from generate_graph import g_graph

# main
def main():
    root_directory = Path(__file__).parent
    start = os.path.basename(root_directory)
    graph = g_graph(root_directory)

    bfs(graph, start)


if __name__ == "__main__":
    main()
