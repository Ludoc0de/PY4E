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
# fHandle = open("mboxs.txt")
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
# fName = input("enter your file name: \n")
# fHandle = "null"
# try:
#     if fName == "Which pill?":
#         print("hey !!!! How did you ind my easter egg word ?!")
#     elif fName:
#         fHandle = open(fName)
#         print(fHandle)
# except:
#     print("excuse me ? Error file name")

# 8.4
# fname = input("Enter file name: ")
# fh = open(fname)
# lst = list()
# for line in fh:
#     # print(line.rstrip())
#     words = line.split()
#     for word in words:
#         if not word in lst:
#             lst.append(word)
# lst.sort()
# print(lst)

# 8.5
# fname = input("Enter file name: ")
# if len(fname) < 1:
#     fname = "mboxs.txt"

# fh = open(fname)
# # fh = open("mboxs.txt")
# count = 0
# for line in fh:
#     words = line.split()
#     if len(words) == 0:
#         continue
#     if words[0] == "From"
#     count += 1
#     print(words[1])

# print("There were", count, "lines in the file with From as the first word")

# 9.1
# fname = input("Enter file name: ")
# if len(fname) < 1:
#     fname = "words.txt"
# fh = open(fname)
# print(fh)
# # fh = open("words.txt")
# words2dict = dict()
# for line in fh:
#     words = line.split()
#     print(words)
#     for word in words:
#         words2dict[word] = 1
# print(words2dict)
# print("data" in words2dict)

# fh = open("romeo.txt")
# count = dict()
# for line in fh:
#     words = line.split()
#     for word in words:
#         count[word] = count.get(word, 0) + 1
# print(count)
# for key in count:
#     if count[key] > 2:
#         print("key > 3 :", key)

# 9.4
# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
# import string

# name = input("Enter file:")
# if len(name) < 1:
#     name = "mboxs.txt"
# handle = open(name)
# handle = open("mboxs.txt")
# counts = dict()
# for lines in handle:
#     if lines.startswith("From "):
#         second_word = lines.split()[1:2]
#         for mail in second_word:
#             counts[mail] = counts.get(mail, 0) + 1
# for key in counts:
#     if counts[key] > counts[mail] - 1:
#         print(key, counts[key])

# fh = open("mboxs.txt")
# counts = dict()
# max_count = 0
# max_email = None
# for lines in fh:
#     if lines.startswith("From:"):
#         second_words = lines.split()[1:2]
#         for mail in second_words:
#             counts[mail] = counts.get(mail, 0) + 1
# for key in counts:
#     if counts[key] > max_count:
#         max_count = counts[key]
#         max_email = key
# print(max_email, max_count)

# lst = list()
# for key, val in list(counts.items()):
#     lst.append((val, key))

# lst.sort(reverse=True)

# for key, val in lst:
#     print(key, val)

# handle = open("mboxs.txt")
# counts = dict()
# max_count = 0
# max_hour = None
# for lines in handle:
#     if lines.startswith("From "):
#         complete_time = lines.split()[5:6]
#         for time in complete_time:
#             hours = time.split(":")[0:1]
#             for hour in hours:
#                 counts[hour] = counts.get(hour, 0) + 1
# for key in counts:
#     if counts[key] > max_count:
#         max_count = counts[key]
#         max_hour = key
# print(max_hour, max_count)

# lst = list()
# for key, val in list(counts.items()):
#     lst.append((val, key))

# lst.sort(reverse=True)

# for key, val in lst:
#     print(key, val)

# import re

# handle = open("resum2225867.txt")
# total = 0
# for line in handle:
#     line = line.rstrip()
#     test = re.findall("[0-9]+", line)
#     if len(test) > 0:
#         for num in test:
#             total += int(num)

# print(total)

# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(("google.com", 80))
# cmd = "GET https://www.google.com/ HTTP/1.0\r\n\r\n".encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(), end="")

# mysock.close()

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import ssl

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# # url = input("Enter - ")
# url = "http://py4e-data.dr-chuck.net/comments_2225869.html"
# html = urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, "html.parser")

# # Retrieve all of the anchor tags
# total = 0
# lst = list()
# tags = soup("span")
# for tag in tags:
#     # Look at the parts of a tag
#     # print("TAG:", tag)
#     # print("URL:", tag.get("href", None))
#     # print("Contents:", tag.contents[0])
#     # print("Attrs:", tag.attrs)
#     span = tag.contents[0:1]
#     # print(span)
#     for number in span:
#         lst.append(number)
#         total += int(number)
# print(total)
# print(lst)

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl  # defauts to certicate verification and most secure protocol (now TLS)

# Ignore SSL/TLS certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input("Enter - ")
url = "http://py4e-data.dr-chuck.net/known_by_Zaaine.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
count = 0
tags = soup("a")
for tag in tags:
    count += 1
    # print(tag.get("href", None), count)
    if count == 18:
        link = tag.get("href", None)
        print(link)
