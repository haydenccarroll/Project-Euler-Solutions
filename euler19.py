def is_leap_year(year): 
  if year % 4 != 0: 
    return False 
  if year % 100 == 0 and year % 400 != 0:
    return False
  return True


def sundays_in_a_month(starting_day, days_in_month): 
  sundays = 0 if starting_day % 7 != 0 else 1
  for i in range(days_in_month):
    #print(i + starting_day, 'i + starting_day')
    if i == days_in_month-1:
      new_starting_day = ((i + starting_day) % 7) + 1 #isnt right
  return sundays, new_starting_day
#new starting day6 is correct but some logic for deciding if you get an extra sunday is off

list_of_months = [31,28,31,30,31,30,31,31,30,31,30,31]
sundays = 0

starting_day = 2
for year in range(1900,1901):
  for month in range(0, 12):
    if month == 1 and is_leap_year(year):
      starting_day = sundays_in_a_month(starting_day, 29)[1] 
    else: 
      days_in_month = list_of_months[month]
      starting_day = sundays_in_a_month(starting_day, days_in_month)[1]
    print(month+1, starting_day)    

i = 0
for year in range(1901, 2001): 
  starting_sundays = sundays
  for month in range(0, 12):
    if month == 1 and is_leap_year(year):
      sundays += sundays_in_a_month(starting_day, 29)[0]
      starting_day = sundays_in_a_month(starting_day, 29)[1]
    else: 
      days_in_month = list_of_months[month]
      sundays += sundays_in_a_month(starting_day, days_in_month)[0]
      starting_day = sundays_in_a_month(starting_day, days_in_month)[1]
  #print(year, sundays - starting_sundays, sundays)
  if sundays - starting_sundays == 53:
    i = i+1
    print(year, i)
  elif sundays - starting_sundays != 52:
      print(year, i, sundays-starting_sundays)

    #print(month+1, sundays, starting_day)
print(sundays)
