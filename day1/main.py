def f():
    elf_and_calories = []
    x = open("input.txt", "r").readlines()
    j = 0
    for i in x:
        if i != "\n":
            j+=int(i)
        else:

            elf_and_calories.append(j)
            j = 0
    return elf_and_calories


print(sorted(f()))