# Felix Muzny
# DS 2001 - CS
# Sept 15/16, 2021
# Practicum 2 - Variables etc

def main():
    # Task 1: Help Waldo out!
    
    # 1.1
    # Error: Name "x" is not defined 
    x = 7
    print(x)
    
    # 1.2
    # Error: num 3 is not defined, then num3 is still not defined
    num1 = 0
    num2 = 1
    num3 = num2 + num2
    num3 = num1 + num2 + num3
    print(num3)
    
    # 1.3
    # Error: TypeError: can only concatenate str (not "int") to str
    text1 = "Harriet the spy's favorite number is"
    text2 = input("Harriet's favorite number: ")
    print(text1 + text2)
    text2 = int(text2) # can also move this line to the end
    print(text1, text2)
    
    # 1.4
    # Error: NameError: name 'feet' is not defined
    # Error:
    feet = input("How many feet? ")
    feet = int(feet) # Attention! should also fix this line!
    inches = feet * 12
    inches = str(inches) # Attention! should also fix this line!
    print("That's " + inches + " inches!")
    
    # Answer to the question about print(v1, v2) vs print(v1 + v2) goes here :)
    
    # Task 2: Dining out
    bill = float(input("How much was the bill?\n"))
    percent = float(input("What percent will everyone tip? Enter a number between 0 and 1\n"))
    people = int(input("How many people are splitting?\n"))
    total = bill * (1 + percent)
    per_person = total / people
    # to get it to always do exactly two digits, we'll need to 
    # use the string format method
    print("Everyone cough up $", round(per_person, 2), "please!")
    
    # Part 3: How long will is take to walk home?
    speed = float(input("How fast do you walk? "))
    far = float(input("How far are you from home? "))
    minutes = (1 / speed) * (60) * far
    print("With no obstacles, it will take you", minutes, "minutes to get home.")
    cats = int(input("How many angry cats? "))
    print("If you encounter", cats, "angry cats, it will take you", minutes + (5 * cats), "minutes to get home.")
        
    
    
    # Part 4: better ATM
    in_dollars = int(input("How much are you putting in?\n"))
    left = in_dollars - 2.37 # everything costs 2.37
    print("Your change is $", left)
    
    dollars = round(left // 1)
    left = (left - dollars) * 100 # convert to cents
    quarters = round(left // 25)
    left = left - (quarters * 25)
    dimes = round(left // 10)
    left = left - (dimes * 10)
    nickels = round(left // 5)
    left = left - (nickels * 5)
    pennies = round(left)
    print("I'm giving you back:")
    print(dollars, "dollars")
    print(quarters, "quarters")
    print(dimes, "dimes")
    print(nickels, "nickels")
    print(pennies, "pennies")
    
    # Part 5: Isolating digits
    num = int(input("Enter a non-negative integer:\n"))
    ones = num % 10
    tens = (num // 10) % 10
    hundreds = (num // 100) % 10
    print("hundreds =", hundreds)
    print("tens =", tens)
    print("ones =", ones)
    
main()
