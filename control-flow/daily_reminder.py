# daily_reminder.py

while True:
    # Prompt for task, priority, and time sensitivity
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Process the task using match-case
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"\nReminder: '{task}' is a high priority task that requires immediate attention today!\n")
            else:
                print(f"\nReminder: '{task}' is a high priority task. Try to address it as soon as possible.\n")
        case "medium":
            if time_bound == "yes":
                print(f"\nReminder: '{task}' is a medium priority task that needs to be handled today.\n")
            else:
                print(f"\nReminder: '{task}' is a medium priority task. Plan to complete it soon.\n")
        case "low":
            if time_bound == "yes":
                print(f"\nReminder: '{task}' is a low priority but time-bound task. Don't forget to finish it today.\n")
            else:
                print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.\n")
        case _:
            print("\nInvalid priority entered. Please use high, medium, or low.\n")

    # Optionally allow the user to do another reminder
    repeat = input("Would you like to enter another task? (yes/no): ").strip().lower()
    if repeat != "yes":
        print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
        break

