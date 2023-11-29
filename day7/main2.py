
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
        self.children.append(child)
        return self

    def get_child(self, path: str):
        for i in self.children:
            if i.path == path:
                return i
        return None

    def get_child_from_path(self, path: str):
        if path == self.path:
            return self
        for i in self.children:
            if str(i) == path:
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

    file_tree: Tree = None
    current_node: Tree = None
    lst = []

    for i in x:
        i = i.strip().split(" ")
        
        if i[0] == "$":
            if i[1] == "cd":
                if i[2] == "..":
                    current_node = current_node.parent

                else:
                    if file_tree:
                        current_node = file_tree.get_child_from_path(str(current_node) + i[2] + "/")

                    else:
                        file_tree = Tree(None, "/", [], [])
                        current_node = file_tree

            elif i[1] == "ls":
                lst.append(str(current_node))

        elif i[0] == "dir":
            x = Tree(current_node, i[1], [], [])
            file_tree.add_child(x)
            current_node.add_child(x)
            # file_tree.get_child_from_path(str(current_node) + i[1] + "/").add_child(current_node)
        else:
            x = Tree(current_node, i[1], [], [])
            current_node.add_file(File(i[1],int(i[0])))
            # file_tree.add_file(File(i[1],int(i[0])))
            # print([str(i) for i in file_tree.children], str(current_node))
            # file_tree.get_child_from_path(str(current_node) + i[1] + "/").add_child(current_node)


    needed_space =  30000000
    total_space = 70000000
    used_space = file_tree.get_child_from_path("/").get_total_size() # 40913445

    required_space = needed_space - (total_space - used_space)



    x = []
    # y = file_tree.get_child_from_path("/a/").get_total_size()
    # print(y)

    for i in lst:
        y = file_tree.get_child_from_path(i).get_total_size()
        # print(i, y)
        # print(y, i)
        if y >= 913445:
            x.append(y)

    return sorted(x)

print(f())