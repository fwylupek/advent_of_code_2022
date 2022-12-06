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

def rearrange_crates(stacks_matrix: list, moves_list: list):
    # indexes in move command after splitting:
    #   1 for how many
    #   3 is from
    #   5 is to
    #   from and to have 1 subtracted because indexes start at 0, not 1
    how_many = []
    from_stack = []
    to_stack = []
    for move in moves_list:
        how_many.append(int(move.split(' ')[1]))
        from_stack.append(int(move.split(' ')[3]) - 1)
        to_stack.append(int(move.split(' ')[5]) - 1)
    
    # for each move
    for move in range(len(moves_list)):
        moved_stack = []
        starting_coordinates = [0, 0]
        # for number of crates to move
        for count in range(how_many[move]):
            # remove top layer from matrix if empty
            if stacks_matrix[0] == [''] * len(stacks_matrix[0]):
                stacks_matrix.pop(0)
            is_complete = False
            crate_letter = ''
            # for each vertical position in the stack
            for layer in range(len(stacks_matrix)):
                # break out of loop of searching for layers if move is complete
                if is_complete:
                    break
                # move to next layer if this 'move from' position is empty
                if stacks_matrix[layer][from_stack[move]] != '':
                    # letter of crate being moved is first occupied
                    # vertical space
                    crate_letter = stacks_matrix[layer][from_stack[move]]
                    # lowest vertical position this crate can be moved to
                    # as per the 'move to' part of the command
                    lowest_position = \
                        first_lowest_position(stacks_matrix, to_stack[move])
                    # if there exists a space for the crate, move it there
                    if lowest_position > -1:
                        stacks_matrix[lowest_position][to_stack[move]] = \
                            crate_letter
                        stacks_matrix[layer][from_stack[move]] = ''
                        is_complete = True
                    # if there is no space in this position
                    else:
                        # make a new layer
                        stacks_matrix.insert(0, \
                            [''] * len(stacks_matrix[layer]))
                        # add crate to desired position in new layer
                        stacks_matrix[0][to_stack[move]] = \
                            crate_letter
                        # remove crate from old layer, plus 1 because a new
                        # layer has been added since
                        stacks_matrix[layer + 1][from_stack[move]] = ''
                        is_complete = True
                    if is_complete:
                        # reorder stack that was moved
                        if stacks_matrix[0] == [''] * len(stacks_matrix[0]):
                            stacks_matrix.pop(0)
                        reorder_multi_stack(stacks_matrix, how_many[move], to_stack[move])

# return lowest available position, or -1 if there is no space
def first_lowest_position(stacks_matrix: list, to_position: int):
    for reversed_layer in reversed(range(len(stacks_matrix))):
        if stacks_matrix[reversed_layer][to_position] == '':
            return reversed_layer
        elif reversed_layer == 0:
            return -1

# return highest non-empty position
def first_highest_position(stacks_matrix: list, to_position: int):
    for layer in range(len(stacks_matrix)):
        if stacks_matrix[layer][to_position] != '':
            return layer
    return 0


# print which crate will end up at the top of each stack
def format_results(stacks_matrix: list):
    output_format = ''
    temp_list = [''] * len(stacks_matrix[0])
    for line in stacks_matrix:
        for i in range(len(line)):
            if line[i] != '' and temp_list[i] == '':
                temp_list[i] = line[i]
    for crate in temp_list:
        output_format += crate
    print(output_format)

def reorder_multi_stack(stacks_matrix: list, moves: int, to_position: int):
    if moves == 1:
        return
    # get list of stack that was placed
    new_stack = []
    highest_position = first_highest_position(stacks_matrix, to_position)
    if highest_position < 0:
        return
    for num in range(moves):
        new_stack.append(stacks_matrix[highest_position + num][to_position])
    print(new_stack)

def main():
    stacks_matrix = []
    moves_list = []
    load_input(stacks_matrix, moves_list)
    rearrange_crates(stacks_matrix, moves_list)
    for layer in stacks_matrix:
        print(layer)
    format_results(stacks_matrix)

main()