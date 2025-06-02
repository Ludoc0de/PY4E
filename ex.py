# largest = None
# smallest = None
# while True:
#     num = input("Enter a number: ")
#     if num == "done":
#         break
#     try:
#         num = int(num)
#         if largest is None or num > largest:
#             largest = num
#         if smallest is None or num < smallest:
#             smallest = num
#     except:
#         print("invalid")

# print("Maximum is", largest)
# print("Minimum is", smallest)

# fruit = "banana"
# index = len(fruit) - 1
# while index >= 0:
#     letter = fruit[index]
#     print(letter)
#     index = index - 1

# fruit = "banana"
# Exercise 3: Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.

# def count(test, word):
#     count = 0
#     for letter in word:
#         if letter == test:
#             count = count + 1
#     return count


# test = count("n", "banana")
# print(test)

# Exercise 4: There is a string method called count that is similar to the function in the previous exercise. Read the documentation of this method at

# word = "banana"
# print(word.count("b"))

# Slicing strings
# Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence: 0.8475'
# Use and string slicing to extract the portion of the string after the colon character and then use the function to convert the extracted string into a floating point number.

# str = "X-DSPAM-Confidence: 0.8475"
# print(str.find(" "))
# print(str.find("5"))
# sliceStr = str[20:26]
# number = float(sliceStr)
# print(number)

# Write a program to read through a file and print the contents of the file (line by line) all in upper case. Executing the program will look as follows:
# fHandle = open("mbox.txt")
# rHandle = fHandle.read()
# print(rHandle[0:20].upper())

# Write a program to prompt for a file name, and then read through the file and look for lines of the form:X-DSPAM-Confidence: 0.8475
# fName = input("enter your file name: \n")
# fHandle = open(fName)
# number = 0
# count = 0
# for lines in fHandle:
#     if lines.startswith("X-DSPAM-Confidence"):
#         # print(lines)
#         pos = lines.find("0")
#         number = number + float(lines[pos:])
#         # print(number)
#         count = count + 1
# print(number)
# print(count)
# averageNumber = number / count
# print(averageNumber)

# add an Easter Egg to the program
fName = input("enter your file name: \n")
fHandle = "null"
try:
    if fName == "Which pill?":
        print("hey !!!! How did you ind my easter egg word ?!")
    elif fName:
        fHandle = open(fName)
        print(fHandle)
except:
    print("excuse me ? Error file name")
