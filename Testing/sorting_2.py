my_list = [15, 5, 14, 33, 72, 26, 56, 42, 40]


def selection_sort(my_list):
    for cur_pos in range(len(my_list)):
        min_pos = cur_pos
        for scan_pos in range(cur_pos + 1, len(my_list)):
            if my_list[scan_pos] < my_list[min_pos]:
                min_pos = scan_pos

        # Swap
        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp


def insertion_sort(my_list):
    for key_pos in range(1, len(my_list)):  # 100
        key_value = my_list[key_pos]
        scan_pos = key_pos - 1
        while (scan_pos >= 0) and (my_list[scan_pos] > key_value):  # worst 50, Avg 25
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos = scan_pos - 1

        my_list[scan_pos + 1] = key_value


insertion_sort(my_list)
print(my_list)

# Selection sort, all cases
# n = 10, 10* 5 = 50
# n = 100, 100 * 50 = 5,000
# n = 1000, 1000 * 500 = 500,000
# n = (n/2) = n^2/2

# Insertion sort, worst case
# n = 10, 10* 5 = 50
# n = 100, 100 * 50 = 5,000
# n = 1000, 1000 * 500 = 500,000
# n = (n/2) = n^2/2

# Insertion sort, average case
# n = 10, 10* 2.5 = 25
# n = 100, 100 * 25 = 2,500
# n = 1000, 1000 * 250 = 250,000
# n = (n/4) = n^2/4

# Insertion sort, best case
# n = 10, 10* 1 = 10
# n = 100, 100 * 1 = 100
# n = 1000, 1000 * 1 = 1000
# n
