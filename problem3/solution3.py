# The solution provided for problem 3 by the AI agent is:

import sys
sys.setrecursionlimit(10**7)

def solve():
    input = sys.stdin.readline
    n = int(input().strip())

    if n % 2 == 1:
        print(0)
        return

    adj = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)

    bad_edges = 0  # edges with even subtree size

    def dfs(node, parent):
        nonlocal bad_edges
        size = 1
        for nei in adj[node]:
            if nei == parent:
                continue
            child_size = dfs(nei, node)
            if child_size % 2 == 0:
                bad_edges += 1
            size += child_size
        return size

    dfs(0, -1)

    good_edges = (n - 1) - bad_edges

    print(2 * good_edges * good_edges)


if __name__ == "__main__":
    solve()



if __name__ == "__main__":
    solve()

