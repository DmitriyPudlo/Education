num_man = int(input())
list_man = [str(z) for z in range(1, num_man + 1)]
k = int(input())

while len(list_man) > 3:
    del list_man[k - 1]
    list_man = list_man[k - 1:] + list_man[:k - 1]

while len(list_man) > 1:
    del list_man[k - 1]
    print(list_man)

print(*list_man)

