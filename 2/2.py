def load_file(file_name):
    file_data = open(file_name).readlines()
    return [line.rstrip() for line in file_data]


def main(file_name):
    lines = load_file(file_name)

    depth = 0
    distance = 0
    aim = 0

    for line in lines:
        [direction, amount] = line.split()
        amount = int(amount)
        
        if direction == 'forward':
            distance += amount
            depth += aim * amount            

        elif direction == 'up':
            aim -= amount
            
        elif direction == 'down':
            aim += amount

    print('depth', depth, 'distance', distance, 'total', depth * distance)


main("input.txt")






