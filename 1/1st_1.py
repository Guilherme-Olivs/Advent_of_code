sum=0

with open('input_1.txt', 'r') as file:
    
    for line in file:
        a=0
        b=0
        c=0
        for char in line:
            try:
                number = int(char)
            except ValueError as e:
                continue

            if a != 0:
                 b=char
            else:
                a = char

            if b == 0:
                b=a

        c=int(a+b)
        sum+=c


print(sum)