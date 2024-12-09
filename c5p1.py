import calendar

year=int(input("enter the year :"))
if calendar.isleap(year):
        print(f"{year} is a leap year")
else:
        print(f"{year} not a leap year")

