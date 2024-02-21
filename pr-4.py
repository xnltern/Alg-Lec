n = int(input())
a = 0
b = 1
i = 2
while i != n:
    b = a + b
    a = b - a
    i +=1
    print(b)
