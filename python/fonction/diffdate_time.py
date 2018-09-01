import datetime
##formatdate = "%m/%d/%Y"
##you can get more information on class date here :
#https://docs.python.org/3/library/datetime.html
def diffDate(date1,date2):
    firstday = datetime.date(date1)
    seconday = datetime.date(date2)
    diff = firstday - seconday
    diff.days
    return
