# load input file into a list
def load_input(input_filename: str, input_list: list):
    with open(input_filename, 'r') as open_file:
        for line in open_file.readlines():
            input_list.append(line.strip())

# load each tree height into multidimensional array of [column][row]
def load_tree_heights(input_list: list, tree_heights: list):
    for line in input_list:
        temp_list = []
        for tree_height in line:
            temp_list.append(int(tree_height))
        tree_heights.append(temp_list)
    return

# get visibility in the up direction, go in reverse from the position of the
# tree - 1
def check_up_visibility(row: int, column: int, tree_heights: list):
    view_distance = 1
    # iterate through columns, descending from current tree
    for up_direction in reversed(range(column)):
        # blocking tree was found
        if tree_heights[up_direction][row] >= tree_heights[column][row]:
            # return the viewing distance
            return view_distance
        # if view reached the end of the tree line
        if up_direction == 0:
            # return the maximum viewing distance
            return view_distance
        view_distance += 1

# get visibility in the down direction, ascending from tree
def check_down_visibility(row: int, column: int, tree_heights: list):
    # same as check_up_visibility(), just in reverse order
    view_distance = 1
    # iterate through columns, ascending from current tree
    for down_direction in range(column + 1, len(tree_heights)):
        # blocking tree was found
        if tree_heights[down_direction][row] >= tree_heights[column][row]:
            # return the viewing distance
            return view_distance
        # if view reached the end of the tree line
        if down_direction == len(tree_heights) - 1:
            # return the maximum viewing distance
            return view_distance
        view_distance += 1

# get visibility in the left direction, descending from tree
def check_left_visibility(row: int, column: int, tree_heights: list):
    view_distance = 1
    # iterate through rows, descending from current tree
    for left_direction in reversed(range(row)):
        # blocking tree was found
        if tree_heights[column][left_direction] >= tree_heights[column][row]:
            # return the viewing distance
            return view_distance
        # if view reached the end of the tree line
        if left_direction == 0:
            # return the maximum viewing distance
            return view_distance
        view_distance += 1

# get visibility in the right direction, ascending from tree
def check_right_visibility(row: int, column: int, tree_heights: list):
    # same as check_left_visibility(), just in reverse order
    view_distance = 1
    # iterate through rows, ascending from current tree
    for right_direction in range(row + 1, len(tree_heights[0])):
        # blocking tree was found
        if tree_heights[column][right_direction] >= tree_heights[column][row]:
            # return the viewing distance
            return view_distance
        # if view reached the end of the tree line
        if right_direction == len(tree_heights[0]) - 1:
            # return the maximum viewing distance
            return view_distance
        view_distance += 1

def get_scenic_score(row: int, column: int, tree_heights: list):
    # look in every direction for how many trees are seen before the view
    # is blocked
    scenic_score = 0
    # since one zero will make the whole score zero, any tree on the edge will
    # have a scenic score of zero
    if row == 0 or row == len(tree_heights[0]) - 1:
        return scenic_score
    if column == 0 or column == len(tree_heights)- 1:
        return scenic_score
    
    # multiply the four view distances together to get the scenic score
    scenic_score = \
        check_up_visibility(row, column, tree_heights) * \
        check_down_visibility(row, column, tree_heights) * \
        check_left_visibility(row, column, tree_heights) * \
        check_right_visibility(row, column, tree_heights)

    return scenic_score

def main():
    # multidimensional array which represents [columns][rows]
    tree_heights = []
    input_list = []
    scenic_scores = []

    load_input('input.txt', input_list)
    load_tree_heights(input_list, tree_heights)

    for row in range(len(tree_heights)):
        for column in range(len(tree_heights[0])):
            scenic_scores.append(get_scenic_score(row, column, tree_heights))

    scenic_scores.sort()

    print('highest scenic score:', scenic_scores[-1])

main()