n=100
from random import randint

print('\n'.join(map(str,[n]+[randint(1,10**9) for _ in range(n)])))