def around_char (matrix, row, char):
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
        c = 1
    elif char >= len(matrix[row])-1:
        char_finish = char -1
        c = 0 
    else:
        char_finish = char - 1
        c = 1

    row_start = row + r
    
    nums=[]

    while row_start >= row_finish:
        char_start = char + c
        while char_start >= char_finish:
            if is_int(matrix, row_start, char_start):
                num = get_num(matrix, row_start, char_start)
                nums.append(num)
            char_start-=1
        row_start-=1

    unique_nums = []

    if nums == []:
        return (0,0)
    else:
        unique_nums = set(nums)

    numbers = list(unique_nums)

    if len(numbers) == 2:
        return (int(numbers[0]), int(numbers[1]))    
    else:
       return (0,0) 





def is_int (matrix, row, char):
    try:
        if char < 0 or char >= len(matrix[row]):
            return False
        int(matrix[row][char])
        return True
    except ValueError as e:
        return False

def get_num (matrix, row, char): 
    num = matrix[row][char]
    i = 1
    while is_int(matrix, row, char + i):
        num+= matrix[row][char + i]
        i+=1
    i = 1
    while is_int(matrix, row, char - i):
        num= matrix[row][char - i] + num
        i+=1   
    return num

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
sum = 0

for row_index, row in enumerate(matrix):
    for char_index, char in enumerate(row):
        num1 = 0
        num2 = 0
        if char == '*':
            (num1, num2) = around_char(matrix, row_index, char_index)
        sum+=(num1*num2)    

print(sum)
