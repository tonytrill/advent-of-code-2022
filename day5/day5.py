file = open("./day5/input.txt", 'r').read().splitlines()

def get_command(line):
    return int(line.split(' ')[1]), int(line.split(' ')[3]), int(line.split(' ')[5])

class Stack:
    def __init__(self) -> None:
        self.items = []
    
    def add_item(self, item):
        if item.strip() != "":
            self.items.insert(0, item.strip())
    def insert_item(self,item):
        if item.strip() != "":
            self.items.append(item.strip())
    def pop(self):
        return self.items.pop(0)
    def slice_stack(self, finish):
        list_to_return = self.items[0:finish]
        for item in list_to_return: self.pop()
        return list_to_return
    def __str__(self) -> str:
        return str(self.items)
        
is_commands = False
initial_stacks = []
stacks = []
for line in file[0:11]:
    if not is_commands: 
        x = [line[i:i+4] for i in range(0, len(line), 4)]
        if len(x) == 0:
            for stack in list(map(list, zip(*initial_stacks[0:-1]))):
                new_stack = Stack()
                for item in stack:
                    new_stack.insert_item(item)
                stacks.append(new_stack)
            is_commands = True
            next
        initial_stacks.append(x)
    else:
        move, position_1, position_2 = get_command(line)
        print("Moving " + str(move) + ", From Position " + str(position_1) + ", " + "To Position " + str(position_2))
        print("Starting Stacks")
        for stack in stacks: print(stack)
        for n in range(move):
            print("New Move")
            crate_to_move = stacks[position_1-1].pop()
            stacks[position_2-1].add_item(crate_to_move)

        
for stack in stacks: print(stack)
    
    
    