def load_file(file_name):
    file_data = open(file_name).readlines()
    return [line.rstrip() for line in file_data]


def main(file_name):
    lines = load_file(file_name)

    depth = 0
    distance = 0

    for line in lines:
        [direction, amount] = line.split()
        amount = int(amount)
        if direction == 'forward':
            distance += amount
         
        elif direction == 'up':
            depth -= amount
            
        elif direction == 'down':
            depth += amount

    print(depth * distance)


main("test_case.txt")






