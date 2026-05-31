import json
from datetime import datetime

name = input("Enter your name: ")

print(f"\nHello {name}! Welcome to Smart Student Assistant")

tips = [
    "Study for 45 minutes and take a 5 minute break.",
    "Practice coding daily.",
    "Make short notes for revision."
]

quotes = [
    "Success is the sum of small efforts repeated every day.",
    "Believe in yourself.",
    "Your future is created by what you do today."
]

while True:
    print("\n1. Generate Study Tip")
    print("2. Generate Motivation Quote")
    print("3. Display Current Date & Time")
    print("4. Exit")

    choice = input("Choose an option: ")

    output = ""

    if choice == "1":
        output = tips[0]
        print(output)

    elif choice == "2":
        output = quotes[0]
        print(output)

    elif choice == "3":
        output = str(datetime.now())
        print(output)

    elif choice == "4":
        break

    else:
        print("Invalid Choice")

    with open("output.txt", "a") as file:
        file.write(output + "\n")