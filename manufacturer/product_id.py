
from datetime import datetime
def Product(name):
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    return str(name[0]).upper()+str(day)+str(month)+str(year)


