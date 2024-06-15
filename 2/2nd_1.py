import re

blue_limit= 14
red_limit= 12
green_limit= 13
sum= 0

with open('input.txt', 'r') as file:

    for line in file:
        words= []
        game_id = 0

        cleaned_text = re.sub(r'[^A-Za-z0-9\s]', '', line.strip())

        words = cleaned_text.split(' ')

        game_id = int(words[1])

        i=0

        for word in words:
            if word == 'blue':
                if int(words[i-1]) > blue_limit:
                    game_id = 0
                    break
            elif word ==  'red':
                if int(words[i-1]) > red_limit:    
                    game_id = 0
                    break
            elif word == 'green':
                if int(words[i-1]) > green_limit:
                    game_id = 0
                    break
            i+=1

        sum+=game_id

print(sum)