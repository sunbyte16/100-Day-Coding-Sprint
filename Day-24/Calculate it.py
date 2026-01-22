def count_expressible_numbers(X, Y):
    numbers = set()

    pow2 = 1
    while pow2 <= Y:
        pow3 = 1
        while pow2 * pow3 <= Y:
            val = pow2 * pow3
            if val >= X:
                numbers.add(val)
            pow3 *= 3
        pow2 *= 2

    return len(numbers)


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    X = int(data[0])
    Y = int(data[1])
    
    # Call user logic function and print the output
    result = count_expressible_numbers(X, Y)
    print(result)

if __name__ == "__main__":
    main()
