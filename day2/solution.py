def safe(filename, dampen = False):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            values = list(map(int, line.split()))
            idx = bad(values)
            
            if idx is None or (dampen is True and bad([values[x] for x, _ in enumerate(values) if x != idx]) is None):
                count += 1
            
    return count

def bad(values):
    asc = isAscending(values)
    for idx, value in enumerate(values[:-1]):
        diff = value - values[idx+1]
        if abs(diff) < 1 or abs(diff) > 3 or (diff < 0) != asc:
            if idx >= len(values) -2 or (abs(value - values[idx+2]) > 0 and abs(value - values[idx+2]) < 4 and (value - values[idx+2] < 0) == asc):
                return idx+1
            else:
                return idx

    return None

def isAscending(values):
    x = []
    for idx, value in enumerate(values[1:], start=1):
        diff = value - values[idx-1]
        if diff > 0:
            x.append(True)
        elif diff < 0:
            x.append(False)
    return max(x, key=x.count)

if __name__ == '__main__':
    print('part 1:')
    print(safe('input.txt'))
    print('part 2:')
    print(safe('input.txt', True))