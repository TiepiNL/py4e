from datetime import datetime

current_day = datetime.now().day
current_month = datetime.now().month

# Greetings
merry_xmas = "Merry Christmas"
happy_ny = "Happy New Year"

# val1 = month, val2 = day, val3 = greeting
events = {
    "Christmas Eve": [12, 24, merry_xmas],
    "Christmas Day": [12, 25, merry_xmas],
    "Second Day of Christmas": [12, 26, merry_xmas],
    "New Year's Day": [1, 1, happy_ny]
}

for key,val in events.items():
    if current_month == val[0] and current_day == val[1]:
        print("It's", key)
        greeting = f"{val[2]}!"
        print(greeting)
