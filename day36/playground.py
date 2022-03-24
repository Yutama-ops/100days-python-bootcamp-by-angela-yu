import datetime as dt

date = dt.datetime.now()
d = date.isoformat()
weekday = date.weekday()
today_date = d.split("T")[0]
print(type(today_date))
print(weekday)


def weekdate(today_date):
    now_date = date.fromisoformat(today_date)
    now_date_day = now_date.day
    now_date_weekday = now_date.weekday()
    if now_date_weekday < 5:
        now_date_day = now_date.day
        news_date = now_date_day
    elif now_date_weekday == 6:
        now_date_day = now_date.day
        news_date = now_date_day - 1
    elif now_date_weekday == 7:
        now_date_day = now_date.day
        news_date = now_date_day - 2
    return news_date
