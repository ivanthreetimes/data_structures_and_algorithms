"""
Write a function that calculates the sum and product of
all elements in a tuple of numbers.

Example:
    input_tuple = (1, 2, 3, 4)
    sum_result, product_result = sum_product(input_tuple)
    print(sum_result, product_result)

Expected output:
    10, 24
"""


def sum_product(input_tuple):
    sum_t = 0
    prod_t = 1
    for el in input_tuple:
        sum_t += el
        prod_t *= el
    return sum_t, prod_t


input_t = (1, 2, 3, 4)
sum_result, product_result = sum_product(input_t)
print(sum_result, product_result)
