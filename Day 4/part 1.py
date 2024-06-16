
def check_win (winning_num, my_numbers):
    win=0
    i=0

    for num in my_numbers:
        if num in winning_num:
            i+=1
    
    if i == 0:
        return 0
    if i == 1:
        return 1
    win = 1
    while i != 1:
        win*= 2
        i-=1
    
    return win

sum = 0

with open ('input.txt', 'r') as file:
    for line in file:
        new_line = line.replace(',', '').replace(':', '').replace('|', '').replace('Card', '')
        num_list = new_line.split()
        game_id = num_list[0]
        win_num = num_list[1:11]
        my_num = num_list[11:]

        wins = check_win(win_num, my_num)
        
        sum+=wins

print(sum)

file.close()
