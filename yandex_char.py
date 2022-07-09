l = [1, 2, 3, 4, 5, 6, 7, 8,
     1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
     1, 2, 3, 4, 5, 6, 7]
temp = 0
total = 0
start = 0
end = 0
for i in range(len(l)):
    if i != len(l) - 1 and l[i] < l[i + 1]:
        temp += 1
    else:
        if temp > total:
            total = temp
            end = i
        temp = 0
start = end - total
print(start, end)
