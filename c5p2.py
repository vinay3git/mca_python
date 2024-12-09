import datetime as d

print("current date and time :", d.datetime.now())
print("current year :", d.datetime.now().year)
print("current month :", d.datetime.now().strftime("%B"))
print("current week number :", d.datetime.now().strftime("%V"))
print("day of the year :", d.datetime.now().strftime("%j"))
print("day of the month :", d.datetime.now().day)
print("day of the week :", d.datetime.now().strftime("%A"))
