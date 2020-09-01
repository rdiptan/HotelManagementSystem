def binary_search(list, key):
    start = 0
    end = len(list) - 1
    while start <= end:
        mid = (start + end) // 2
        if list[mid][0] == key:
            return mid
        elif list[mid][0] > key:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def find_user():
    data = [('admin',), ('ball',), ('user123',), ('xoxo',), ('zebra',)]
    # my_data = []
    # for i in data:
    #     my_data.append(i[0])
    result = (binary_search(data, 'xoxo'))
    if result != -1:
        print("Element is present at index", str(result))
    else:
        print("Element is not present in list")


find_user()


# def binary_search_iterative(item_list, item):
#     first = 0
#     last = len(item_list) - 1
#     found = False
#     while first <= last and not found:
#         mid = (first + last) // 2
#         if item_list[mid] == item:
#             found = True
#         else:
#             if item < item_list[mid]:
#                 last = mid - 1
#             else:
#                 first = mid + 1
#     return found
#
#
# result = binary_search_iterative([1, 2, 3, 5, 8], 5)
# if result:
#     print("Element is present at list")
# else:
#     print("Element is not present in list")
