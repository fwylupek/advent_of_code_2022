MAX_SIZE = 100000

def load_input(input_file: str, input_list: list):
    open_file = open(input_file)
    for line in open_file:
        input_list.append(line.strip())
    open_file.close()

def process_input(input_list: list, data_list: list, working_directory : str):
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
            data_list[-1].location = working_directory + directory_listing[item].split(' ')[1] + '/'
        else:
            data_list[-1].type = 'file'
            data_list[-1].size = int(directory_listing[item].split(' ')[0])
            data_list[-1].location = working_directory

        data_list[-1].name = directory_listing[item].split(' ')[1]

# for every directory, add up the files inside, traversing directories
# and adding them as well
def get_folder_sizes(data_list: list):
    # add sizes of all files to each parent directory
    for f in range(len(data_list)):
        for d in range(len(data_list)):
            if f != d and \
                data_list[f].type == 'file' and data_list[d].type == 'directory':
                if data_list[d].location == data_list[f].location:
                    data_list[d].size += data_list[f].size

    for data in data_list:
        if data.type == 'directory':
            print('directory ' + data.location + ': ' + str(data.size))
    # then add each directory to parent directory, starting with most
    # nested, i.e. /foo/bar before /foo, and add each to sum if over MAX_SIZE
    # todo

def get_results_total(data_list: list):
    sum = 0
    for data in data_list:
        if data.type == 'directory':
            if data.size >= MAX_SIZE:
                sum += data.size
    return sum
    # 211047775 is too high
    # 46762389 is too high

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

    get_folder_sizes(data_list)
    print('sum:', get_results_total(data_list))

main()