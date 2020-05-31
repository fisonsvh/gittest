import random as r
import time as t

print("I can guess your password!")
t1 = t.time()
while True:
    inp = int(input("Enter your password: \n"))
    guess = None
    tries = []
    x = 0
    while guess != inp:
        guess = r.randint(1, 9999)
        tries.append(guess)
        x += 1
        print(f'{x} try is – {guess}')
    if guess == inp:
        print(f'Your password is {guess}')
    t2 = t.time()
    print(f'Time needed – {t2 - t1}')
    print(f'Tries – {len(tries)}')
