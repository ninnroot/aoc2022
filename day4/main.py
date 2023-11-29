
def set_maker(s:str):
    x = s.split("-")
    a,b = int(x[0]),int(x[1])+1
    return set(range(a,b))


def f():
    x = open("input.txt","r").readlines()
    lst = []
    for i in x:
        j,k = i.strip().split(",")
        j,k = set_maker(j),set_maker(k)
        print(j,k)
        lst.append(j.intersection(k))
    return [i for i in lst if len(i)!=0]

print(len(f()))

