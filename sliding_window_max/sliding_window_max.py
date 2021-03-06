'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max_initial(nums, k):
    results = []
    # loop over array
    for i in range(len(nums)):
        # get each set of 3 items
        window = nums[i:i+k]
        if len(window) == k:
            # find max of those 3 items
            maximum = max(window)
            # append max to results array
            results.append(maximum)
    return results


def sliding_window_max(nums, k):
    num_sets = len(nums) - (k - 1)  # number of windows that fit in array
    windows = [None for x in range(num_sets)]
    results = []

    for i in range(len(windows)):
        windows[i] = nums[i:i+k]

    for i in range(len(windows)):
        results.append(max(windows[i]))

    return results


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    # Expected Output: [3,3,5,5,6,7]

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
