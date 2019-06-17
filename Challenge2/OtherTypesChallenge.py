import datetime as dt

def ShowSomeDates():
    now = dt.datetime.now()
    bday = dt.datetime(1963, 6, 9)
    atWork = dt.time(6, 0, 5)
    age = (now - bday).days // 365

    print(f"now = {now}")
    print(f"bday = {bday}")
    print(f"atWork = {atWork}")
    print(f"age = {age}")