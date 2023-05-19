import math
def add_time(start, duration, week = False) :
    weekDays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    startTime = start.split()
    startTimeS = startTime[0].split(':')
    startH = int(startTimeS[0])
    startM = int(startTimeS[1])
    operand = startTime[1]

    weekday = week.lower()
 #   print(weekDays[weekDays.index(weekday)+1])
    
    durationTime = duration.split(':')
    durationH = int(durationTime[0])
    durationM = int(durationTime[1])
    
    newH = 0
    newM = 0
    newO = 'AM'
    newD = ''
  #  print(durationH)
    new_time = ''

    newH = startH + durationH + (math.floor((startM + durationM) / 60))

    if weekday in weekDays :
        if newH >= 24 :
            newD += weekDays[weekDays.index(weekday)+1].capitalize()

    print(newD)


    if newH >= 24 :
        newH = newH % 24

    newM = (startM + durationM) % 60

    if newH >= 12 :
        newH -= 12
        newO = 'PM'
    else :
        newO = 'AM'











    new_time = f'{newH}:{newM} {newO}'

    return new_time

print(add_time("23:40 PM", "00:40", 'Monday'))