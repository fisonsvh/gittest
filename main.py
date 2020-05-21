s = 'Hello World'
if ' ' in s:
    s = s.upper()
else:
    s = s.lower()

print(s)


def getsum(*args):
    print(args)


print(getsum(sum(1, 5, 10)))
