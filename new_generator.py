nested_list = [['a', 'b', 'c'], ['d', 'e', 'f'], [1, 2, None]]


def flat_generator(lists):
    cnt1 = 0
    cnt2 = 0
    while len(lists) > cnt1:
        while len(lists[cnt1]) > cnt2:
            yield lists[cnt1][cnt2]
            cnt2 += 1
        cnt1 += 1
        cnt2 = 0


for item in flat_generator(nested_list):
    print(item)
