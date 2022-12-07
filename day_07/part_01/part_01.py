file_tree = \
    ['/', 
        ['a',
            ['e',
                ['i', 584]]],
        ['b.txt', 14848514],
        ['c.dat', 8504156],
        ['d',
            ['j', 4060174],
            ['d.log', 8033020],
            ['d.ext', 5626152],
            ['k', 7214296]]
    ]

def load_input(input_file: str, input_list: list):
    open_file = open(input_file)
    for line in open_file:
        input_list.append(line)
    open_file.close()

def load_data(input_list: list, data_list: list):
    # go through each line
    # hold variable for working_directory
    # if 'ls', 
    #   hold that position
    #   look for the next dollar sign
    #   add files and directories between the ls and next dollar sign
    return

def change_directory(command: str, working_directory: str):
    # real function will account for '$ ' before 'cd x'
    # move to root
    if len(command) == 4 and command[3] == '/':
        print('moving to \'/\'')
        return '/'
    # move to absolute path from '/'
    if command[3] == '/':
        print('moving to: ' + command[3:])
        return command[3:] + '/'
    elif command[3:] == '..':
        print('moving up one directory')
        temp_directory = ''
        for num in range(len(working_directory.split('/')) - 2):
            temp_directory += working_directory.split('/')[num]
            temp_directory += '/'
        return temp_directory
    else:
        print('appending to directory')
        return working_directory + command[3:] + '/'

class DeviceData:
    location = '/'
    type = 'file or directory'
    size = 0
    name = location.split('/')[-1]

def main():
    directory_commands = ['cd /', 'cd a', 'cd b', 'cd c', 'cd ..', \
                'cd b1', 'cd ..', 'cd /a', 'cd /']
    # dynamically create list of DeviceData objects
    data_list = []
    for num in range(10):
        data_list.append(DeviceData())
        data_list[num].location += str(num)
    
    # testing change_directory function
    working_directory = ''
    for command in directory_commands:
        print('command: ' + command)
        working_directory = change_directory(command, working_directory)
        print('cwd: ' + working_directory)
        print()

main()