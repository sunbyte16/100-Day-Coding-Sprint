import sys

def user_logic(n, runs):
    target = n - 1
    i = 0
    while i < n and target > 0:
        if runs[i] == 0:
            return False  # stuck, cannot move forward
        take = min(runs[i], target)  # score as much as possible without overshooting
        i += take
        target -= take
    return target == 0

if __name__ == "__main__":
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    runs = list(map(int, input_data[1:n+1]))
    
    result = user_logic(n, runs)
    print("true" if result else "false")
