# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a, b, c):
    return max(a, b, c)

result = max_num(1, 2, 3)
print("The maximum number is", result)

# Write a Python function called mult_list() to multiply all the numbers in a list.
def multi_list(a, b, c):
    return a * b * c

result = multi_list(1, 2, 3)
print("The multiplied number is", result)

# Write a Python function called rev_string() to reverse a string.
def rev_string(input):
    return input[::-1]

original_string = "Hello"
reversed_string = rev_string(original_string)
print(reversed_string)
print(original_string)

# Write a Python function called num_within() to check whether a number falls in a given range.
def num_within(number, start_range, end_range):
    return start_range <= number <= end_range

print(num_within(3, 2, 4))
print(num_within(3, 1, 3))
print(num_within(10, 2, 5))

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
def pascal(n):
    if n <= 0:
        print("Number of rows should be a positive integer.")
        return

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            value = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(value)
        row.append(1)
        triangle.append(row)

# Print triangle
    for row in triangle:
        print(' '.join(map(str, row)).center(n*3))

pascal(2)
pascal(5)