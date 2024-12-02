first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(first_string) for first_string in first_strings if len(first_string) >= 5]

second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]

third_strings = first_strings + second_strings

third_result = {third_string: len(third_string) for third_string in third_strings if len(third_string) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)