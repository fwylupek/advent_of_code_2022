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

        data_list[-1].location = \
            working_directory + directory_listing[item].split(' ')[1]

        if directory_listing[item].split(' ')[0] == 'dir':
            data_list[-1].type = 'directory'
            data_list[-1].location = data_list[-1].location + '/'
        else:
            data_list[-1].type = 'file'
            data_list[-1].size = int(directory_listing[item].split(' ')[0])

        data_list[-1].name = data_list[-1].location.split('/')[-1]

# for every directory, add up the files inside, traversing directories
# and adding them as well
def get_deletion_candidate(data_list: list):
    # option 1:
        # first, set the directory size values to the files they contain
        # then, set the directory size values to the directories they contain
    # option 2:
    # it's a little broken right now, but I have to come back to this
    for f in range(len(data_list)):
        for d in range(len(data_list)):
            if f != d and \
                data_list[f].type == 'file' and \
                data_list[d].type == 'directory':
                print('comparing ', \
                    data_list[f].location, data_list[d].location)
                if data_list[f].location in data_list[d].location:
                    data_list[d].size += data_list[f].size
                    print(int(data_list[d].size + data_list[f].size))

    for data in data_list:
        if data.type == 'directory':
            print('directory ' + data.location + ': ' + str(data.size))

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
        print()

    get_deletion_candidate(data_list)


main()