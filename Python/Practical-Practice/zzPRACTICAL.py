# import math
# x = 45
# y = 5
# z = 12.45

# print(math.ceil(z))
# print(math.copysign(x,y))
# print(math.cos(x))
# print(math.exp(x))
# print(math.factorial(x))
# print(math.floor(z))
# print(math.fmod(x,y))
# print(math.gcd(x))
# print(math.log(x,y))
# print(math.log2(x))
# print(math.log10(x))
# print(math.pow(x,y))
# print(math.remainder(x,y))
# print(math.sqrt(x))
# print(math.sin(x))
# print(math.tan(x))

# d1 = {1:10,2:20}
# d2 = {4:40,3:30}
# d3 = {5:50,1:60}
# d4 = {}

# print(sorted(d1))
# print(sorted(d1,reverse = True))

# d4.update(d1)
# d4.update(d2)
# d4.update(d3)
# print(d4)

# s1 = set(d1)
# s3 = set(d3) 
# d4 = s1 | s3
# print(d4)

# for key in d3:
#     if key in d1:
#         d3[key] = d3[key] + d1[key]
# for key in d1:
#     if key in d3:
#         d1[key] = d1[key] + d3[key]
# d4.update(d1)
# d4.update(d3)
# print(d4)

# L = [{1:10},{2:20},{4:40},{3:40},{5:50},{1:60}]
# print(L)
# u_value = set(val for dict in L for val in dict.values())
# print(u_value)

# from collections import Counter
# k = Counter(d4)
# high = k.most_common(3)
# for i in high:
#     print(i[0],":- ",i[1]," ")



def uplp():
    m = 0
    n = 0
    s  = input("Enter str:- ")
    for i in s :
        if (i.isupper() == True):
            n = n + 1
        else:
            m = m+1
    print("upper",n)
    print("Lower",m)
uplp()

