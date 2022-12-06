# load input file and create a multidimensional array, with rows representing
# layers of crates, and columns representing stacks
def load_input(stacks_matrix: list, how_many: list, \
    from_stack: list, to_stack: list):
    moves_list = []
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
    for move in moves_list:
        how_many.append(int(move.split(' ')[1]))
        from_stack.append(int(move.split(' ')[3]) - 1)
        to_stack.append(int(move.split(' ')[5]) - 1)

def move_single_crate(stacks_matrix: list, \
    from_row: int, from_column: int, \
    to_row: int, to_column: int):
    print('moving: ' + stacks_matrix[from_row][from_column])
    print('from: ' + str(from_row) + ', ' + str(from_column))
    print('to: ' + str(to_row) + ', ' + str(to_column))
    if to_row == -1:
        insert_new_row(stacks_matrix)
        to_row = 0
        from_row += 1
    stacks_matrix[to_row][to_column] = stacks_matrix[from_row][from_column]
    stacks_matrix[from_row][from_column] = ''

def insert_new_row(stacks_matrix: list):
    print('inserting new blank row')
    stacks_matrix.insert(0, [''] * len(stacks_matrix[0]))

def remove_empty_row(stacks_matrix: list):
    print('removing empty row')
    if stacks_matrix[0] == [''] * len(stacks_matrix[0]):
        stacks_matrix.pop(0)

def get_from_row(stacks_matrix: list, column_position: int):
    # return first blank row that corresponds to column position
    for layer in range(len(stacks_matrix)):
        if stacks_matrix[layer][column_position] != '':
            return layer

# returns lowest available position, or -1 if there isn't one
def get_to_row(stacks_matrix: list, column_position: int):
    for reversed_layer in reversed(range(len(stacks_matrix))):
        if stacks_matrix[reversed_layer][column_position] == '':
            return reversed_layer
        elif reversed_layer == 0:
            return -1

def main():
    stacks_matrix = []
    how_many = []
    from_stack = []
    to_stack = []

    load_input(stacks_matrix, how_many, from_stack, to_stack)
    print('starting matrix: ')
    for row in stacks_matrix:
        print(row)

    from_row = 0
    from_column = 0
    to_row = 0
    to_column = 0

    # for each move
    for move in range(len(how_many)):
        for part in range(how_many[move]):
            print('move: ' + str(move + 1) + ', part ' + str(part + 1) + ' of '\
                + str(how_many[move] + 1))
            from_row = get_from_row(stacks_matrix, from_stack[move])
            from_column = from_stack[move]
            to_row = get_to_row(stacks_matrix, to_stack[move])
            to_column = to_stack[move]
            move_single_crate(stacks_matrix, from_row, from_column, to_row, to_column)
            for row in stacks_matrix:
                print(row)
            print()
    print('resulting matrix: ')
    for row in stacks_matrix:
        print(row)

main()