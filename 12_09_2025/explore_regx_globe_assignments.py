import glob
import re

#Assignment 1: List All .txt Files and Check for a Word using glob + re.search
print("*" *50)
print("Assignment #1: List All .txt Files and Check for a Word using glob + re.search")
print("*" *50)
files = glob.glob("*.txt", recursive=True)
print(files)

for item in files:
    match = re.search("python", item)
    if match:
        print("Found keyword", item)

#Assignment 2: Match File Names Using re.match
print("*" *50)
print("Assignment #2: Match File Names Using re.match")
print("*" *50)
files = glob.glob("*.*", recursive=True)
print(files)

pattern = re.compile("")
for item in files:
    match = re.match(r"^data_.*\.csv$", item)
    if match:
        print("Found keyword:", item)

#Assignment 3: Validate Phone Numbers with re.match
print("*" *50)
print("Assignment #3: Validate Phone Numbers with re.match")
print("*" *50)
phone_list =  ["(123) 456-7890", "(193) 456-7790", "(091) 456-7490" , "(456 456-890"]

for phone in phone_list:
    match = re.match(r'^\(\d{3}\) \d{3}-\d{4}$', phone)
    if match:
        print("Found valid phone number = ", phone)
    else:
        print("Phone not in valid format = ", phone)
