def user_logic(n, s):
    # Helper function to check prime
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    digits = []
    primes = []

    # Collect digits and prime digits
    for ch in s:
        if ch.isdigit():
            val = int(ch)
            digits.append(val)
            if is_prime(val):
                primes.append(val)

    # Determine the unique number
    if primes:
        unique = sum(primes) // len(primes)  # floor average
    else:
        unique = None  # special case

    result = []

    for ch in s:
        if ch.isdigit():
            val = int(ch)
            if unique is not None and unique != 0:
                idx = val % unique
            else:
                idx = val
            result.append(chr(ord('a') + idx))
        else:
            result.append(ch)

    return "".join(result)


def main():
    n = int(input().strip())
    s = input().strip()
    print(user_logic(n, s))


if __name__ == "__main__":
    main()
