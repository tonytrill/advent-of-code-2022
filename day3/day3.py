priority = "abcdefghijklmnopqrstuvwxyz"
class Sack:
    def __init__(self, contents):
        self.contents = contents
        self.total_contents = len(contents)
        self.compartment_1 = self.contents[0:int(self.total_contents/2)]
        self.compartment_2 = self.contents[int(self.total_contents/2):]
        self.item = ""
        self.priority = 0
        
    def find_item(self):
        for item in self.compartment_1:
            if item in self.compartment_2:
                self.item = item
                break
    
    def calculate_priority(self):
        self.priority = priority.index(self.item.lower()) + 1
        if self.item.isupper():
            self.priority+=26
        
def main():
    file = open("./day3/input.txt", 'r')
    lines = file.readlines()
    total_priority = []
    for line in lines:
        sack = Sack(line.strip())
        sack.find_item()
        sack.calculate_priority()
        total_priority.append(sack.priority)
    print(sum(total_priority))

        
if __name__ == "__main__":
    main()