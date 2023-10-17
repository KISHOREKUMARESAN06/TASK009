my_list = [1, 'kishore', 42, 'PAT', '42']

check_elements = lambda lst: all(isinstance(item, (int, str)) for item in lst)

result = check_elements(my_list)

if result:
    print("Every element in the list is an integer or string.")
else:
    print("The list contains elements that are not integers or strings.")


