def convert_to_24_hour(hour, minute, period):
    if period == "am":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12
    
    return "{:02d}{:02d}".format(hour, minute)

print(convert_to_24_hour(1, 00, "pm")) 
