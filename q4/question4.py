def factorial(n) :
    if n <= 1:
        return n
    else:
        return n * factorial(n - 1)

if __name__ == '__main__':
    for i in range (0, 15, 2):
        print(str(i) + "! = " + str(factorial(i)))