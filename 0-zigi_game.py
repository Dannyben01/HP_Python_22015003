while True:
    for i in range(1, 21):
        print('*' * 10 + ' ' * i + '*' * 10)
        time.sleep(0.1)
    for i in range(20, 0, -1):
        print('*' * 10 + ' ' * i + '*' * 10)
        time.sleep(0.1)
