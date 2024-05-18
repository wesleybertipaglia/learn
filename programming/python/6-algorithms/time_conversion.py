def time_conversion(s):
    hour = int(s[:2])
    minute_second = s[2:8]
    time_format = s[-2:]

    if time_format == "PM":
        if hour != 12:
            hour += 12
    else:
        if hour == 12:
            hour = 0   
    
    return f"{hour:02}{minute_second}"