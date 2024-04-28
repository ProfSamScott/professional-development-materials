"""Solution to exercise 2. The print_current_time() is a little tricky!
Sam Scott, January 2015"""
def print_time(seconds):
    """Format the time nicely given the number of seconds since midnight"""
    hours = seconds // 3600
    seconds = seconds % 3600
    minutes = seconds // 60
    seconds = seconds % 60
    if hours < 10:
        print('0',end='',sep='')
    print(hours,':',end='',sep='')
    if minutes < 10:
        print('0',end='',sep='')
    print(minutes,':',end='',sep='')    
    if seconds < 10:
        print('0',end='',sep='')
    print(seconds,sep='')        
    
def print_current_time_utc():
    """prints the current UTC time"""
    import time
    seconds = round(time.time())
    # get remainder after dividing by num seconds in a day
    seconds = seconds % (60*60*24) 
    print_time(seconds)

def print_current_time():
    """prints the current EST time"""
    import time
    seconds = round(time.time())
    # we're behind UTC by 5 hours so subtract that many seconds
    seconds = seconds - 5*60*60 
    # get remainder after dividing by num seconds in a day
    seconds = seconds % (60*60*24)
    print_time(seconds)