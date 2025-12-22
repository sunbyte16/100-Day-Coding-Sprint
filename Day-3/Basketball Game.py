def user_logic(ops):
    record = []
    
    for op in ops:
        if op == 'C':
            if record:
                record.pop()
        elif op == 'D':
            if record:
                record.append(record[-1] * 2)
        elif op == '+':
            if len(record) >= 2:
                record.append(record[-1] + record[-2])
        else:
            record.append(int(op))
    
    return sum(record)


if __name__ == "__main__":
    n = int(input())
    line = input().strip().split()
    ops = line
    
    result = user_logic(ops)
    print(result)
