# load input file into a list
def load_input(input_filename: str, input_list: list):
    with open(input_filename, 'r') as open_file:
        for line in open_file.readlines():
            input_list.append(line.strip())

# load each tree height into multidimensional array of [column][row]
def load_tree_heights(input_list: list, tree_heights: list):
    for line in input_list:
        temp_list = []
        for tree in line:
            temp_list.append(tree)
        tree_heights.append(temp_list)
    return

# return true if visible from any angle
def get_visibility(x: int, y: int, tree_heights: list):
    # return true if 'edge'
    if x == 0 or x == len(tree_heights[0]) - 1:
        return True
    if y == 0 or y == len(tree_heights) - 1:
        return True
    # if the tree is bigger than any other tree in any direction, return true
    if \
    check_up(x, y, tree_heights) or \
    check_down(x, y, tree_heights) or \
    check_left(x, y, tree_heights) or \
    check_right(x, y, tree_heights):
        return True

    # return false if a tree is blocking from any angle
    return False

# to change check* functions, start at row, column of tree, check trees in the
# order away from tree until one tree is >= tree in question

# get visibility in the up direction
def check_up(row: int, column: int, tree_heights: list):
    # iterate through columns, overall length of multidimensional array
    for up_direction in range(len(tree_heights)):
        # blocking tree was found
        if tree_heights[up_direction][row] >= tree_heights[column][row]:
            # if the tree was itself, then all trees from this direction
            # have been checked
            if up_direction == column:
                return True

            break

# get visibility in the down direction
def check_down(row: int, column: int, tree_heights: list):
    # same as check_up(), just in reverse order
    for down_direction in reversed(range(len(tree_heights))):
        if tree_heights[down_direction][row] >= tree_heights[column][row]:
            if down_direction == column:
                return True

            break

# get visibility in the left direction
def check_left(row: int, column: int, tree_heights: list):
    # iterate through rows, length of an index in overall array
    for left_direction in range(len(tree_heights[0])):
        # blocking tree was found
        if tree_heights[column][left_direction] >= tree_heights[column][row]:
            # if the tree was itself, then all trees from this direciton
            # have been checked
            if left_direction == row:
                return True

            break

# get visibility in the right direction
def check_right(row: int, column: int, tree_heights: list):
    # same as check_left(), just in reverse order
    for right_direction in reversed(range(len(tree_heights[0]))):
        if tree_heights[column][right_direction] >= tree_heights[column][row]:
            if right_direction == row:
                return True

            break

def get_scenic_score(row: int, column: int, tree_heights: list):
    # look in every direction for how many trees are seen before the view
    # is blocked
    # multiply the four view distances together to get the scenic score
    scenic_score = 0
    return scenic_score

def main():
    # multidimensional array which represents [columns][rows]
    tree_heights = []
    input_list = []
    scenic_scores = []

    load_input('input.txt', input_list)
    load_tree_heights(input_list, tree_heights)

    scenic_scores.sort()

    print('highest scenic score:', scenic_scores[-1])

main()