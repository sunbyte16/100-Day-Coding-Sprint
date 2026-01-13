def count_characters(words, chars):
    from collections import Counter

    chars_count = Counter(chars)
    total_length = 0

    for word in words:
        word_count = Counter(word)
        for ch in word_count:
            if word_count[ch] > chars_count.get(ch, 0):
                break
        else:
            total_length += len(word)

    return total_length


if __name__ == "__main__":
    n = int(input().strip())
    words = [input().strip() for _ in range(n)]
    chars = input().strip()

    print(count_characters(words, chars))
