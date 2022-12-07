# signal is seemingly random characters that device receives one at a time
# need to detect start of packet marker: four characters that are all different
# identify the first position where the four most recently received characters
# were all different, needs to report the number of characters from the
# beginning of the buffer to the end of the first four-character marker
# since the characters are all different, need to skip some like characters
# to find the marker
MARKER_SIZE = 14

example_input = \
    ['mjqjpqmgbljsphdztnvjfqwrcgsmlb', \
     'bvwbjplbgvbhsrlpgdmjqwftvncz', \
     'nppdvjthqldpwncqszvftbrmjlhg', \
     'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', \
     'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw']

def load_input():
    puzzle_input = []
    open_file = open('input.txt', 'r')
    for line in open_file:
        puzzle_input.append(line)
    open_file.close()
    return puzzle_input

def is_marker(characters: list):
    if len(characters) < MARKER_SIZE:
        return False
    # compare all characters to each other
    for i in range(len(characters)):
        for j in range(len(characters)):
            if characters[i] == characters[j]:
                # if they're not the same index in the list, so itself,
                # then they're not unique
                if j != i:
                    return False
    # checks passed, it's a marker
    return True

def convert_string_to_list(input_string: str, output_list: list):
    for character in input_string:
        output_list.append(character)

def get_marker(signal: str):
    signal_list = []
    convert_string_to_list(signal, signal_list)
    for i in range(len(signal_list) - MARKER_SIZE):
        # get the first four characters
        packet_portion = signal_list[i:i + MARKER_SIZE]
        # compare to see if they're all unique
        if is_marker(packet_portion):
            # if so, that's the answer
            print('signal: ' + signal)
            print('marker is: ', *packet_portion, sep='')
            print('characters processed:', i + MARKER_SIZE)
            return

def main():
    puzzle_input = load_input()
    get_marker(puzzle_input[0].strip())

main()
