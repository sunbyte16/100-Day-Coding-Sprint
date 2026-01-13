def letterCombinations(digits):
    if not digits:
        return []
    
    # Mapping of digits to letters
    phone_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    
    result = []
    
    def backtrack(index, path):
        # If the current path has reached the length of digits, append to result
        if index == len(digits):
            result.append(path)
            return
        # Get letters corresponding to the current digit
        letters = phone_map[digits[index]]
        for letter in letters:
            backtrack(index + 1, path + letter)
    
    backtrack(0, "")
    return result

if __name__ == '__main__':
    digits = input().strip()
    result = letterCombinations(digits)
    result.sort()  # ensure lexicographical order
    print(' '.join(result))
