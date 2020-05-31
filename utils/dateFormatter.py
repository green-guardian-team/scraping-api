from datetime import datetime

def formatDateWHO(date):
    dateText = str(date.text).strip("\n")
    d = datetime.strptime(dateText, '%d %B %Y')
    
    return str(d.strftime('%Y-%m-%d'))