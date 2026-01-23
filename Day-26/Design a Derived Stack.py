def user_logic(capacity, operations):
    stack = []
    result = []
    
    # Initialization output
    result.append("null")
    
    for op in operations:
        parts = op.split()
        
        if parts[0] == "push":
            x = int(parts[1])
            if len(stack) < capacity:
                stack.append(x)
            result.append("null")
        
        elif parts[0] == "pop":
            if not stack:
                result.append("-1")
            else:
                result.append(str(stack.pop()))
        
        elif parts[0] == "increment":
            k = int(parts[1])
            inc = int(parts[2])
            limit = min(k, len(stack))
            for i in range(limit):
                stack[i] += inc
            result.append("null")
    
    return result


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    capacity = int(data[0])
    num_operations = int(data[1])
    operations = data[2:]
    
    results = user_logic(capacity, operations)
    
    # IMPORTANT: print in ONE LINE
    print(" ".join(results))


if __name__ == "__main__":
    main()
