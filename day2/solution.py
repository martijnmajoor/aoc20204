def safe(filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            count += 1
            values = list(map(int, line.split()))
        
            desc = (values[1] - values[0]) < 0
            for idx, value in enumerate(values[1:], start=1):
                diff = value - values[idx-1]

                if abs(diff) < 1 or abs(diff) > 3 or (diff < 0) != desc:
                    count -= 1
                    break
                
                desc = diff < 0
    
    return count


if __name__ == '__main__':
    print('part 1:')
    print(safe('input.txt'))
    print('part 2:')
    print(0)