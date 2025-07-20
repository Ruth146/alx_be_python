task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unspecified priority"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif time_bound == "no":
    reminder += ". Consider completing it when you have free time."
else:
    reminder += " (time sensitivity not specified)."

print("\nReminder:", reminder)

while True:
    again = input("\nDo you want to enter another task? (yes/no): ").lower()
    if again == "yes":
        task = input("Enter your task: ")
        priority = input("Priority (high/medium/low): ").lower()
        time_bound = input("Is it time-bound? (yes/no): ").lower()

        match priority:
            case "high":
                reminder = f"'{task}' is a high priority task"
            case "medium":
                reminder = f"'{task}' is a medium priority task"
            case "low":
                reminder = f"'{task}' is a low priority task"
            case _:
                reminder = f"'{task}' has an unspecified priority"

        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        elif time_bound == "no":
            reminder += ". Consider completing it when you have free time."
        else:
            reminder += " (time sensitivity not specified)."

        print("\nReminder:", reminder)
    elif again == "no":
        print("Good job completing your tasks!")
        break
    else:
        print("Please answer with 'yes' or 'no'.")
