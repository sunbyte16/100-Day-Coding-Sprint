def good_sum(N, A):
    stack = []

    for x in A:
        if x >= 0:
            stack.append(x)
        else:
            need = abs(x)
            removed_sum = 0

            # Remove elements from the end until sum >= abs(x)
            while stack and removed_sum < need:
                removed_sum += stack.pop()

            # Convert x to its absolute value and push
            stack.append(need)

    return sum(stack)


def main():
    import sys
    data = sys.stdin.read().strip().split()
    
    N = int(data[0])
    A = list(map(int, data[1:]))
    
    print(good_sum(N, A))


if __name__ == "__main__":
    main()
