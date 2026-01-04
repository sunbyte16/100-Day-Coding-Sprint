def user_logic(n):
    # Find smallest prime factor
    spf = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            spf = i
            break
        i += 1

    # If n is prime
    if spf == n:
        return 1

    # If n is composite
    return 1 + (n - spf) // 2


n = int(input())
print(user_logic(n))
