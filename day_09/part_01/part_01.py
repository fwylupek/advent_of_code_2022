# rope has head and tail end. if the head moves far enough away, the tail
# is pulled toward the head. positions are on two-dimensional grid. puzzle
# input is series of motions. head and tail must always be touching or
# overlapping. if head is ever two steps directly up, down, left, or right
# from the tail, the tail must move one step in that direction
# if the head and tail aren't touching and aren't in the same row or column,
# the tail moves one step diagonally to keep up
# if head is (2, 2), and tail is (1, 3), they are diagonal. if head moves
# to (2, 1), tail must move to the position the head was, (2, 2)
# U, D, L, R = up, down, left, right, followed by number of steps in that
# direction
# after each step, update the position of the tail if the head is no longer
# adjacent to the tail
# how many positions does the tail of the rope visit at least once?
from time import sleep
from os import system

# add each row, column position of the tail on a grid to a list

def load_input(input_filename: str, input_list: list):
    with open(input_filename, 'r') as open_file:
        for line in open_file.readlines():
            input_list.append(line.strip())

def get_head_positions(input_list: list):
    position_x = 0
    position_y = 0
    head_positions = [[0, 0]]

    for motion_number in range(len(input_list)):
        if input_list[motion_number].split(' ')[0] == 'U':
            position_y += int(input_list[motion_number].split(' ')[1])
        elif input_list[motion_number].split(' ')[0] == 'D':
            position_y -= int(input_list[motion_number].split(' ')[1])
        elif input_list[motion_number].split(' ')[0] == 'L':
            position_x -= int(input_list[motion_number].split(' ')[1])
        elif input_list[motion_number].split(' ')[0] == 'R':
            position_x += int(input_list[motion_number].split(' ')[1])
        head_positions.append([position_x, position_y])
    
    print('head positions:')
    for position in head_positions:
        print(position)
    
    print()
    
    return head_positions

def get_tail_positions(head_positions: list):
    tail_positions = []

    # start at 0, 0
    tail_positions.append([0, 0])

    # if "touching" or in the same position of the head, don't move
    # I think that means if x and y or no more than 1 position away
    # if tail is on other side of where head is moving toward, then
    # tail has to catch up even if it's just one space

    # if moving only horizontally or vertically, from the same direction,
    # just take the same number of steps, - 1 if head and tail occupied same
    # position, -2 if tail is on the other side of movement direction

    # if moving vertically from horizontally, or horizontally from vertically,
    # cut off the "corner"

    return tail_positions

def get_grid_size(head_positions: list):
    grid_size = \
        {'width': 0, 'height': 0, \
        'min_x': 0, 'max_x': 0, \
        'min_y': 0, 'max_y': 0}

    for position in head_positions:
        if position[0] < grid_size['min_x']:
            grid_size['min_x'] = position[0]
        if position[0] > grid_size['max_x']:
            grid_size['max_x'] = position[0]
        if position[1] < grid_size['min_y']:
            grid_size['min_y'] = position[1]
        if position[1] > grid_size['max_y']:
            grid_size['max_y'] = position[1]
    
    grid_size['width'] = abs(grid_size['min_x']) + abs(grid_size['max_x'])
    grid_size['height'] = abs(grid_size['min_y']) + abs(grid_size['max_y'])
    
    # include [0, 0] position
    grid_size['width'] += 1
    grid_size['height'] += 1
    
    print('grid size:', grid_size['width'], 'x', grid_size['height'])
    return grid_size

# idk this will probably freeze your console with full input
def visualize_grid(positions: list, grid_size: dict):
    # make empty grid
    grid = []
    for height in range(grid_size['height']):
        grid.append(['.'] * grid_size['width'])
    
    # replace coordinate in grid with move number
    for position in range(len(positions)):
        row = positions[position][0] + abs(grid_size['min_x'])
        column = positions[position][1] + abs(grid_size['min_y'])
        grid[column][row] = position + 1
        # print grid in reverse, so y=0 is on the bottom
#        if system('clear') != 0:
#            system('cls')
#        for line in reversed(range(len(grid))):
#            print(*grid[line], sep='\t')
#        sleep(0.7)

def main():
    input_list = []
    head_positions = []
    load_input('input.txt', input_list)
    #load_input('example_input.txt', input_list)
    head_positions = get_head_positions(input_list)
    visualize_grid(head_positions, get_grid_size(head_positions))

main()