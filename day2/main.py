# A, X, 1 = Rock
# B, Y, 2 = Paper
# C, Z, 3 = Scissors


dic = {
    "A X": (3, 1, "Z"),
    "A Y": (6, 2, "X"),
    "A Z":(0, 3, "Y"),
    "B X": (0, 1, "X"),
    "B Y": (3, 2, "Y"),
    "B Z": (6, 3, "Z"),
    "C X": (6, 1, "Y"),
    "C Y": (0, 2, "Z"),
    "C Z": (3, 3, "X"),

}


def f():
    lst = []
    x = open("input.txt", "r").readlines()
    for i in x:
        i = i.strip()
        opp, me = i.split(" ")
        ans = dic[i][2]
        lst.append(sum(dic[f"{opp} {ans}"][0:2]))



    return lst

print(sum(f()))