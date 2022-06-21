from datetime import date
from datetime import timedelta


def dates(arg):
    today=date.today()
    i=int(arg)
    
    if i==1:
        return today
    elif i==2:
        return today-timedelta(days=1)
    else:
        listt=[]
        j=0
        while(j<i):
            listt.append(today-timedelta(days=j))
            j+=1
        return listt
