# INFOSYS SPRINGBOARD
# Programming Fundamentals using Python - Part 1
# EXERCISES

# Selection Control Structures
def display(num):
    if num % 3 == 0 and num % 5 == 0:
        return "Zoom"
    elif num % 3 == 0:
        return "Zip"
    elif num % 5 == 0:
        return "Zap"
    else:
        return "Invalid"
    
print(display(10))
print(display(12))
print(display(45))
print(display(30))


# Iteration Control Structures
def find_sum_of_digits(number):
    sum_of_digits = 0
    while number > 0:
        sum_of_digits += number % 10
        number //= 10
    return sum_of_digits

print(find_sum_of_digits(0))      
print(find_sum_of_digits(123))    
print(find_sum_of_digits(78975))  
print(find_sum_of_digits(780))    


# Collections and List in Python
def get_count(num_list):
    count = 0
    for i in range(len(num_list) - 1):
        if num_list[i] == num_list[i + 1]:
            count += 1
    return count

print(get_count([2, 4, 1, 6, 9]))
print(get_count([23, 23, 6, -7, -7, 8, 0, 0]))


# String in Python
def generate_ticket(airline, source, destination, no_of_passengers):
    tickets = []
    src_code = source[:3].capitalize()  
    dest_code = destination[:3].capitalize()  
    start_number = 101  
    
    for i in range(start_number, start_number + no_of_passengers):
        ticket = f"{airline}:{src_code}:{dest_code}:{i}"
        tickets.append(ticket)

    if no_of_passengers < 5:
        return tickets
    else:
        return tickets[-5:]
print(generate_ticket('AI', 'Bangalore', 'London', 10))  
print(generate_ticket('BA', 'Australia', 'France', 2))  


# Dictionary in Python
def translate(bilingual_dict, english_words_list):
    swedish_words_list = []
    for word in english_words_list:
        if word in bilingual_dict:
            swedish_words_list.append(bilingual_dict[word])
        else:
            swedish_words_list.append("Not found")

    return swedish_words_list
bilingual_dict = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "ar"}
english_words_list = ["merry", "christmas"]

print("The bilingual dict is:", bilingual_dict)
print("The english words are:", english_words_list)
swedish_words_list = translate(bilingual_dict, english_words_list)
print("The equivalent Swedish words are:", swedish_words_list)


# Libraries & Functions in Python
def find_number_of_combination(number_of_flavours):
    total_combination = 2 ** number_of_flavours
    return total_combination
number_of_combination = find_number_of_combination(6)
print(number_of_combination)


# String in Python

def count_names(name_list):
    count1 = 0 
    count2 = 0  
    for name in name_list:
        if len(name) == 3 and name.endswith('at'):
            count1 += 1
        if 'at' in name:
            count2 += 1
    print("_at -> ", count1)
    print("%at% -> ", count2)
name_list = ["Hat", "Cat", "rabbit", "matter"]
count_names(name_list)


















# print("hello world!")

# import speedtest
# test = speedtest.Speedtest()
# download = test.download()
# upload = test.upload()
# print(f"Download Speed: {download}")
# print(f"Upload Speed: {upload}")


# from speedtest import Speedtest

# test = Speedtest()
# print(test.download(), test.upload())

# import pyautogui as pg
# import time as t
# t.sleep(5)
# print(pg.position())