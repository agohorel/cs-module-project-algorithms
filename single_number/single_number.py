'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # sort elements
    arr = sorted(arr)
    # loop over and alternate adding and subtracting each elem to cancel pairs
    result = int()
    for idx,v in enumerate(arr):
        if idx % 2 == 0:
            result += v
        else:
            result -= v

    return result


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]
    arr = [1, 5, 4, 4, 1, 5, 0, 3, 9, 3, 0]

    print(f"The odd-number-out is {single_number(arr)}")