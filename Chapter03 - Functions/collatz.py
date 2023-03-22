def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

print('Enter number:')
try:
    number = int(input())
    while number != 1:
        number = collatz(number)
        print(number)
except ValueError:
    print('You must enter an integer.')