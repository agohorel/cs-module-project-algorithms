'''
Input: a List of integers
Returns: a List of integers
'''

def product_of_all_other_numbers(arr):
    result = [1 for i in arr]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j] != 0:
                result[i] *= arr[j]
   
        if arr[i] > 0:
            result[i] *= 1/arr[i]

    for i in range(len(result)):
        result[i] = int(result[i])

    print(result)
    return result


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]
    arr = [1, 7, 3, 4]
    # expected output: [84, 12, 28, 21]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

# input
[1, 2, 3]

# desired output
[6, 3, 2]

# if you multiplied every item by every other item
[6, 6, 6]

# if you divide each item by it's original value:
[6, 3, 2]

# we can divide w/ multiplication via reciprocals ( n * (1/x))
# but that still uses division... clarify
