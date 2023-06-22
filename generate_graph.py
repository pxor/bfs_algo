import os


# Generate graph from root directory excluding 'venv' and hidden that start with '.'.
def g_graph(root_directory):
    graph = {}

    for dirpath, dirnames, filenames in os.walk(root_directory):
        current_directory = os.path.basename(dirpath)
        adjacent_items = [file_tree for file_tree in dirnames + filenames if file_tree != "venv" and not file_tree.startswith(".")]

        graph[current_directory] = adjacent_items

    return graph
