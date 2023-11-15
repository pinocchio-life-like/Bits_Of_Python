matrix = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(i * j)
    matrix.append(row)

# Using nested list comprehension
matrix = [[i * j for j in range(3)] for i in range(3)]

print(matrix)