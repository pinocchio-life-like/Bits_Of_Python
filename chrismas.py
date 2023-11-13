for i in range(1, 10):
    spaces = " " * (10 - i)
    hashes = "#" * (2 * i - 1)
    print(spaces + hashes)
for i in range(3):
    print(f'{" "*7}{"#"*4}')