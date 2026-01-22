def find_possible_combinations(n, b, c, a):
    result = []

    def backtrack(path, b_left, c_left, a_left):
        if len(path) == n:
            result.append("".join(path))
            return

        if b_left > 0:
            path.append('B')
            backtrack(path, b_left - 1, c_left, a_left)
            path.pop()

        if c_left > 0:
            path.append('C')
            backtrack(path, b_left, c_left - 1, a_left)
            path.pop()

        if a_left > 0:
            path.append('A')
            backtrack(path, b_left, c_left, a_left - 1)
            path.pop()

    backtrack([], b, c, a)

    for combo in result:
        print(combo)


# Input handling
data = list(map(int, input().split()))
n, b, c, a = data
find_possible_combinations(n, b, c, a)
