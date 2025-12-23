# натация - 0(1) , описание - концтантная сложность , пример- допуск к элементу списка по индекцу
# def find_element(my_list, target):
#     return my_list[target]
from _pyrepl.commands import left, right

# натация (0n)  описание - линейная сложность , пример - однопроходный цикл
# def find_element(my_list, target):
#     for i , j in enumerate(my_list):
#         if target == i :
#             return j

# enumerate - перебирает сп списак и нумериует его
# my_list = ["eliza","madina","saku"] [(0,"eliza"),(1,"madina"),(3,"saku")]
# так же i и j модно как угодно писать рапример ( a и d)


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
target = 11
def binary_search(arr, target):
    left,right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
    if arr[mid] == target:
        return print (mid)
    elif arr[mid] < target:
        right = mid + 1
    else:
        left = mid - 1

    return print("нету того то мы искали ")
binary_search(my_list, target)