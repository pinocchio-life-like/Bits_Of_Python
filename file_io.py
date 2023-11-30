my_file = open("output.txt")
print(my_file.read())
my_file.close()

# or we can do it as

with open('output.txt') as my_file:
    print(my_file.read())