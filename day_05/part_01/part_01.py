# copy all lines temporarily into lists, longest set of '[' sets width of 
# multi dimensional array, number of lines sets height

def load_input(stacks_matrix: list, moves_list: list):
    input_list = []
    open_file = open('example_input.txt')
    for line in open_file:
        input_list.append(line)
    open_file.close()

    stacks_list = []
    for line in input_list:
        if '[' not in line:
            break
        else:
            stacks_list.append(line.strip('\n'))
    
    for line in input_list:
        if 'move' in line:
            moves_list.append(line.strip())
    
    stacks_number = 0
    for stack in stacks_list:
        if len(stack.split('[')) > stacks_number:
            stacks_number = len(stack.split('['))
    
    for line in stacks_list:
        temp_list = []
        for num in range(stacks_number - 1):
            temp_list.append(line[num * 4:(num * 4) + 4].strip(' \n[]'))
        stacks_matrix.append(temp_list)

def rearrange_crates(stacks_matrix: list, moves_list: list):
    # indexes:
    #   1 for how many
    #   3 is from
    #   5 is to
    #   from and to are -1 because indexes start at 0, not 1
    how_many = []
    from_stack = []
    to_stack = []
    for move in moves_list:
        how_many.append(int(move.split(' ')[1]))
        from_stack.append(int(move.split(' ')[3]) - 1)
        to_stack.append(int(move.split(' ')[5]) - 1)
    # for each move
    for move in range(len(moves_list)):
        # for number of crates to move
        for count in range(how_many[move]):
            # remove top layer if empty
            if stacks_matrix[0] == [''] * len(stacks_matrix[0]):
                stacks_matrix.pop(0)
            print(stacks_matrix)
            print('move ' + str(move + 1) + ', operation ' + str(count + 1) + \
                ' of ' + str(how_many[move]))
            # for each vertical position in the stack
            for layer in range(len(stacks_matrix)):
                # skip layer if move from position is empty
                if stacks_matrix[layer][from_stack[move]] != '':
                    print(stacks_matrix[layer][from_stack[move]])
                    print('moving from ' + str(from_stack[move] + 1))
                    print('moving to ' + str(to_stack[move] + 1))
                    for reversed_layer in reversed(range(len(stacks_matrix))):
                        if stacks_matrix[reversed_layer][to_stack[move]] == '':
                            stacks_matrix[reversed_layer][to_stack[move]] = \
                                stacks_matrix[layer][from_stack[move]]
                            stacks_matrix[layer][from_stack[move]] = ''
                            break
                        elif reversed_layer == len(stacks_matrix):
                            # make a new layer
                            # not working right now...
                            stacks_matrix.insert(0, [''] * len(stacks_matrix[layer]))
                            stacks_matrix[0][to_stack[move]] = \
                                stacks_matrix[layer][from_stack[move]]
                            stacks_matrix[layer][from_stack[move]] = ''
                            break
                    break


    # for each move
    #   for number of crates to move
    #       for each layer
    #           if move from position is empty, move to next layer
    #           find first empty layer from bottom layer for move to position
    #           make that spot equal to the move from value
    #           if the layer is 0, make a new layer with:
    #               stacks_matrix.insert('' * len(stacks_matrix[]))
    #               replace the position of to with value from
    #           break

def main():
    stacks_matrix = []
    moves_list = []
    load_input(stacks_matrix, moves_list)
    rearrange_crates(stacks_matrix, moves_list)

    print('stacks result:')
    print(stacks_matrix)

main()