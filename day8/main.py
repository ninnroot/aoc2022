



def get_line_from_coors(coors, coors_list):
    lst = [[], [], [], []]
    for i in coors_list:
        if coors[0] == i["coors"][0] and coors[1] > i["coors"][1]:
            lst[0].append(i)
            
        elif coors[1] == i["coors"][1] and coors[0] > i["coors"][0]:
            lst[1].append(i)
            
        elif coors[0] == i["coors"][0] and coors[1] < i["coors"][1]:
            lst[2].append(i)
            
        elif coors[1] == i["coors"][1] and coors[0] < i["coors"][0]:
            lst[3].append(i)
            
        else:
            continue
    lst[0] = [i for i in reversed(lst[0])]
    lst[1] = [i for i in reversed(lst[1])]
    # lst[2] = [i for i in reversed(lst[2])]
    # lst[3] =[i for i in reversed(lst[3])]
    return [i for i in reversed(lst)]

def get_visible_trees_from_line(height, line):

    visible_trees = []
    for i in line:
        if i["height"] < height:
            visible_trees.append(i)
        if i["height"] >= height:
            visible_trees.append(i)
            break

    return visible_trees




def f():
    x = open("input.txt", "r").readlines()
    lst = []
    
    for y, seq in enumerate(x):
        seq = seq.strip()
        for x, cha in enumerate(seq):
            cha = cha.strip()
            lst.append({"coors":(x,y), "height": cha})

    scenic_scores = []

    for i in lst:


        a = 1
        temp = []
        for x in get_line_from_coors(i["coors"],lst):
            
            t = len(get_visible_trees_from_line(i["height"], x))

            # if i["coors"] == (3,2):
            #     print(get_visible_trees_from_line(i["height"], x), t)

            temp.append(t)
            a*=t

            # print(x, t)
        scenic_scores.append(a)
        
            



    return scenic_scores


print(sorted(f()))
