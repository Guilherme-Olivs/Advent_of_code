import re

blue_limit= 14
red_limit= 12
green_limit= 13
sum= 0

with open('input.txt', 'r') as file:

    for line in file:
        words= []
        mul = 0
        red= 0
        green= 0
        blue= 0

        cleaned_text = re.sub(r'[^A-Za-z0-9\s]', '', line.strip())

        words = cleaned_text.split(' ')


        i=0

        for word in words:
            if word == 'blue':
                if blue == 0:
                    blue = int(words[i-1])
                elif int(words[i-1]) > blue:
                    blue = int(words[i-1])
            elif word == 'red':
                if red == 0:
                    red = int(words[i-1])
                elif int(words[i-1]) > red:
                    red = int(words[i-1])
            elif word == 'green':
                if green == 0:
                    green = int(words[i-1])
                elif int(words[i-1]) > green:
                    green = int(words[i-1])
            i+=1

        mul= red * blue * green

        sum+=mul

print(sum)