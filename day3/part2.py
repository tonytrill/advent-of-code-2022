from day3 import Sack, priority

class GroupSack:
    def __init__(self, sack_1, sack_2, sack_3):
        self.sack_1 = sack_1
        self.sack_2 = sack_2
        self.sack_3 = sack_3
        self.item = ""
    
    def find_item(self):
        for item in self.sack_1.contents:
            if item in self.sack_2.contents:
                if item in self.sack_3.contents:
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
    groups = zip(*(iter(lines),) * 3)
    for group in groups:
        sack1 = Sack(group[0].strip())
        sack2 = Sack(group[1].strip())
        sack3 = Sack(group[2].strip())
        
        grouping = GroupSack(sack_1=sack1, sack_2=sack2, sack_3=sack3)
        grouping.find_item()
        grouping.calculate_priority()
        total_priority.append(grouping.priority)
        
        
    print(sum(total_priority))

        
if __name__ == "__main__":
    main()