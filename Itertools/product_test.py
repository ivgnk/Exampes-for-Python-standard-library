from itertools import product

res=list(product([0,1], repeat=3))
print(f'{len(res)=}')
print(res)

res=list(product('ABC', repeat=2))
print(f'{len(res)=}')
print(res)
