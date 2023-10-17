def exponential(x):
    def square(y):
        return y * y
    return square(x) * square(x)

print(exponential(2))