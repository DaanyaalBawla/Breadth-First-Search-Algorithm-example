import collections

def bfsalgo(graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        for n in graph[vertex]:
            if n not in visited:
                visited.add(n)
                queue.append(n)
        if vertex == 11:
            break

if __name__ == '__main__':
    graph = {1: [2,3], 2:[4,5], 3:[6,7], 4:[8,9], 5:[10,11], 6:[12,13], 7:[14,15], 8:[],9:[], 10:[],11:[], 12:[],13:[],14:[],15:[]}
    print("Breadth First Traversal path: ")
    bfsalgo(graph,1)