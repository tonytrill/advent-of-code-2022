def main():
    file = open("input.txt", 'r')
    lines = file.readlines()
    
    count = 0
    elfs = []
    for line in lines:
        if line != '\n':
            count += int(line.replace('\n', ''))
        else:
            elfs.append(count)
            count = 0
    
    print("Max Value of Cals:")
    print(max(elfs))
    elfs.sort(key=None,reverse=True)
    print(sum(elfs[0:3]))
    
if __name__ == "__main__":
    main()