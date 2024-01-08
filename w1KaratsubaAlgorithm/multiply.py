def karatsuba_multiplication(x, y):
    if x < 10 or y < 10:
        return x * y

    # Determine the length of the numbers
    n = max(len(str(x)), len(str(y)))
    n2 = n // 2

    # Split x and y into smaller parts
    a = x // 10**n2
    b = x % 10**n2
    c = y // 10**n2
    d = y % 10**n2

    # Calculate sub-products
    ac = karatsuba_multiplication(a, c)
    bd = karatsuba_multiplication(b, d)
    ad_plus_bc = karatsuba_multiplication(a + b, c + d) - ac - bd

    # Calculate the final result
    result = ac * 10**(2*n2) + ad_plus_bc * 10**n2 + bd
    return result

# Set the values of the two numbers to be multiplied
num1 = 3141592653589793238462643383279502884197169399375105820974944592
num2 = 2718281828459045235360287471352662497757247093699959574966967627

# Call the Karatsuba multiplication function and print the result
result = karatsuba_multiplication(num1, num2)
print(result)
