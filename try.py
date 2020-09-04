def binary_search(my_list, key):
    start = 0
    end = len(my_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if my_list[mid][0] == key:
            return mid
        elif my_list[mid][0] > key:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def find_user():
    data = [('admin',), ('ball',), ('user123',), ('xoxo',), ('zebra',)]
    result = (binary_search(data, 'xoxo'))
    if result != -1:
        print("Element is present at index", str(result))
    else:
        print("Element is not present in list")


find_user()


def quick_sort(my_list):
    less = []
    equal = []
    greater = []

    if len(my_list) > 1:
        pivot = my_list[0]
        for x in my_list:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quick_sort(less) + equal + quick_sort(greater)

    else:
        return my_list


def insertion_sort(list):
    for i in range(1, len(list)):
        temp = list[i]
        j = i - 1
        while j >= 0 and temp < list[j]:
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = temp
    return list


data = [('x',), ('ww',), ('aaa',), ('dbi7',), ('zebra',), ('1',)]
print(quick_sort(data))
print(insertion_sort(data))

