def specialmsg(s, vocab):
    mp = {}
    for key, value in vocab:
        mp[key] = value

    result = []
    i = 0
    n = len(s)

    while i < n:
        if s[i] == '(':
            j = i + 1
            key = ""
            while j < n and s[j] != ')':
                key += s[j]
                j += 1

            if key in mp:
                result.append(mp[key])
            else:
                result.append("?")

            i = j + 1
        else:
            result.append(s[i])
            i += 1

    return "".join(result)


# Correct input handling for this judge
s = input().strip()
n = int(input().strip())

vocab = []
for _ in range(n):
    key, value = input().split()
    vocab.append([key, value])

print(specialmsg(s, vocab))
