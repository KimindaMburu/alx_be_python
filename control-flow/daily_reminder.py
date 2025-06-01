# Prompt for a single task
task = input("Enter the task description: ")
priority = input("Enter the task’s priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Initialize reminder message based on priority
match priority:
    case "high":
        reminder = f"Task '{task}' is high priority"
    case "medium":
        reminder = f"Task '{task}' is medium priority"
    case "low":
        reminder = f"Task '{task}' is low priority"
    case _:
        reminder = f"Task '{task}' has an unknown priority"

# Modify reminder if task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Print the customized reminder
print(reminder)
