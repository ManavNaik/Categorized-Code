# No. in Figure
# 1,000,000,000 one billion
# 100,000,000 one hundred million
# 10,000,000 ten million
# 1,000,000 one million
# 100,000 hundred thousand
# 10,000 ten thousand
# 1,000 one thousand
# 100 hundred
# 10 ten
# 1 one

n = input("Enter number up to 10 digit:- ")
arr = []
for i in n:
    arr.append(i)

ones = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
    }

tens = {
    10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
    15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"
}

above_tens = {
    20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
    60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
}

m = 0
print(arr)
for i in n:
    m = m + 1

if m < 2:
    # print(ones[int(n)])
    print(ones[arr[0]])
elif m < 3:
    print(tens[int(n)])
# elif m < 4:
    # print(ones[arr[0]], "hundred", tens[int(n)])
    # print(ones[arr[0]])








# print(m)


# def number_to_words(num):
#     # Dictionaries for numbers to words
#     ones = {
#         0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
#         5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
#     }

#     tens = {
#         10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
#         15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"
#     }

#     above_tens = {
#         20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
#         60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
#     }

#     if num < 10:
#         return ones[num]
#     elif num < 20:
#         return tens[num]
#     elif num < 100:
#         if num % 10 == 0:
#             return above_tens[num]
#         else:
#             return above_tens[num // 10 * 10] + "-" + ones[num % 10]
#     else:
#         return "Number out of range"

# # Test the function
# number = 93
# print(number_to_words(number))
