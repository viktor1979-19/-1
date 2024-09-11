immutable_var = 1,9,2,7, 'bly', True
print(immutable_var)
#immutable_var[0] = 8
#print(immutable_var)
# TypeError: 'tuple' object does not support item assignment
#Главное свойство кортежа - это невозможность изменить его содержимое
mutable_list = [1,9,2,7,'grin', False ]
mutable_list[4] = 'blu'
print(mutable_list)
