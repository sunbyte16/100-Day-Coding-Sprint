def firstPalindrome(words):
    for word in words:
        if word == word[::-1]:
            return word
    return ""

if __name__ == "__main__":
    n = int(input().strip())
    
    # Read all words from a single line
    arr = input().strip().split()
    
    print(firstPalindrome(arr))
