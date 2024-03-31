# Python program prompts the user to input a list of numbers, 
# provides options to view the list or perform addition/subtraction operations on 
# selected numbers from the list, and incorporates error handling for input validation.

# Initialize an empty list to store numbers
list = []

# Get the number of elements the user wants to add to the list
while True:
    try:
        number = int(input("How many numbers do you want to add to the list? "))
        # Loop to get user input for each element and append it to the list
        for i in range(number):
            your_input = float(input(f"Enter number {i + 1}: "))
            list.append(your_input)
        break
    except ValueError:
        print("Error, please enter a valid number")
        continue

print()
print("You can enter 'add', 'subs', 'mult', 'div' if you want to perform operations on the numbers.")
print()

# Display the list if the user wants to see it
while True:
    choice = input("Press 'yes' if you want to see your list or 'no' if you don't want that: ")
    if choice.lower() == "yes":
        print(list)
        print()
        break
    elif choice.lower() == "no":
        break
    else:
        print("Error! Please enter 'yes' or 'no'")
        continue

list1 = []
operation = input("What operation do you want to perform? ")

if operation.lower() == "add" or operation.lower() == "subs":
    while True:
        try:
            choice_num = int(input(f"How many numbers do you want to {operation} from the list? "))
            break
        except ValueError:
            print("Error! Please enter a valid number")
            continue

    # Loop to get user input for positions and display corresponding numbers
    for i in range(choice_num):
        while True:
            try:
                num = int(input(f"Position for number {i + 1}: "))
                print(f"The number for that position is {list[num]}")
                print()
                list1.append(list[num])
                break
            except IndexError:
                print("Error! Please enter a valid position")
                continue

    print(list1)

    # Perform addition or subtraction based on the user's choice
    if operation.lower() == "add":
        print(f"The sum is: {sum(list1)}")
    elif operation.lower() == "subs":
        num = 1
        num1 = num * list1[0]
        for i in range(len(list1) - 1):
            num1 = num1 - list1[i + 1]
        print(f"The result of subtraction is: {num1}")
