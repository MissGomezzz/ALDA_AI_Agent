# The code provided by the AI agent is:


def simulate_queue(n: int, t: int, s: str) -> str:
    """
    Simulates the queue transformation for t seconds.
    Time complexity: O(n * t)
    Space complexity: O(n)
    """
    queue = list(s)  # O(n)

    for _ in range(t):  # O(t)
        i = 0
        while i < n - 1:  # O(n) per second
            if queue[i] == 'B' and queue[i + 1] == 'G':
                # Swap adjacent elements
                queue[i], queue[i + 1] = queue[i + 1], queue[i]
                i += 2  # Prevent double processing within the same second
            else:
                i += 1

    return "".join(queue)  # O(n)


if __name__ == "__main__":
    n, t = map(int, input().split())
    s = input().strip()
    result = simulate_queue(n, t, s)
    print(result)
