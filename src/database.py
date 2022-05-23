import csv
from src.deadlined_reminders import DeadlinedReminder

def list_reminders():
    f = open("reminders.csv", "r")
@@ -12,10 +13,13 @@ def list_reminders():
                print(e.ljust(32), end=' ')
        print()

def add_reminder(reminder):
    print()
    reminder = input("What would you like to be reminded about?: ")

def add_reminder(text, date, ReminderClass):
    reminder = ReminderClass(text, date)

    if not isinstance(reminder, DeadlinedReminder):
        raise TypeError('Invalid Reminder Class')


    with open('reminders.csv', 'a+', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow([reminder])
        writer.writerow(reminder)
