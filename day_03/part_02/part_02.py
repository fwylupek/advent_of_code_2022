# load input values from file, line by line into a list, then into
# groups of three
def load_input(groups_list: list):
    input_list = []
    open_file = open('input.txt')
    for line in open_file:
        input_list.append(line.strip())
    open_file.close()

    group_size = 3
    member_count = 0
    temp_list = []
    for line in input_list:
        temp_list.append(line)
        member_count += 1
        if member_count == group_size:
            groups_list.append(temp_list)
            temp_list = []
            member_count = 0

# return a list of letters two members have in common
def find_like_letters(first_string: str, second_string: str):
    like_letters = []
    for letter in first_string:
        if letter in second_string:
            if letter not in like_letters:
                like_letters.append(letter)
    return like_letters

# find the letter that the 3 member group has in common by iterating through
# the list of letters the last two members have in common
def find_group_letter(first_string: str, second_string: str, third_string: str):
    for letter in first_string:
        for like_letter in find_like_letters(second_string, third_string):
            if letter == like_letter:
                return letter

# use unicode point to follow priority of the prompt
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
def determine_item_priority(letter: str):
    if letter.islower(): # if letter is lowercase
        # return unicode code point for character - 96 since 'a' starts at 97
        return ord(letter) - 96
    else: # if letter is uppercase
        # unicode code point for 'A' is 65, so subtract 64, and add 26 to bring
        # it to start at 27
        return ord(letter) - 38

def main():
    groups_list = []
    load_input(groups_list)

    # sum of priorities of group item types
    priorities_sum = 0

    for group in groups_list:
        # add each priority value to the sum, unpacking the iterable group into
        # the argument of the function find_group_letter using an asterisk (*)
        priorities_sum += \
            determine_item_priority(find_group_letter(*tuple(group)))
    print(priorities_sum)

main()