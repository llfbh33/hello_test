def factoral(n):
    if n == 0:
        return 1
    else:
        return n * factoral(n-1)

num = 5
result = factoral(num)
print("Factoral of", num, "is", result)
