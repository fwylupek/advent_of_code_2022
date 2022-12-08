MAX_SIZE = 100000

def load_input(input_file: str, input_list: list):
    open_file = open(input_file)
    for line in open_file:
        input_list.append(line.strip())
    open_file.close()

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
            if input_list[line][2:] == 'ls':
                print('listing directory')
                load_data(working_directory, list_directory(input_list, line), data_list)
            if input_list[line][2:4] == 'cd':
                print('changing directory')
                working_directory = \
                    change_directory(input_list[line], working_directory)
                print('current working directory:')
                print(working_directory)
            print()
    return

# accept 'cd' command and working directory, and return new working directory
def change_directory(command: str, working_directory: str):
    # move to root
    if len(command) == 6 and command[5] == '/':
        print('moving to \'/\'')
        return '/'
    # move to absolute path from '/'
    if command[5] == '/':
        print('moving to: ' + command[5:])
        return command[3:] + '/'
    elif command[5:] == '..':
        print('moving up one directory')
        temp_directory = ''
        for num in range(len(working_directory.split('/')) - 2):
            temp_directory += working_directory.split('/')[num]
            temp_directory += '/'
        return temp_directory
    else:
        print('appending to directory')
        return working_directory + command[5:] + '/'

# returns slice of input that is current output of 'ls' command
def list_directory(input_list: list, output_position: int):
    # todo: append working directory + 'dir' type to new DeviceData
    # process slice of lines between output_position and next '$'
    # output_position += length of ls output
    start_position = output_position + 1
    end_position = start_position
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
    for item in range(len(directory_listing)):
        data_list.append(DeviceData())

        if directory_listing[item].split(' ')[0] == 'dir':
            data_list[-1].type = 'directory'
            data_list[-1].location = \
                working_directory + directory_listing[item].split(' ')[1] + '/'
        else:
            data_list[-1].type = 'file'
            data_list[-1].size = int(directory_listing[item].split(' ')[0])
            data_list[-1].location = working_directory

        data_list[-1].name = directory_listing[item].split(' ')[1]

# for every directory, add up the files inside, traversing directories
# and adding them as well
def get_directory_sizes(data_list: list):
    # add up files to directory sizes
    files = []
    directories = []
    for data in data_list:
        if data.type == 'file':
            files.append(data)
        else:
            directories.append(data)
    
    for file in files:
        for directory in directories:
            if file.location == directory.location:
                directory.size += file.size
    
    # doesn't work because not ordered
#    for i in directories:
#        for j in directories:
#            # add to parent directory
#            # if one directory is equal to the other, minus one level
#            if i.location in j.location and \
#                len(i.location.split('/')) + 1 == len(j.location.split('/')):
#                if i.name != j.name:
#                    print('adding', j.location, 'to', i.location)
#                    i.size += j.size
    # doesn't work because additions repeat
#    for f in data_list:
#        for d in data_list:
#            if f != d:
#                if f.type == 'file' and d.type == 'directory':
#                    if f.location == d.location:
#                        d.size += f.size
#
#    # add up directories to directory sizes
#    for i in data_list:
#        for j in data_list:
#            # if one location is contained within another location,
#            # but names are not the same (they aren't the same directory)
#            if i.location in j.location:
#                if i.name != j.name:
#                    j.size += i.size
    # add each directory to a list[][], sort it, start from bottom
    # adding file sizes to directories can be done in any order,
    # but the order of adding directories to directories has to be done
    # starting with the most nested directories first
    dir_list = []
    for dir in directories:
        dir_list.append([dir.location, dir.size])
    print(dir_list)

    for data in data_list:
        if data.type == 'directory':
            print(data.location, data.size)

def get_results_total(data_list: list):
    sum = 0
    for data in data_list:
        if data.type == 'directory':
            if data.size <= MAX_SIZE:
                sum += data.size
    return sum
    # 211047775 is too high
    # 46762389 is too high
    # 1142162 is also wrong...

class DeviceData:
    location = '/'
    type = 'file or directory'
    size = 0
    name = ''

def main():
    working_directory = ''
    input_list = []
    data_list = []

    load_input('example_input.txt', input_list)
    process_input(input_list, data_list, working_directory)
    
    # check data_list
    for i in data_list:
        print()
        print('location:', i.location)
        print('type', i.type)
        print('size:', i.size)
        print('name:', i.name)
        print()

    get_directory_sizes(data_list)
    print('sum:', get_results_total(data_list))

main()