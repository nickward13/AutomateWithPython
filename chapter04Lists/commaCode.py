def toString(list):
    string = ''
    for item in list:
        if item == list[-1]:
            string += 'and ' + item
        else:
            string += item + ', '
    return string

spam = ['apples', 'bananas', 'tofu', 'cats']
print(toString(spam))