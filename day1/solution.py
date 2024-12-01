def read(filename):
    left = []
    right = []
    with open(filename, 'r') as file:
        for line in file:
            values = line.split()
            left.append(values[0])
            right.append(values[1])
            
    left.sort()
    right.sort()

    return left, right

def distance(left, right):
    result = 0
    for idx, value in enumerate(left):
        result += abs(int(value) - int(right[idx]))
        
    return result

def score(left, right):
    result = 0
    for l in left:
        result += int(l) * len(list(filter(lambda r: r == l, right)))
    return result

if __name__ == '__main__':
    left, right = read('input.txt')
    print('part 1:')
    print(distance(left, right))
    print('part 2:')
    print(score(left, right))