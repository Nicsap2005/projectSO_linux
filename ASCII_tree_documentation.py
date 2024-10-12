import rich
print = rich.print

class Node:
    def __init__(self, name):
        self.parent = None
        self.name = name
        self.short_name = ""
        self.child_directories = []
        self.child_files = []
        self.edges = 0

    def build_tree(self, UBUNTU, depth, stacking):
        if depth <= 0:
            return # berhenti sampai sini
        else:

            available_directories = UBUNTU.get_available_directories()
            for directory in available_directories:
                current_Node = Node(self.name + directory)
                self.child_directories.append(current_Node)

                current_Node.short_name = directory

                current_Node.edges = len(stacking)

                stacking.append(self.name + directory)
                UBUNTU.change_directory(stacking[-1])

                current_Node.child_files = UBUNTU.get_available_files()

                current_Node.build_tree(UBUNTU, depth - 1, stacking)
                UBUNTU.change_directory(stacking.pop())

    def traverse(self):
        for directory in self.child_directories:
            print(directory.name, directory.edges)
            print(directory.child_files)
            directory.traverse()

    def pipe_edges(self, depth):
        panjang_space = 3
        for _ in range(depth - 1):
            print('|' + ' ' * panjang_space, end='')

    def new_pipe(self, lst):
        for x in lst:
            if x is True:
                print('|' + ' ' * 3, end='')
            else:
                print(' ' * 4, end='')

    def pretty_printing_directories(self, lst):
        for (i, directory) in enumerate(self.child_directories):
            directory.new_pipe(lst)
            
            if i == len(self.child_directories) - 1:
                if not self.child_files:
                    print('└──', directory.short_name)
                    lst.append(False)
                else:
                    print('├──', directory.short_name)
                    lst.append(True)
            else:
                print('├──', directory.short_name)
                lst.append(True)
            
            directory.pretty_printing_directories(lst)

            directory.pretty_printing_files(lst)

            lst.pop()

    def pretty_printing_files(self, lst):
        if self.child_files:
            for (j, file) in enumerate(self.child_files):
                self.new_pipe(lst)
                if j == len(self.child_files) - 1:
                    print('└──', file)
                else:
                    print('├──', file)

            self.new_pipe(lst)
            print()
        else:
            if not self.child_directories:
                self.new_pipe(lst)
                print()

def tembelek(UBUNTU, depth):
    if depth == 0: depth = float('inf')

    root = Node(UBUNTU.get_current_path() + '/')
    root.child_files = UBUNTU.get_available_files()

    stacking = [root.name]
    root.build_tree(UBUNTU, depth, stacking)

    print(root.name)
    print('|')
    root.pretty_printing_directories([])
    root.pretty_printing_files([])

    UBUNTU.change_directory(root.name)
