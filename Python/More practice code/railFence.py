task = input("1.Encryption\n2.Decryption\n\nEnter task number:- ")
if task == "1":
    str = input("Enter string:- ")
    arr1 = []
    arr2 = []
    opStr = ""
    for i in range (len(str)):
        if (i%2) == 0:
            arr1.append(str[i])
        else:
            arr2.append(str[i])
    for i in range (len(arr1)):
        opStr = opStr + arr1[i]
    for i in range (len(arr2)):
        opStr = opStr + arr2[i]
    print(opStr)
elif task == "2":
    str = input("Enter string:- ")
    strlen = ((len(str))/2)+0.5
    arr1 = []
    arr2 = []
    opStr = ""
    for i in range (int(strlen)):
        arr1.append(str[i])
    for i in range (int(strlen),int(len(str))):
        arr2.append(str[i])
    if len(arr1) != len(arr2):
        for i in range (len(arr1)):
            opStr = opStr + arr1[i]
            if i == len(arr1)-1:
                break
            opStr = opStr + arr2[i]
    else:
        for i in range (len(arr1)):
            opStr = opStr + arr1[i]
            opStr = opStr + arr2[i]           
    print(opStr)
else:
    print("invalid input")