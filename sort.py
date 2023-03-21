def sort_dictionary(dictionary):
    output = ()
    temp = sorted([(name, phone, age) for name, (phone, age) in dictionary.items()], key=lambda age: age[2])
    for i in temp:
        output = output + i[:-1]
    return output

temp = {'Tom': (5464512, 24), 'Sara': (5446897, 32), 'Mary': (1557896, 20)}
print(sort_dictionary(temp))