input = (input("Enter No :-"))
arr = []
m = 0
for i in range(len(input)+1):
    arr.append(i)
for i in range(len(arr)):
    m += int(arr[i])
print(m)