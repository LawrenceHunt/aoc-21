import os

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

def main():
    input = open(input_path, 'r').readlines()
    lines = [line.rstrip() for line in input]
    
    average_depths = []

    for index, line in enumerate(lines[:-2]):
        iteration = lines[index:index+3]
        iteration_sum = sum(map(int, iteration))
        average_depths.append(iteration_sum)
    
    deeper_count = 0

    for index, average_depth in enumerate(average_depths):
        if average_depth > average_depths[index-1]:
            deeper_count += 1

    print('final deeper count ', deeper_count)

main()