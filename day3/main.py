from math import ceil

alphas = "abcdefghijklmnopqrstuvwxyz"
dic = {
    j:i+1 for i,j in enumerate(list(alphas+alphas.upper()))
}

def list_spliter(lst: list):
    
    return [lst[0:ceil(len(lst)/2)],lst[ceil(len(lst)/2):len(lst)+1]]

def f():
    x = open("input.txt", "r").readlines()
    total = 0

    c = 1
    lst = []
    for i in x:
        lst.append(set(i.strip()))        
        if c%3==0:

            total += dic[list(lst[0].intersection(lst[1].intersection(lst[2])))[0]]
            lst=[]



        
        c+=1



    return total


print(f())