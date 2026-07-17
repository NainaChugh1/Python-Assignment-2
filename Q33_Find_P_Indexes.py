# Q33 - Find all indexes of 'p' in the given string

s1 = "practice is important to perfectly learn python"

index_list = []

for i in range(len(s1)):
    if s1[i] == 'p':
        index_list.append(i)

print(index_list)
