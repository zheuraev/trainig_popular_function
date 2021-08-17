def palindrome(a: str):
    b = 0
    a = ''.join(a.split())
    for i in range(round(len(a)/2)):
        if a[i] == a[-1 - i]:
            b += 0
        else:
            b += 1
    if b == 0:
        print(f'Введеная строка {a} палиндром')
    else:
        print(f'Строка {a} не является палиндромом')


def main():
    a = 'vffv vffv'
    palindrome(a)


if __name__ == '__main__':
    main()