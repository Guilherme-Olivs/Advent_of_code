def string_to_int (value):
    if value == 'one':
        return '1'
    elif value == 'two':
        return '2'
    elif value == 'three':
        return '3'
    elif value == 'four':
        return '4'
    elif value == 'five':
        return '5'
    elif value == 'six':
        return '6'
    elif value == 'seven':
        return '7'
    elif value == 'eight':
        return '8'
    else:
        return '9'

numbers_first = {
    'one': None,
    'two': None,
    'three': None,
    'four': None,
    'five': None,
    'six': None,
    'seven': None,
    'eight': None,
    'nine': None,
    '1': None,
    '2': None,
    '3': None,
    '4': None,
    '5': None,
    '6': None,
    '7': None,
    '8': None,
    '9': None
}

numbers_last = {
    'one': None,
    'two': None,
    'three': None,
    'four': None,
    'five': None,
    'six': None,
    'seven': None,
    'eight': None,
    'nine': None,
    '1': None,
    '2': None,
    '3': None,
    '4': None,
    '5': None,
    '6': None,
    '7': None,
    '8': None,
    '9': None
} 

sum=0

with open('input.txt', 'r') as file:
    
    for line in file:
        a=0
        b=0
        c=0
        for key in numbers_first:
            pos = line.find(key)
            numbers_first[key] = pos
            pos2 = line.rfind(key)
            numbers_last[key] = pos2
        
        for key in numbers_first:
            if numbers_first[key] == -1:
                numbers_first[key] = 100000

        b = max(numbers_last, key=numbers_last.get)
        a = min(numbers_first, key=numbers_first.get)

        try:
            number = int(a)
        except ValueError as e:
            a = string_to_int(a)

        try:
            number = int(b)
        except ValueError as e:
            b = string_to_int(b)

        numbers_first = {key: None for key in numbers_first}
        numbers_last = {key: None for key in numbers_last}

        c=int(a+b)
        sum+=c


print(sum)
