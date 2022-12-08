DISK_SIZE = 70000000
GOAL_SIZE = 30000000

# load all lines of input into input_list
def load_input(input_file: str, input_list: list):
    open_file = open(input_file)
    for line in open_file:
        input_list.append(line.strip())
    open_file.close()

# go line by line through input and execute commands 'cd' and 'ls'
def process_input(input_list: list, data_list: list, working_directory : str):
    # add '/' directory first
    data_list.append(DeviceData())
    data_list[0].type = 'directory'
    data_list[0].location = '/'
    data_list[0].name = '/'

    for line in range(len(input_list)):
        # if the line is a command
        if '$' in input_list[line]:
            print('command: ' + input_list[line][2:])
            # ls command
            if input_list[line][2:] == 'ls':
                print('listing directory')
                # load listings into data_list
                load_data(working_directory, list_directory(input_list, line), data_list)
            # cd command
            if input_list[line][2:4] == 'cd':
                print('changing directory')
                # set new working directory
                working_directory = \
                    change_directory(input_list[line], working_directory)
                print('current working directory:')
                print(working_directory)
            print()
    return

# accept 'cd' command and working directory, and return new working directory
def change_directory(command: str, working_directory: str):
    # move to root on 'cd /'
    if len(command) == 6 and command[5] == '/':
        print('moving to \'/\'')
        return '/'
    # move to absolute path from '/'
    if command[5] == '/':
        print('moving to: ' + command[5:])
        return command[3:] + '/'
    # move to parent directory
    elif command[5:] == '..':
        print('moving up one directory')
        temp_directory = ''
        # add the directories back, skipping the most recent one, to the
        # working directory
        for num in range(len(working_directory.split('/')) - 2):
            temp_directory += working_directory.split('/')[num]
            temp_directory += '/'
        return temp_directory
    else:
        # move to nested directory
        print('appending to directory')
        return working_directory + command[5:] + '/'

# returns slice of input that is current output of 'ls' command
def list_directory(input_list: list, output_position: int):
    # process slice of lines between output_position and next '$'
    # output_position += length of ls output to skip processing directory
    # listings in parent directory, which is process_input in this case
    start_position = output_position + 1
    end_position = start_position
    # set end of slice to first instance of '$'
    for line_position in range(len(input_list[start_position:])):
        if '$' in input_list[line_position + start_position]:
            end_position = line_position + start_position
            break
    # otherwise, we are at the end of the input
    if end_position == start_position:
        end_position = len(input_list)
    print('directory listing:')
    print(input_list[start_position:end_position])
    output_position = end_position
    return input_list[start_position:end_position]

def calculate_directory_depth(input: list):
    directory_depths = []
    for i in range(0, len(input)):
        directory_depths.append('/'.join(input[: i + 1]))
    return directory_depths

# set each element of directory listing to a DeviceData object
def load_data(working_directory: str, directory_listing: list, data_list: list):
    # for each directory listing, create new DeviceData object
    for item in range(len(directory_listing)):
        data_list.append(DeviceData())

        # if listing is a directory
        if directory_listing[item].split(' ')[0] == 'dir':
            data_list[-1].type = 'directory'
            # location includes itself, and directories end with '/'
            data_list[-1].location = \
                working_directory + directory_listing[item].split(' ')[1] + '/'
        else:
            data_list[-1].type = 'file'
            # size is listed in directory listing
            data_list[-1].size = int(directory_listing[item].split(' ')[0])
            data_list[-1].location = working_directory

        # name is listed in directory listing
        data_list[-1].name = directory_listing[item].split(' ')[1]

# for every directory, add up the files inside, traversing directories
# and adding them as well
def get_directory_sizes():
    directories = {}
    working_directory = []
    with open('input.txt', 'r') as input_file:
        for line in input_file.readlines():
            command = line.strip().split(' ')
            if '$ cd /' in line:
                working_directory = ['/']
            if '$ cd ..' in line:
                working_directory.pop()
            elif '$ cd ' in line:
                working_directory.append(command[2])
            # if file size is listed (not a directory)
            elif command[0].isdigit():
                for val in calculate_directory_depth(working_directory):
                    directories[val] = directories.get(val, 0) + int(command[0])
    return directories

# find smallest single file to delete that would free up space equal to
# GOAL_SIZE
def get_smallest_deletion(directory_sizes: list):
    # root directory is total used space
    unused_space = DISK_SIZE - directory_sizes['/']
    required_space = GOAL_SIZE - unused_space
    sorted_input = []
    # for each file size in directory dictionary
    for directory in directory_sizes.values():
        # if deleting would free up enough space
        if directory >= required_space:
            sorted_input.append(directory)
    # sort ascending
    sorted_input.sort()
    # return the smallest
    return sorted_input[0]

class DeviceData:
    location = '/'
    type = 'file or directory'
    size = 0
    name = ''

def main():
    working_directory = ''
    input_list = []
    data_list = []
    directory_sizes = []

    load_input('input.txt', input_list)
    process_input(input_list, data_list, working_directory)
    
    # check data_list
    for i in data_list:
        print()
        print('location:', i.location)
        print('type', i.type)
        print('size:', i.size)
        print('name:', i.name)
        print()

    directory_sizes = get_directory_sizes()
    print('size of directory to delete:', \
        get_smallest_deletion(directory_sizes))

main()