import datetime

def time():
    now = datetime.datetime.now()
    t = now.strftime("%H:%M:%S")
    print(t)