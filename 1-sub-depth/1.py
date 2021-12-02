import os

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

def main():
    input = open(input_path, 'r').readlines()
    lines = [line.rstrip() for line in input]
    
    deeper_count = 0
   
    for index, line in enumerate(lines):
        if int(line) > int(lines[index -1]):
            deeper_count += 1
    
    print(deeper_count)


main()