def user_logic(n, positions_cards):
    # Separate positions into left and right
    left = []
    right = []
    
    for p, c in positions_cards:
        if p < 0:
            left.append((p, c))
        elif p > 0:
            right.append((p, c))
    
    # Sort:
    # Left: closest to 0 first → descending
    # Right: closest to 0 first → ascending
    left.sort(reverse=True)
    right.sort()
    
    def simulate(start_right):
        i = j = 0
        total = 0
        turn_right = start_right
        
        while True:
            if turn_right:
                if j < len(right):
                    total += right[j][1]
                    j += 1
                else:
                    break
            else:
                if i < len(left):
                    total += left[i][1]
                    i += 1
                else:
                    break
            turn_right = not turn_right
        
        return total
    
    # Try both starting directions
    return max(simulate(True), simulate(False))


def main():
    import sys
    data = sys.stdin.read().strip().split()
    
    n = int(data[0])
    positions_cards = []
    idx = 1
    for _ in range(n):
        pi = int(data[idx])
        ci = int(data[idx + 1])
        positions_cards.append((pi, ci))
        idx += 2
    
    print(user_logic(n, positions_cards))


if __name__ == "__main__":
    main()
