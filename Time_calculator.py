def add_time(start, duration, day_of_week=None ):
    
    start_time, period = start.split(' ')

    hour, minute = start_time.split(':')
    
    hour = int(hour)    
    minute = int(minute)
    print(hour,':',minute)


    # convert to 24h
    if period == 'PM' and hour != 12:
        hour +=12
    if period == 'AM' and hour == 12:
        hour = 0
    
    #add duration
    h_dur, m_dur = map(int,duration.split(':')) #convert str to in with map()
    print(h_dur, ':', m_dur)
    minute = minute + m_dur #(00 + 10 = 10)

    hour = hour + h_dur + (minute//60) # hour + h_dur (11+3 = 14 , + minute > 60 = +1hour)

    final_minute = minute % 60 
    days_later = hour // 24
    final_hour = hour % 24 #(14 -> 14/24 = 0, 10)
    print(final_hour, ':',final_minute)

    #convert back to 12am
    if final_hour == 0:
        final_hour = 12
        period = 'AM'
    elif final_hour < 12:
        final_hour = final_hour
        period = 'AM'
    elif final_hour == 12:
        final_hour = 12
        period = 'PM'
    elif final_hour > 12:
        final_hour = final_hour - 12
        period = 'PM'
    
    print('\nAfter convert back:\n',final_hour,':',final_minute)

    new_time = f'{final_hour}:{str(final_minute).zfill(2)} {period}' #zfill(2) add a leading zero  

    if day_of_week: #input day_of_week
        in_week = ['Monday','Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] #index 0-6

        #use index to handle with input list
        day_now_index = in_week.index(day_of_week.capitalize()) # take index of capitalize input (day_of_week) inside in_week -> the day we are

        new_day_index = (day_now_index + days_later) % 7 #the day we add , %7 turn back inside week
        
        new_day = in_week[new_day_index]

        new_time += f', {new_day}'
        print(new_time)
    
    if days_later == 1:
        new_time += ' (next day)' 
    if days_later > 1:
        new_time += f' ({days_later} days later)'
    print(new_time)


    return new_time

add_time('2:59 AM', '24:00', 'saturDay')
    # '5:42 PM, Monday'