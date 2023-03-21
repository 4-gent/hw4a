def sort_dictionary(dictionary):
    output = ()
    temp = sorted([(name, phone, age) for name, (phone, age) in dictionary.items()], key=lambda age: age[2])
    for i in temp:
        output = output + i[:-1]
    return output
