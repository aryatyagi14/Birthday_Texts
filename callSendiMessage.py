import subprocess
import datetime
from collections import namedtuple
import random

# We need to store Name, Birthday (Month, Day), Number 
MonthDay = namedtuple('MonthDay', ['Month', 'Day'])
Birthday = namedtuple('Birthday', ['Name', 'MonthDay', 'Number'])

# Create a List of Possible Messages
messages = [
    "Happy Birthday!!!!",
    "HAPPY BIRTHDAY! I Hope you have the BEST DAY EVER!!",
    "Happy Birthday :))",
]

# Create List of Birthdays
birthdayList = [
    Birthday('John Doe', MonthDay(1, 20), '1234567890'),
    # Add more People here if needed!
]

# Loop through all the birhtdays
for birthday in birthdayList:
    today = datetime.date.today()
    todayMonthDay = MonthDay(today.month, today.day)
    # Check if today is someones bday
    if (todayMonthDay == birthday.MonthDay) :
        message = random.choice(messages)
        # Call the AppleScript application
        subprocess.run(
            ["osascript", "SendiMessage.app", birthday.Number, message])


