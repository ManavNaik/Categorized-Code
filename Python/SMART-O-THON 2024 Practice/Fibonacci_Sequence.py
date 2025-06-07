# 0, 1, 1, 2, 3, 5, 8, 13, 21

m = 0
n = 1
print(m)
print(n)
i = 0

def add():
    global m , n
    v = m + n
    m = n
    n = v
    print(v)

while i<7:
    add()
    i = i + 1