some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list({dup for dup in some_list if some_list.count(dup) > 1})
print(duplicates)