"""def main():
    my_file = open("super_villains.txt")
    name_list = []
    for line in my_file:
        # line = line.strip()
        name_list.append(line)
    my_file.close()
    print(name_list)
    print("There were", len(name_list), "names in the file.")

    # Linear search
    key = "Morgiana the Shrew"

    current_list_position = 0
    while current_list_position < len(name_list) and name_list[current_list_position] != key:
        current_list_position += 1

    if current_list_position == len(name_list):
        print("Found at:", current_list_position)
    else:
        print("Not found.")"""

    # Binary Search
key = "Morginana the Shrew"
lower_bound = 0
upper_bound = len(name_list) - 1
found = False
while lower_bound <= upper_bound and not found:
    middle_pos = (lower_bound + upper_bound // 2)

    if name_list[middle_pos] < key:
        lower_bound = middle_pos + 1
    elif name_list[middle_pos] > key:
        upper_bound = middle_pos - 1
    else:
        found = True

if found:
    print("The name is at position,", middle_pos)
else:
    print("The name was not in the list.")






main()