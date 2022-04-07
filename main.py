print("Welcome to Adventure!")
name = input("What is your Characters name? ")
age = int(input("What is your age? "))

print("Hello", name, "you are", age, "years old.")

if age >= 18:
    print("You are old enough to play!")
    want_to_play = input("Do you want to play a game? ").lower()
    if want_to_play == "yes":
        print("Let's play!")

    else:
        print("Cya...")

else:
    print("You are not old enough to play...")
