# open input file, copy the contents to a list, and close the file
calorie_list = []
open_file = open('input.txt')

for line in open_file:
    calorie_list.append(line)

open_file.close()

# create list to hold the total calories each elf is carrying
elf_calories = []

# holding variable for counting calories
temp_counter = 0

for num in range(len(calorie_list)):
    # if the line is empty, add holding variable to totals list,
    # and move to next elf
    if calorie_list[num] == '\n':
        elf_calories.append(temp_counter)
        temp_counter = 0
    else:
        # add value to holding variable
        temp_counter += int(calorie_list[num].strip())

        # add last value to the totals list
        if num + 1 == len(calorie_list):
            elf_calories.append(temp_counter)

# sort calorie totals for each elf in descending order
elf_calories.sort(reverse=True)

# print first value in sorted calorie total list
print(elf_calories[0])
