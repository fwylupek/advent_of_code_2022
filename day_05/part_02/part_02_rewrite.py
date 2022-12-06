# load input file and create a multidimensional array, with rows representing
# layers of crates, and columns representing stacks
def load_input(stacks_matrix: list, moves_list: list):
    input_list = []
    open_file = open('example_input.txt')
    for line in open_file:
        input_list.append(line)
    open_file.close()

    stacks_list = []
    for line in input_list:
        # use the left bracket as an indicator that the line contains a crate
        if '[' not in line:
            break
        else:
            stacks_list.append(line.strip('\n'))
    
    # word 'move' indicates that this line is a move command
    for line in input_list:
        if 'move' in line:
            moves_list.append(line.strip())
    
    stacks_number = 0
    for stack in stacks_list:
        # find highest number of stacks, the rows in the matrix
        if len(stack.split('[')) > stacks_number:
            stacks_number = len(stack.split('['))
    
    for line in stacks_list:
        temp_list = []
        for num in range(stacks_number - 1):
            # every 4 characters, including empty space and brackets, denotes a
            # new crate label, so slice the lines up every 4 characters, remove
            # junk in lines afterward
            temp_list.append(line[num * 4:(num * 4) + 4].strip(' \n[]'))
        stacks_matrix.append(temp_list)

def from_position(stacks_matrix: list, row_position: int):
    # return first blank row that corresponds to column position
    for layer in range(len(stacks_matrix)):
        if stacks_matrix[layer][row_position] != '':
            return layer

# returns lowest available position, or -1 if there isn't one
def to_position(stacks_matrix: list, row_position: int):
    for reversed_layer in reversed(range(len(stacks_matrix))):
        if stacks_matrix[reversed_layer][row_position] == '':
            return reversed_layer
        elif reversed_layer == 0:
            return -1