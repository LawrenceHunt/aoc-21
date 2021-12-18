def load_file(file_name):
    file_data = open(file_name).readlines()
    return [line.rstrip() for line in file_data]

def most_common(lst):
    return max(set(lst), key=lst.count)

def least_common(lst):
    return min(set(lst), key=lst.count)

def calc_binary(lst):
    sum = 0
    for index, char in enumerate(lst[::-1]):
        if (char == '1'):
            sum += (2 ** (index))
    return sum

def main(file_name):
    lines = load_file(file_name)

    split_lines = [[char for char in line] for line in lines]
    
    columns = zip(split_lines[0], *split_lines[1:])

    lists = [list(line) for line in columns]
    
    gamma = [most_common(line) for line in lists]

    epsilon = [least_common(line) for line in lists]

    print(calc_binary(gamma) * calc_binary(epsilon))

            

main("input.txt")