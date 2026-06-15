# 1. Convert the time entered in hh,min and sec into seconds.

###Take input from user
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))
###Perform Operation
total_sec = hours * 3600 + minutes * 60 + seconds

print(f'Total seconds in {hours} hrs,{minutes} minutes & {seconds} seconds is {total_sec}')
