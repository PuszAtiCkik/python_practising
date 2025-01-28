def merge(l1,l2):
    results = []
    i = 0
    j = 0
    while i <len(l1) and j <len(l2):
        if l1[i] < l2[j]:
            results.append(l1[i])
            i+=1
        else:
            results.append(l2[j])
            j+=1
    while i < len(l1):
        results.append(l1[i])
        i+=1
    while j <len(l2):
        results.append(l2[j])
        j+=1
    return results

def main():
    list1 = [1, 3, 5, 7]
    list2 =  [2, 4, 6, 8]
    print(merge(list1,list2))
main()