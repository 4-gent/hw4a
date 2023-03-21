def palindrome(listInput):
    for i in range(len(listInput) // 2):
        if listInput[i] != listInput[len(listInput) - i - 1]:
            return False
    return True