# Q35 - Display unique words with length >= 4 starting with W or w

s1 = "How much wood would a woodchuck chuck if a Woodcutter could chuck wood to build a wooden house to woo his wife"

words = s1.split()

result = []

for word in words:
    if len(word) >= 4 and (word.startswith("w") or word.startswith("W")):
        if word not in result:
            result.append(word)

print(result)
