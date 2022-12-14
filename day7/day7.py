script = open("./day7/input.txt", 'r').read().splitlines()

class File:
    def __init__(self) -> None:
        self.size = 0
        self.name = ""
        self.directory = None
    def setSize(self, size):
        self.size = size
    def setName(self, name):
        self.name = name
    def setDirectory(self, directory):
        self.directory = directory

class Directory:
    def __init__(self):
        self.files = []
        self.sub_directories = []
        self.parent_directory = None
        self.name = ""
        self.directory_size = 0
    def addName(self, name):
        self.name = name
    def addFile(self, file):
        self.files.append(file)
    def addSubDirectory(self, folder):
        self.sub_directories.append(folder)
        folder.setParentDirectory(self)
    def getDirectorySize(self):
        file_size = 0
        directory_size = 0
        for file in self.files:
            file_size+=file.size
        for directory in self.sub_directories:
            directory_size+=directory.getDirectorySize()
        self.directory_size = file_size+directory_size
        return file_size + directory_size
    def setParentDirectory(self, parent):
        self.parent_directory = parent  

print("Initializing Storage System")
root_directory = Directory()
root_directory.addName("/")
pointer = root_directory
for command in script[1:]:
    print("Current Directory: " + pointer.name)
    print(command)
    command = command.split(' ')
    if command[0] == "$":
        if command[1] == "cd": 
            if command[2] == "..":
                print("Going to Parent Directory")
                pointer = pointer.parent_directory
            elif command[2] == "/":
                print("Go to Root")
                pointer = root_directory
            else:
                print("Changing Current Directory to: " + command[2])
                pointer = [x for x in pointer.sub_directories if x.name == command[2]][0]
        if command[1] == "ls": print("Listing out directory contents")
    else:
        if command[0] == "dir":
            print("Adding Directory")
            new_directory = Directory()
            new_directory.addName(command[1])
            pointer.addSubDirectory(new_directory)
        else:
            print("Adding File of size: " + command[0])
            new_file = File()
            new_file.setSize(int(command[0]))
            new_file.setName(command[1])
            pointer.addFile(new_file)

print("Total Space Used: " + str(root_directory.getDirectorySize()))
print("Total Space Unused: " + str(70000000 - root_directory.getDirectorySize()))
size_to_delete = 30000000 - (70000000 - root_directory.getDirectorySize())
print(size_to_delete)
directory_to_calculate = []
directory_to_delete = []
def calculateSizes(folder):
    if len(folder.sub_directories) == 0: return 
    for x in folder.sub_directories:
        size = x.getDirectorySize()
        if size <= 100000: directory_to_calculate.append(size)
        if size > size_to_delete: directory_to_delete.append(size)
        calculateSizes(x)
calculateSizes(root_directory)
print("Part 1: Total Sum - " + str(sum(directory_to_calculate)))
print("Part 2: " + str(min(directory_to_delete)))
    