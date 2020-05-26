while True:
    try:
        number = int(input('Enter number: '))
        result = number / 2
        print(result)
        break
    except Exception:
        print('It must be a number > 0')
