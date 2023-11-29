

def is_touching(head, tail):

    if ((head[0] - tail[0])**2 + (head[1] - tail[1])**2)**0.5 <= 2.5:
        return True
    return False
    
def move_knot(instruction, knot):
    if instruction == "R":
        knot[0] += 1
    elif instruction == "D":
        knot[1] -= 1
    elif instruction == "L":
        knot[0] -= 1
    elif instruction == "U":
        knot[1] += 1

    return knot


def f():
    x = open("input.txt", "r").readlines()
    x = [i for i in x]

    head_loc = [0,0]
    tails = [[0,0]]*9
    tail_places = []
    prev_locs = [[0,0]]*10

    for i in x:
        i = i.strip().split(" ")
        i[1] = int(i[1])
        for j in range(i[1]):
            prev_locs[0] = [*head_loc]
            for s,p in enumerate(prev_locs):
                if s == 0:
                    continue
                prev_locs[s] = tails[s-1]

            head_loc = move_knot(i[0],head_loc)
            
            for s,a in enumerate(tails):

                if s==0:
                    if not is_touching(head_loc,tails[s]):
                        tails[s] = [*prev_locs[0]]
                else:
                    if not is_touching(tails[s-1],tails[s]):
                        tails[s] = [*prev_locs[s]]
            print(head_loc, tails)
            

            tail_places.append(tuple(tails[-1]))

    # for i in x:
    #     i = i.strip()
    return set(tail_places)

print(len(f()))