# load input values from file, line by line into a list
def load_input(input_list: list):
    open_file = open('input.txt')
    for line in open_file:
        input_list.append(line.strip())
    open_file.close()
    return input_list

def find_like_letter(first_string: str, second_string: str):
    for letter in first_string:
        if letter in second_string:
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
    rucksacks_list = []
    load_input(rucksacks_list)

    rucksack_1 = ''
    rucksack_2 = ''
    # the submission value which holds the sum of priorities
    priorities_sum = 0
    like_letter = ''
    for line in rucksacks_list:
        # the format [x:x] in array can be simplified by removing the first
        # value to include the beginning, and the second value to include the
        # end, divided by half to denote the rucksacks
        rucksack_1 = line[:int(len(line) / 2)]
        rucksack_2 = line[int(len(line) / 2):]
        like_letter = find_like_letter(rucksack_1, rucksack_2)
        priorities_sum += determine_item_priority(like_letter)

    print(priorities_sum)

main()