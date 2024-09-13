my_dict = {'Vika': 1995, 'Vlad':2000,'Max':2005}
print('Словарь:',my_dict)
print('Год рождения Влада:',my_dict.get('Vlad'))
print('Год рождения Камилы:',my_dict.get('Kamila'))
my_dict.update({'Roma': 2005, 'sacha': 2009})
print(my_dict)
del my_dict['Vika']
print(my_dict)
print()
my_set = {1,2,3,2,4,2,True,False,True,'cod','cch','cod'}
print(my_set)
my_set.add('znak')
my_set.add(9)
my_set.discard(False)
print(my_set)