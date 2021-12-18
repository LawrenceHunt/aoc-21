def load_file(file_name):
    file_data = open(file_name).readlines()
    return [line.rstrip() for line in file_data]


def rows_to_columns(rows):
    columns = zip(rows[0], *rows[1:])
    return [list(line) for line in columns]


def most_common(lst, default):
    num1 = lst.count('1')
    num0 = lst.count('0')
    if num1 > num0:
        return '1'
    elif num0 > num1:
        return '0'
    elif num0 == num1:
        return default


def least_common(lst, default):
    num1 = lst.count('1')
    num0 = lst.count('0')
    if num1 < num0:
        return '1'
    elif num0 < num1:
        return '0'
    elif num0 == num1:
        return default


def calc_binary(lst):
    sum = 0
    for index, char in enumerate(lst[::-1]):
        if (char == '1'):
            sum += (2 ** index)
    return sum


def filter_by_char_at_index(lst, char, index):
    output = []
    for item in lst:
        if item[index] == char:
            output.append(item)
    return output

def eliminate_by(rows, most_or_least):
    check_index = 0
    while True:
        columns = rows_to_columns(rows)
        column_at_index = columns[check_index]

        if most_or_least == 'most':
            most_common_at_index = most_common(column_at_index, '1')
            rows = filter_by_char_at_index(rows, most_common_at_index, check_index)
            
        elif most_or_least == 'least':
            least_common_at_index = least_common(column_at_index, '0')
            rows = filter_by_char_at_index(rows, least_common_at_index, check_index)

        if check_index == len(columns)-1 or len(rows) == 1:
            break
        else:
            check_index += 1
    return rows


def main(file_name):
    lines = load_file(file_name)
    rows = [[char for char in line] for line in lines]
    o2_rows = eliminate_by(rows, 'most')
    co2_rows = eliminate_by(rows, 'least')
    o2_number = calc_binary(o2_rows[0])
    co2_number = calc_binary(co2_rows[0])

    print(o2_number * co2_number)
            

main("input.txt")