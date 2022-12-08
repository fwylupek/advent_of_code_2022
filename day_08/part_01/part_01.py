# load tree heights into tree_heights[][]
# all trees in first and last rows, and first and last columns are visible
# for each tree, it is visible if
# directions above, below, left, or right are smaller
# MAX_HEIGHT is 9

def load_input(input_filename: str, input_list: list):
    with open(input_filename, 'r') as open_file:
        for line in open_file.readlines():
            input_list.append(line.strip())

def load_tree_heights(input_list: list, tree_heights: list):
    for line in input_list:
        temp_list = []
        for tree in line:
            temp_list.append(tree)
        tree_heights.append(temp_list)
    return

def get_visibility(x: int, y: int, tree_heights: list):
    print()
    print('checking visibility of', x, y)
    # return true if 'edge'
    if x == 0 or x == len(tree_heights[0]) - 1:
        return True
    if y == 0 or y == len(tree_heights) - 1:
        return True
    # if the tree is bigger than any other tree in any direction, return true
    if \
    check_up(x, y, tree_heights) or \
    check_down(x, y, tree_heights):
        return True
    # get visibility in the left direction
    # get visibility in the right direction
    return False

def check_up(x: int, y: int, tree_heights: list):
    # get visibility in the up direction
    for up_direction in range(len(tree_heights)):
        print('comparing', tree_heights[x][up_direction], 'to', tree_heights[x][y])
        if tree_heights[x][up_direction] >= tree_heights[x][y]:
            if up_direction == y:
                print('tree is visible from up direction')
                return True
            print('tree is not visible from up direction')
            break

def check_down(x:int, y: int, tree_heights: list):
    # get visibility in the down direction
    for down_direction in reversed(range(len(tree_heights))):
        print('comparing', tree_heights[x][down_direction], 'to', tree_heights[x][y])
        if tree_heights[x][down_direction] >= tree_heights[x][y]:
            if down_direction == y:
                print('tree is visible from down direction')
                return True
            print('tree is not visible from down direction')
            break
def main():
    input_list = []
    tree_heights = []

    load_input('example_input.txt', input_list)
    load_tree_heights(input_list, tree_heights)

    visible_trees = 0
    for x in range(len(tree_heights[0])):
        for y in range(len(tree_heights)):
            if get_visibility(x, y, tree_heights):
                print(x, y, 'is visible')
                visible_trees += 1
    
    print('visible trees', visible_trees)
    for line in tree_heights:
        print(line)

main()