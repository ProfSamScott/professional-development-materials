""" Solution to exercise 2.4 #3 from section 2.12 of the textbook
Sam Scott, 2016"""

timeout = 6+52/60           # time in hours
easypace = 8/60+15/60/60    # converts 8 mins, 15 seconds to hours
tempo = 7/60+7/60/70        # converts 7 mins 12 seconds to hours

timein = timeout + easypace*2 + 3*tempo # compute the new time in hours

hours = int(timein)         # using int to drop the decimal on the hours
mins = (timein-hours)*60    # compute the minutes
mins = int(mins)            # drop the decimal

print("I get back at ",hours,":",mins,".",sep="")
