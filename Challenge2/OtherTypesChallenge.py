import datetime as dt

def ShowSomeDates():
    now = dt.datetime.now()
    bday = dt.datetime(1963, 6, 9)
    atWork = dt.time(6, 0, 5)

    print(f"now = {now}")
    print(f"bday = {bday}")
    print(f"atWork = {atWork}")

def GetAge(dob):
    return (dt.datetime.now() - dob).days / 365.25

def DivideTest(numerator, denominator):
    try:
        div = numerator / denominator
        return div
    except Exception as ex:
        print(f"Division Error: {ex}")
