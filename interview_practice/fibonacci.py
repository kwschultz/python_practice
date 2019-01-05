

def naive_fibonacci(N):
    assert isinstance(N, int)
    if N<1:
        return []
    elif N == 1:
        nums = [1]
        return nums
    elif N == 2:
        nums = [1, 1]
        return nums
    else:
        nums = [1, 1]
        for i in range(N-2):
            nums.append(nums[i] + nums[i+1])
        return nums

if __name__ == '__main__':
    N = 32
    print(naive_fibonacci(N))

