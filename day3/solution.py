import re

def mulsum(filename, strict=False):
    with open(filename, 'r') as file:
        program = file.read().replace("\n", '')

    if strict is True:
        program = re.sub(r"don't\(\).*?(do\(\)|$)", '', program)
    
    matches = re.findall(r"mul\((\d+),(\d+)\)", program)
    sum = 0
    for match in matches:
        sum += int(match[0]) * int(match[1])
        
    return sum
    
if __name__ == '__main__':
    print('part 1:')
    print(mulsum('input.txt'))
    print('part 2:')
    print(mulsum('input.txt', True))