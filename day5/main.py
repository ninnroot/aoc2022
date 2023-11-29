
alpha = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"

def f():
    x = open("input2.txt", "r").readlines()
    lst = []
    for i in x:
        i = list(i)
        lst2 = []
        for j in i:
            if j in alpha.upper() + numbers:
                lst2.append(j)
            else:
                lst2.append("-")
        lst.append(lst2)

    indexes = {}
    for i in range(len(lst[-1])):
        if lst[-1][i] in numbers:
            indexes[i] = lst[-1][i]

    indexed_boxes = {i:[] for i in indexes.values()}

    for i in lst[0:len(lst)-1]:
        for j in range(len(i)):
            if i[j] in alpha.upper():
                c = i[j]
                d = indexes[j]
                indexed_boxes[d].append(c)
    for i in indexed_boxes:
        indexed_boxes[i] = list(reversed(indexed_boxes[i]))

    return indexed_boxes

def g():
    x = open("input.txt", "r").readlines()
    lst = []
    for i in x:
        i = i.split(" ")
        y = []
        for j in i:
            j = j.strip()
            try:
                y.append(int(j))
            except ValueError or TypeError:
                pass
        lst.append(y)

    return lst
        

boxes = f()

for i in g():
    
    x = boxes[str(i[1])]
    x = (x[len(x)-(i[0]):len(x)])
    for a in range(i[0]):
        boxes[str(i[1])].pop()
    for j in x:
        boxes[str(i[2])].append(j)

print(boxes)

x = ""
for i in boxes:
    print(boxes[i][-1])
    x+=boxes[i][-1]
print(x)


