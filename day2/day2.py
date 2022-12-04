score_key = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

def get_score(opponent, yours):
    if opponent == 'A':
        if yours == 'X':
            return 3 + 1
        if yours == 'Y':
            return 6 + 2
        if yours == 'Z':
            return 0 + 3
    if opponent == 'B':
        if yours == 'X':
            return 0 + 1
        if yours == 'Y':
            return 3 + 2
        if yours == 'Z':
            return 6 + 3
    if opponent == 'C':
        if yours == 'X':
            return 6 + 1
        if yours == 'Y':
            return 0 + 2
        if yours == 'Z':
            return 3 + 3
    return 0

def get_score_part2(opponent, result):
        if result == 'X':
            if opponent == 'A':
                return score_key.get('Z') + 0
            if opponent == 'B':
                return score_key.get('X') + 0
            if opponent == 'C':
                return score_key.get('Y') + 0
        if result == 'Y':
            if opponent == 'A':
                return score_key.get('X') + 3
            if opponent == 'B':
                return score_key.get('Y') + 3
            if opponent == 'C':
                return score_key.get('Z') + 3
        if result == 'Z':
            if opponent == 'A':
                return score_key.get('Y') + 6
            if opponent == 'B':
                return score_key.get('Z') + 6
            if opponent == 'C':
                return score_key.get('X') + 6
            
def main():
    file = open("input.txt", 'r')
    lines = file.readlines()
    
    total_score_part_1 = 0
    total_score_part_2 = 0
    for line in lines:
        game = line.strip().replace(' ','')
        opponent = game[0]
        yours = game[1]
        # PART 1 Total Score
        total_score_part_1 += get_score(opponent, yours)
        
        #PART 2 Total Score
        total_score_part_2 += get_score_part2(opponent, yours)
        
    print(total_score_part_1)
    print(total_score_part_2)
        
        
    
    
    
if __name__ == "__main__":
    main()