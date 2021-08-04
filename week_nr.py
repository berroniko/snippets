import datetime

# datetime.date.isocalendar() is an instance-method returning a tuple containing year, weeknumber and weekday in respective order for the given date instance
# https://stackoverflow.com/questions/2600775/how-to-get-week-number-in-python

hoy=datetime.date.today()
print("date today: ", hoy)

hoy_string = hoy.strftime("%d.%m.%Y")
print("date today: ", hoy_string)

week_nr = hoy.isocalendar()[1]
print("we have week nr", week_nr)

#alternative way
week_nr2 = hoy.strftime("%V")
print("we have week nr", week_nr2)
