# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from collections import Counter

data = sys.stdin.read().strip().split()
if not data:
    sys.exit(0)

N = int(data[0])
strings = data[1:1 + N]
k = int(data[1 + N])

freq = Counter(strings)

for s in strings:
    if freq[s] == 1:
        k -= 1
        if k == 0:
            print(s)
            break
else:
    # If loop didn't break, less than k distinct strings
    print(-1)