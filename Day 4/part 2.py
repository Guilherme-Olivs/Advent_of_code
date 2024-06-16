
def check_win (winning_num, my_numbers):
    win=0

    for num in my_numbers[:]:
        if num in winning_num:
           win+=1
    
    return win

sum = 0

matrix = []
with open('input.txt', 'r') as file:
    for line in file:  
        new_line = line.replace(',', '').replace(':', '').replace('|', '').replace('Card', '')
        num_list = new_line.split()
        row = []
        for num in num_list:
            row.append(num)
        row.append(1)
        matrix.append(row)
file.close()

for row_index, row in enumerate(matrix):
    mul = int(row[-1])
    game_id = row[0]
    win_num = row[1:11]
    my_num = row[11:-1]
    print(row_index)
    
    if row_index == len(matrix)-1:
        while mul != 0:
            mul -= 1
            wins = check_win(win_num, my_num)
            sum += wins
    
    while mul != 0:
        mul -= 1
        wins = check_win(win_num, my_num)
        sum += wins
        i= 1

        while wins != 0:
            matrix[row_index+i][-1]+=1
            i+=1
            wins-=1

sum = sum + len(matrix)
print(sum)

