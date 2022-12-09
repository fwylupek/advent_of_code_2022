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

# add each row, column position of the tail on a grid to a list

# size of grid:
#   rows = sum of downs - sum of ups
#   columns = sum of rights - sum of lefts