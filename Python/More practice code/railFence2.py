task = input("1. Encryption\n2. Decryption\n\nEnter task number: ")

if task == "1":
    input_str = input("Enter string: ")
    arr1 = input_str[::2]  # Take every second character starting from index 0
    arr2 = input_str[1::2]  # Take every second character starting from index 1
    # Concatenate both parts and print
    op_str = arr1 + arr2
    print("".join(op_str))

elif task == "2":
    input_str = input("Enter string: ")
    half_len = (len(input_str) + 1) // 2  # Determine the split point for odd/even length
    arr1 = input_str[:half_len]  # First half (including middle if odd length)
    arr2 = input_str[half_len:]  # Second half
    op_str = []

    # If lengths are not equal, interleave characters from both parts
    if len(arr1) != len(arr2):
        for i in range(len(arr1)):
            op_str.append(arr1[i])
            if i < len(arr2):
                op_str.append(arr2[i])
    else:
        for i in range(len(arr1)):
            op_str.append(arr1[i])
            op_str.append(arr2[i])

    print("".join(op_str))

else:
    print("Invalid input")