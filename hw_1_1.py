from datetime import datetime
def get_days_from_today(date):
    try:
        string_date = '2020-10-09'
        datetime_date = datetime.strptime(string_date, "%Y-%m-%d")
        print (datetime_date)
        datetime_today = datetime.today()
        print (datetime_today)
        number_day = (datetime_today - datetime_date).days 
        return (number_day)
    except ValueError:
        return ('Input format date Year-momth-day')

print (get_days_from_today('2020-10-10'))