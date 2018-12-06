import random

a= random.sample(range(100),10)   #generating a random list


def quickSort(lst):
    if len(lst) > 1:
        piv = lst[0]
        left = []
        right =[]
        for i in range(1, len(lst)):
            if (lst[i] < piv):
                left.append(lst[i])

            else:
                right.append(lst[i])
        return quickSort(left) + [piv] + quickSort(right)

    else:
        return lst

    lst= [0,8,2,6,9,1,7,4]


def mergeSort(lst):
    if len(lst) > 1:
        middle = len(lst) // 2
        left_sorted = mergeSort(lst[:middle])
        right_sorted = mergeSort(lst[middle:])
        i,j,k = 0, 0, 0
        merged_list = []

        while (i < len(lst) and len(left_sorted) != i and len(right_sorted) != j):
            if left_sorted[i] < right_sorted[j]:
                merged_list.append(left_sorted[i])
                i+=1
            else:
                merged_list.append(right_sorted[j])
                j+=1
            k+=1
        # Handle remaining items in the list.
        if len(left_sorted) == i:
            merged_list += right_sorted[j:]
        elif len(right_sorted) == j:
            merged_list += left_sorted[i:]
        return merged_list
    else:
        return lst

print(mergeSort(a))




