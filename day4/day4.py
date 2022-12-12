def find_contained(id_1, id_2):
    return True if id_1.min_val >= id_2.min_val and id_1.max_val <= id_2.max_val else False

class ID:
    def __init__(self, min_val, max_val) -> None:
        self.min_val = int(min_val)
        self.max_val = int(max_val)

def main():
    file = open("./day4/input.txt", 'r')
    lines = file.readlines()
    count = []
    for line in lines:
        id_1 = ID(min_val=line.strip().split(',')[0].split('-')[0], max_val=line.strip().split(',')[0].split('-')[1])
        id_2 = ID(min_val=line.strip().split(',')[1].split('-')[0], max_val=line.strip().split(',')[1].split('-')[1])
        if find_contained(id_1=id_1, id_2=id_2) or find_contained(id_1=id_2, id_2=id_1):
            count.append(1)
        else:
            count.append(0)
           
    print(sum(count)) 
    
    # Part 2
    x = open("./day4/input.txt", "r").read().splitlines()
    t = 0
    for i in x:

        a,b=i.split(",")

        aa, aaa = [int(r) for r in a.split("-")]
        bb, bbb = [int(r) for r in b.split("-")]
        
        print(aa)

        if bbb >= aa >= bb or aaa >= bb >= aa:t+=1

    print(t)
        
        

if __name__ == "__main__":
    main()