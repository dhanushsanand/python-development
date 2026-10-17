def append(list1:list, list2:list):
    list1.extend(list2)
    return list1


def concat(lists):
    result = []
    for item in lists:
        result.extend(item)
    return result 


def filter(function, list):
    result = []
    for element in list:
        if function(element):
            result.append(element)
    return result


def length(list):
    return len(list)


def map(function, list):
    result = []
    for item in list:
        result.append(function(item))
    return result


def foldl(function, list, initial):
    result = initial
    for item in list:
        result = function(result, item)
    return result


def foldr(function, list, initial):
    result = initial
    for i in range(len(list) -1, -1 , -1):
        result = function(result, list[i])
    return result


def reverse(list:list):
    low, high = 0, len(list) - 1
    while low <= high:
        list[low], list[high] = list[high], list[low]
        low += 1
        high -= 1
    return list

print(foldl(lambda acc, el: el/acc, [1, 2, 3, 4], 24))
