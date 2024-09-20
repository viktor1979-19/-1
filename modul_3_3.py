def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params(1)
print_params(4, 3)
print_params('ложка', 4, False)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [True, 25, 'lom']
values_dict = {'a': "крот", 'b': False, 'c': 44}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)



