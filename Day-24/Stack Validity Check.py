class Solution:
    def validateStackSequences(self, pushed, popped):
        stack = []
        j = 0  # pointer for popped

        # Simulate the stack operations
        for x in pushed:
            stack.append(x)

            # Pop from stack while top matches popped[j]
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        # Check if all popped matched
        if j == len(popped):
            print("true")
        else:
            print("false")
            remaining = len(stack)
            print(self.countPrimes(remaining))

    # Count number of primes ≤ n using Sieve of Eratosthenes
    def countPrimes(self, n):
        if n < 2:
            return 0

        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False

        return sum(sieve)


# ----------------- Main Driver -----------------
if __name__ == "__main__":
    n = int(input())
    pushed = list(map(int, input().split()))
    popped = list(map(int, input().split()))

    ob = Solution()
    ob.validateStackSequences(pushed, popped)
