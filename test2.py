
def awesome(int):
    if int >= 0:
        pass
    else:
        raise Exception

    if int % 3 == 0 and int % 5 == 0:
        return 'fizzbuzz'

    if int % 3 == 0:
        return 'fizz'

    if int % 5 == 0:
        return 'buzz'

    return int


