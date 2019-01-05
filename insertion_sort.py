import numpy as np
# insertion sort

def insertion_sort(values):

    assert isinstance(values, list)
    
    for next_index in range(1, len(values)):
        value_to_insert = values[next_index]
        
        while (value_to_insert < values[next_index - 1]) and next_index > 0:
            values[next_index] = values[next_index - 1]
            next_index -= 1

        values[next_index] = value_to_insert

    return values


def main():
    values = [34, 56, 4, 10, 77, 51, 93, 30, 5, 52, 52]
    
    
    print("Original list: {}\n".format(values))
    ins_sorted = insertion_sort(values).copy()
    print("Insertion Sorted list (asc): {}\n".format(ins_sorted))
    np.random.shuffle(values)
    py_sorted = sorted(values)

if __name__=="__main__":
    main()
