# Write a function to determine the longest common subsequence between two
# strings.


def longest_common_subsequence(s1, s2):

    assert isinstance(s1, str)
    assert isinstance(s2, str)
    
    start = 0
    min_len = min(len(s1), len(s2))
    max_subsequence = ''
    
    while start < min_len:
        end = start
        sequence = ''
        while end < min_len and s1[end] == s2[end]:
            sequence += s1[end]
            if len(sequence) > len(max_subsequence):
                max_subsequence = sequence
            end += 1
        # If we did not find a sequence, increment the start index
        if start == end:
            start += 1
        else:
            start = end

    return max_subsequence


if __name__ == '__main__':

    s1 = 'eeebaceeaalskjdfal;skdjfalskjdfdkkdifiwewet0onasn0wgh4ignkvaskndvlakwengeeee'
    s2 = 'hhhbacedwqeihf9qwhf9wafjasdjfal;sdkjgsa0ghas0dijas;ldfjal;sdjfkddddddd'

    print(longest_common_subsequence(s1, s2))

