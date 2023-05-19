import math
def add_time(start, duration, week = False) :
    weekDays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    startTime = start.split()
    startTimeS = startTime[0].split(':')
    startH = int(startTimeS[0])
    startM = int(startTimeS[1])
    operand = startTime[1]

    weekdayIndex = 0

    try :
        weekday = week.lower()
    except :
        weekday = ''
    
    if weekday in weekDays :
        weekdayIndex = weekDays.index(weekday)
    
    durationTime = duration.split(':')
    durationH = int(durationTime[0])
    durationM = int(durationTime[1])
    
    newH = 0
    displH = 0
    newM = 0
    newO = 'AM'
    newD = ''
    daysLater = ''
    new_time = 0

    if operand == 'AM' :
        newH = startH + durationH + (math.floor((startM + durationM) / 60))
    elif operand == 'PM' : 
        newH = startH + durationH + (math.floor((startM + durationM) / 60 + 12))


    if weekday in weekDays :
        if newH >= 24 :
            weekdayIndex = weekdayIndex + math.floor(newH / 24)
            if weekdayIndex > len(weekDays) :
                weekdayIndex = weekdayIndex % 7
            newD += weekDays[weekdayIndex].capitalize()
        else :
            newD += weekDays[weekdayIndex].capitalize()

# Calculations of an amount of hours after time
    if newH < 24 :
        new_time = f'{newH}:{newM} {newO}'
    elif newH >= 24 and newH < 48:
        daysLater += ' (next day)'
    elif newH >= 48 :
        daysLater = f' ({math.floor(newH / 24)} days later)'

# assigning display hour
    if newH >= 24 :
        displH = newH % 24
    else :
        displH = newH

    newM = (startM + durationM) % 60

    if displH >= 12 :
        displH -= 12
        newO = 'PM'
    elif displH < 12 :
        newO = 'AM'

    if displH == 0 :
        displH = 12

    if newM < 10 :
        newM = f'0{newM}'

    if newH < 24 :
        new_time = f'{displH}:{newM} {newO}'

    elif newH >= 24 :
        new_time = f'{displH}:{newM} {newO}{daysLater}'

    if week != False :
        new_time = f'{displH}:{newM} {newO}, {newD}{daysLater}'

    return new_time

print(add_time("11:59 PM", "24:05", "Wednesday"))