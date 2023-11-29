from typing import List

class File:
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

    def __str__(self) -> str:
        return f"{self.name} ({self.size})"


class Tree:
    def __init__(self, parent, path: str, files: List[File], children) -> None:
        self.parent: Tree = parent
        self.path = path
        self.files = files
        self.children = children

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        return self

    def get_child(self, path: str):
        for i in self.children:
            if i.name == path:
                return i
        return None

    def add_file(self, file: File):
        self.files.append(file)

    def get_total_size(self):
        lst = []

        for i in self.children:

            lst.append(i.get_total_size())

        return sum([i.size for i in self.files] + lst)

    def get_files(self):
        return [str(i) for i in self.files]

    def __str__(self) -> str:
        if self.parent is None:
            return "/"
        return str(self.parent)  + self.path + "/"




def f():
    x = open("input.txt", "r").readlines()
    file_tree = None
    current_node = file_tree
    lst = []
    dir_in_current_dir = {}
    for i in x:
        i = i.strip().split(" ")

        if i[0] == "$":
            if i[1] == "cd":
                if i[2] == "..":
                    current_node = current_node.parent
                    dir_in_current_dir = {i.path: i for i in current_node.children}
                else:
                    if file_tree:
                        current_node = dir_in_current_dir[i[2]]
                        # current_node = Tree(current_node, i[2], [], [])
                        file_tree = current_node
                     
                    else:
                        current_node = Tree(None, "/",[],[])
                        file_tree = current_node

                print(current_node, dir_in_current_dir)


            elif i[1] == "ls":
                if current_node.parent:
                    x = current_node.parent.get_total_size()
                    if x <= 100000:
                        lst.append(x)

        elif i[0] == "dir":
            dir_in_current_dir[i[1]] = Tree(current_node,i[1],[],[])
            current_node.add_child(dir_in_current_dir[i[1]])
            # current_node.add_child(Tree(current_node,i[1],[],[]))

        else:
            current_node.add_file(File(i[1],int(i[0])))

    return lst
                

        

print(sum(f()))

