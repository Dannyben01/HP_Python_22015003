while True:
    try:
        n = int(input('Enter an integer: '))
        break
    except ValueError:
        print('Only integer character is allowed, try again')
for i in range(1, n+1):
    print('#' * i)
