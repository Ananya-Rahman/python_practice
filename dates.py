import datetime

# x= datetime.datetime.now()  getting current time now
# print(x.year)
# print(x.strftime("%A"))

###Display this month ##
# x= datetime.datetime(2020, 6 , 20)
# print(x.strftime("%B"))
#### Age calculate ###
year = datetime.datetime.now().year #now getting current year

birth_year = int(input("Enter your birth year: "))

print ("I am %i years old!" % (year - birth_year))











