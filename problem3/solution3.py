# The solution provided for problem 3 by the AI agent is:

import sys
sys.setrecursionlimit(10**7)

def count_valid_operations(n: int, edges: list[tuple[int, int]]) -> int:
    """
    Counts the number of valid (remove, add) edge operations
    such that the resulting tree has a perfect matching.

    Time complexity: O(n)
    Space complexity: O(n)
    """

    if n % 2 == 1:
        return 0  # Perfect matching impossible

    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:  # O(n)
        adj[u].append(v)
        adj[v].append(u)

    subtree_size = [0] * n
    valid_edges = 0

    def dfs(node: int, parent: int) -> int:
        nonlocal valid_edges

        size = 1  # count current node
        for neighbor in adj[node]:  # total O(n)
            if neighbor == parent:
                continue
            child_size = dfs(neighbor, node)
            if child_size % 2 == 0:
                valid_edges += 1
            size += child_size

        subtree_size[node] = size
        return size

    dfs(0, -1)  # O(n)

    return valid_edges * valid_edges


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input().strip())
    edges = []
    for _ in range(n - 1):
        a, b = map(int, input().split())
        edges.append((a - 1, b - 1))

    print(count_valid_operations(n, edges))
