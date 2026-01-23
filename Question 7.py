def time_convertor(seconds):
    hours = seconds // 3600 #used floor division to divide seconds and leave a whole number
    minutes = seconds // 60
    while minutes >= 60: #loops while the minutes are greater than 60 (1 hour)
        minutes -=60 #subtracts 60 minutes until the minutes is under an hour
        if minutes == 60:
            minutes = 0 #sets the minutes to 0 is minutes is equal to 60 (1 hour)
    while seconds >= 60:#loops while the seconds are greater than 60 (1 minute)
        seconds -=60 #subtracts 60 seconds until the seconds is under a minute
        if seconds == 60:
            seconds = 0 #sets the minutes to 0 is minutes is equal to 60 (1 minute)
    if hours > 12:
        am_or_pm = "PM" #checks if the hours is greater than 12 and sets the time of day to be PM
        hours -= 12 # subtracts 12 hours to change to 12 hour time
    else:
        am_or_pm = "AM" #checks if the hours is less than 12 and sets the time of day to be AM
    return f"{hours:00d}:{minutes:002d}:{seconds:002d}:{am_or_pm}" #returns the time with padded zeros if the number is shorter than 2 digits

print(time_convertor(46800))
