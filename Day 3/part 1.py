def is_int (matrix, row, char):
    try:
        if char < 0 or char >= len(matrix[row]):
            return False
        int(matrix[row][char])
        return True
    except ValueError as e:
        return False

def around_num (matrix, row, char, size): 
    if row == 0:
        row_finish = row
        r = 1
    elif row == len(matrix)-1:
        r = 0
        row_finish = row -1
    else:
        row_finish = row - 1
        r = 1

    if char == 0:
        char_finish = char
        c = size  
    elif char+size >= len(matrix[row])-1:
        char_finish = char -1
        c = 0 
    else:
        char_finish = char - 1
        c = size

    row_start = row + r
    
    
    while row_start >= row_finish:
        char_start = char + c
        while char_start >= char_finish:
            if matrix[row_start][char_start] != '.' and not matrix[row_start][char_start].isdigit():
                return True
            char_start-=1
        row_start-=1
    
    return False

matrix = []
with open('input.txt', 'r') as file:   
    
    for line in file:
        row = []
        for char in line:
            if char != '\n':
                row.append(char)
            else:
                break
        matrix.append(row)

print(matrix[-1])
skip = 0
num = ''
sum = 0

for row_index, row in enumerate(matrix):
    for char_index, char in enumerate(row):
        if skip != 0:
            skip-=1
            continue
        try: 
            int(char)
            num+=char
            i = 1

            while is_int(matrix, row_index, char_index + i):
                num+= matrix[row_index][char_index + i]
                skip=i
                i+=1
            
            if around_num(matrix, row_index, char_index, i):
                print(num)
                sum+=int(num)
                num=''
            else:
                num=''
                continue
        
        
        except ValueError as e:
            num = ''
            continue

print(sum)
