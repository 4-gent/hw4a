def merge(l1, l2):
    sorted = l1 + l2
    for i in range(len(sorted) - 1):
        for j in range(i):
            if(sorted[i] < sorted[j]):
                temp = sorted[j]
                sorted[j] = sorted[i]
                sorted[i] = temp
    return sorted