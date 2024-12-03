import re

def mulsum(filename):
    with open(filename, 'r') as file:
        program = file.read()
    
    pattern = r"mul\((\d+)\,(\d+)\)"
    matches = re.findall(pattern, program)
    
    sum = 0
    for match in matches:
        sum += int(match[0]) * int(match[1])
        
    return sum
    
if __name__ == '__main__':
    print('part 1:')
    print(mulsum('input.txt'))