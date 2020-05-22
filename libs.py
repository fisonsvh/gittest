def get_count(string, symbol):
    cnt = 0;
    for i in string:
        if i == symbol:
            cnt = cnt + 1
    return cnt


def get_len(string):
    cnt = 0
    for i in string:
        cnt += 1
    return cnt


def len_name(name):
    return len(name)
