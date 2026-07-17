# Q34 - Count strings having length greater than 2 and are palindromes

words = ["aba", "abc", "1991", "wow", "aa", "madam", "python"]

count = 0

for word in words:
    if len(word) > 2:
        if word == word[::-1]:
            count += 1

print("Number of palindromes:", count)
