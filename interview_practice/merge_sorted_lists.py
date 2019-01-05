

def merge_sorted(list_a, list_b):
    # asserts
    ia = 0
    ib = 0
    ic = 0
    list_ab = list()
    while( ic < (len(list_a) + len(list_b))):
        if (ia < len(list_a)) and (ib < len(list_b)):
            if list_a[ia] <= list_b[ib]:
                list_ab.append(list_a[ia])
                ia += 1
            else:
                list_ab.append(list_b[ib])
                ib += 1
        else:
            if (len(list_a) > len(list_b)) and (ia < len(list_a)):
                list_ab.append(list_a[ia])
                ia += 1
            elif (len(list_b) > len(list_a)) and (ib < len(list_b)):
                list_ab.append(list_a[ia])
                ia += 1
        
        ic += 1

    return list_ab


if __name__ == '__main__':

    a = [1, 3, 5, 7, 9, 10, 11, 12]
    b = [2, 4, 6, 8, 9, 9]

    merged = merge_sorted(a, b)

    print(merged)
