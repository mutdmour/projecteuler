day = 0
month = 1
year = 1900
week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
week_counter = -1
leapyear = False
sunday_counter = 0
while year >= 1900 and year <= 2000:
    day = day + 1
    week_counter = week_counter + 1
    week_day = week[week_counter]
    if week_counter == 6:
        week_counter = -1
    if year % 4 == 0:
        if year % 100:
            if year % 400:
                leapyear = True
        else:
            leapyear = True
    if month == 4 or month == 9 or month == 11 or month == 6:
        month_limit = 30
    elif month == 2:
        if leapyear == False:
            month_limit = 28
        else:
            month_limit = 29
    else:
        month_limit = 31
    leapyear = False
    if day == month_limit:
        day = 1
        month = month +1
        if month == 13:
            month = 1
            year = year + 1
    if week_counter == -1 and day == 1 and year >= 1901:
        sunday_counter = sunday_counter + 1
#        print(week_day, day, month, year)

print(sunday_counter)
        
          
