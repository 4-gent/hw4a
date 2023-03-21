def cacti_number(func):
    def wrapper(arr):
        count = 0
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] == 1:
                    count += 1
        return count
    num = wrapper(array)
    return num

array = []