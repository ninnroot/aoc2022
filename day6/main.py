

def f():
    x = open("input.txt", "r").readlines()
    s = ""
    c = 0
    for i in x[0]:
        if len(s)== 14:
            if len(set(s)) == 14:
                return c
            else:
                temp = ""
                for j in list(s)[1:len(s)+1]:
                    temp+=j

                s=temp
        s+=i
        c+=1
        

print(f())
    
