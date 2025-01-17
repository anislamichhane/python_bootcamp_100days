print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child ticket are $5.")
    elif age <= 18:
        bill = 7
        print("Youth ticket are $7.")
    else:
        bill = 12
        print("Adult ticket are $12.")

    want_photo = input("Do you want to take a photo? \n Type y for yes and n for no. ")
    if want_photo == "y":
     # Add $3 to their bill
        bill += 3
    print(f"Your final bill is ${bill}")

else:
    print("Sorry you cannot ride the rollarcoaster.")