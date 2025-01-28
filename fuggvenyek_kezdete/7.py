def max_number(list1):
    max = list1[0]
    for x in list1:
        if list1[x] > max:
            max = list1[x]
    return max

print(max_number([41,63,85,35]))