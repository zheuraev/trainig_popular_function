def factorial(a):
    if a == 1:
        return 1
    else:
        return factorial(a - 1)*a

def main():
    print(factorial(993))

if __name__ == '__main__':
    main()