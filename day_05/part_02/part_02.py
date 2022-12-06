# load input file and create a multidimensional array, with rows representing
# layers of crates, and columns representing stacks
def load_input(stacks_matrix: list, how_many: list, \
    from_stack: list, to_stack: list):
    moves_list = []
    input_list = []
    open_file = open('input.txt')
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
    # separate number of crates moved per move, from which stack, and to which
    # stack into separate lists
    for move in moves_list:
        how_many.append(int(move.split(' ')[1]))
        from_stack.append(int(move.split(' ')[3]) - 1)
        to_stack.append(int(move.split(' ')[5]) - 1)

# use to and from coordinates to first move single crate at a time
def move_single_crate(stacks_matrix: list, \
    from_row: int, from_column: int, \
    to_row: int, to_column: int):
    print('moving: ' + stacks_matrix[from_row][from_column])
    print('from: ' + str(from_row) + ', ' + str(from_column))
    print('to: ' + str(to_row) + ', ' + str(to_column))
    # insert new blank row to hold crate if get_to_row returned -1
    # in which case, to_row is the new row, from row is shifted down
    if to_row == -1:
        insert_new_row(stacks_matrix)
        to_row = 0
        from_row += 1
    # set destination to crate, and set source to empty
    stacks_matrix[to_row][to_column] = stacks_matrix[from_row][from_column]
    stacks_matrix[from_row][from_column] = ''
    remove_empty_row(stacks_matrix)

# take the stack that was moved and put them back in reverse order
def rearrange_moved_stack(stacks_matrix: list, crate_list: list, \
    to_row: int, to_column: int):
    print('crate list: ')
    print(crate_list)
    # use get_from_row to find first value in column in row
    to_row = get_from_row(stacks_matrix, to_column)
    # skip if there was only one crate moved
    if len(crate_list) == 1:
        return
    # start at bottom of stack of moved crates, setting new order
    for num in reversed(range(len(crate_list))):
        stacks_matrix[to_row + num][to_column] = crate_list[num]
    print('rearranged stacks matrix: ')
    for row in stacks_matrix:
        print(row)

# insert a blank row of size of first row
def insert_new_row(stacks_matrix: list):
    print('inserting new blank row')
    stacks_matrix.insert(0, [''] * len(stacks_matrix[0]))

# remove empty row if there is one from moving crate from top
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
    # start at the bottom of a column and look for empty spot
    for reversed_layer in reversed(range(len(stacks_matrix))):
        if stacks_matrix[reversed_layer][column_position] == '':
            return reversed_layer
        elif reversed_layer == 0:
            return -1

# format according to rules
def format_result(stacks_matrix: list):                                    
    output_format = ''
    temp_list = [''] * len(stacks_matrix[0])
    for line in stacks_matrix:
        for i in range(len(line)):
            if line[i] != '' and temp_list[i] == '':
                temp_list[i] = line[i]
    for crate in temp_list:
        output_format += crate
    return output_format

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
        # list of crates that are moved this move
        crate_list = []
        # for each crate to be moved
        for part in range(how_many[move]):
            print('move: ' + str(move + 1) + ', part ' + str(part + 1) + ' of '\
                + str(how_many[move]))
            from_row = get_from_row(stacks_matrix, from_stack[move])
            from_column = from_stack[move]
            to_row = get_to_row(stacks_matrix, to_stack[move])
            to_column = to_stack[move]
            crate_list.append(stacks_matrix[from_row][from_column])
            # first move one crate at a time as before
            move_single_crate(stacks_matrix, from_row, from_column, to_row, to_column)
            for row in stacks_matrix:
                print(row)
        # at the end of the move, rearrange the crates that were moved
        rearrange_moved_stack(stacks_matrix, crate_list, to_row, to_column)
        print()
    print('resulting matrix: ')
    for row in stacks_matrix:
        print(row)
    
    print('crate on the top of each stack: ' + format_result(stacks_matrix))

main()