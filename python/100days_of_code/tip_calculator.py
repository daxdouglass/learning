print("Welcome to the tip calculator")

total = input("What was the total bill? $")
people = input("How many people to split the bill? ")
percentage = input(
    "What percentage tip would you like to give? 10, 12, or 15? ")

if percentage == "10":
    tip = .1
    print("Each person should pay $" +
          str((float(total) / int(people)) * float(tip)))
elif percentage == "12":
    tip = .12
    print("Each person should pay $" +
          str((float(total) / int(people)) * float(tip)))
elif percentage == "15":
    tip = .15
    print("Each person should pay $" +
          str((float(total) / int(people)) * float(tip)))
