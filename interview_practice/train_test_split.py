import random

def split_data(data, split_ratio):
    """
    split_ratio is the ratio of test to train samples.
    """
    
    assert 0 <= split_ratio <= 1
    assert data
    test_size = int(len(data)*split_ratio)
    print('target test_size = {}'.format(test_size))
    test = list()
    train = list(data)
    while len(test) < test_size:
        rand_index = random.randrange(len(train))
        test.append(train.pop(rand_index))

    print('split into {} test, {} train'.format(len(test), len(train)))

    return train, test



if __name__ == '__main__':
    this_data = [random.randrange(10) for _ in range(10000)]
    this_split_ratio = 0.3

    print('Starting with {} samples'.format(len(this_data)))
    
    train, test = split_data(this_data, this_split_ratio)
    
    print("split ratio: {}".format(this_split_ratio))
    print("actual: {}".format(len(test)/len(this_data)))

