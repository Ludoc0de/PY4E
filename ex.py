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
