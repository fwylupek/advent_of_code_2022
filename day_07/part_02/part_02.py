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
def get_directory_sizes(data_list: list):
    # add up files to directory sizes, start with new lists for each type to
    # avoid repeating additions
    files = []
    directories = []
    for data in data_list:
        if data.type == 'file':
            files.append(data)
        else:
            directories.append(data)
    
    for file in files:
        for directory in directories:
            # the file exists in the directory, add the size to the directory
            if file.location == directory.location:
                directory.size += file.size

    # add each directory to a list[][], sort it, start from bottom
    # adding file sizes to directories can be done in any order,
    # but the order of adding directories to directories has to be done
    # starting with the most nested directories first
    directory_sizes = []
    for i in directories:
        directory_sizes.append([i.location, i.size])
    # sort directories by most nested, having most parents, first
    directory_sizes.sort(key=lambda x: len(x[0].split('/')), reverse=True)

    for i in directory_sizes:
        for j in directory_sizes:
            # if one directory is nested within another and difference in
            # number of nested directories is no more than one, one directory
            # is the parent of another, so add the size of the nested
            # directory to the parent
            if i[0] in j[0] and \
                len(i[0].split('/')) + 1 == len(j[0].split('/')):
                if i[1] != j[1]:
                    i[1] += j[1]

    return directory_sizes

# find smallest single file to delete that would free up space equal to
# GOAL_SIZE
def get_smallest_deletion(directory_sizes: list):
    # total amount of used space is equal to '/', last directory in list
    used_space = directory_sizes[-1][1]
    # amount needed is equal to DISK_SIZE - used space
    unused_space = DISK_SIZE - used_space
    # required space is remainder of unused space to meet GOAL_SIZE
    required_space = GOAL_SIZE - unused_space

    deletion_candidates = []
    for directory in directory_sizes:
        if directory[1] >= required_space:
            deletion_candidates.append(directory)
    
    print('candidates:', deletion_candidates)

    return '\ndisk size: ' + str(DISK_SIZE) + '\nused space: ' + str(used_space) + '\nunused space: ' + str(unused_space) + '\nrequired: ' + str(required_space)

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

    directory_sizes = get_directory_sizes(data_list)
    print('size of directory to delete:', \
        get_smallest_deletion(directory_sizes))

main()