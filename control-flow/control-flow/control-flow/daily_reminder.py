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

assert task in reminder, "Error: Reminder does not mention the task description."

assert any(p in reminder for p in ["high priority", "medium priority", "low priority", "unspecified priority"]), \
    "Error: Reminder does not include a valid priority level."

if time_bound == "yes":
    assert "immediate attention" in reminder, "Error: Reminder should mention immediate attention for time-bound task."
elif time_bound == "no":
    assert "Consider completing it when you have free time" in reminder, \
        "Error: Reminder should advise less urgency for non-time-bound task."

print("\nReminder:", reminder)
