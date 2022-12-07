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
                list_directory(working_directory, input_list, line)
            if input_list[line][2:4] == 'cd':
                print('changing directory')
                working_directory = \
                    change_directory(input_list[line], working_directory)
                print('current working directory:')
                print(working_directory)
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

def list_directory(working_directory: str, input_list: list, \
    output_position: int):
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

class DeviceData:
    location = '/'
    type = 'file or directory'
    size = 0
    name = location.split('/')[-1]

def main():
    working_directory = ''
    input_list = []
    # dynamically create list of DeviceData objects
    data_list = []
    for num in range(10):
        data_list.append(DeviceData())
        data_list[num].location += str(num)
    load_input('example_input.txt', input_list)
    process_input(input_list, data_list, working_directory)

main()