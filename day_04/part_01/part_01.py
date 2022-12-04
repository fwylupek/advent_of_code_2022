# load input file into a list of lines
def load_input(section_assignments : list):
    open_file = open('input.txt')
    for line in open_file:
        section_assignments.append(line)
    open_file.close()

# determine if one assignment contains all sections of another
def determine_overlap(assignment_pair: str):
    # unpack the results of the range of each assignment from a pair of
    # assignments. here, the first split is by ',', then by '-', so index 0
    # becomes first positional argument for range, second argument is index 0
    # plus 1
    assignment_1 = [*range(int(assignment_pair.split(',')[0].split('-')[0]), \
        int(assignment_pair.split(',')[0].split('-')[1]) + 1)]
    assignment_2 = [*range(int(assignment_pair.split(',')[1].split('-')[0]), \
        int(assignment_pair.split(',')[1].split('-')[1]) + 1)]

    # convert lists into sets to use issubset() method, returns True if one
    # assignment is a subset, or is contained, within another
    if set(assignment_1).issubset(assignment_2) or \
        set(assignment_2).issubset(assignment_1):
        return True
    else:
        return False

def main():
    section_assignments = []
    section_overlaps = 0

    load_input(section_assignments)

    for line in section_assignments:
        if determine_overlap(line):
            section_overlaps += 1
    
    # show occurrences of overlaps
    print(section_overlaps)

main()