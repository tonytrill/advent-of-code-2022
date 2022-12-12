file = open("./day6/input.txt", 'r').readline().strip()
def get_mark(file, num_chars) -> int:
    for i in range(0, len(file)):
        string_to_check = file[i:i+num_chars]
        if len(string_to_check) == len(set(string_to_check)): return i + num_chars
print(get_mark(file,num_chars=4))
print(get_mark(file,num_chars=14))