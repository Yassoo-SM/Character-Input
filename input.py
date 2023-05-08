from datetime import date
name=input("enter your name:")
print ("Your name is "+name)
age=int(input("enter your age: "))
print ("Your age is "+str(age))
#today=date.today().year
#print ( "today is "+(str(date.today())))
print(f'you get 100 years in year {date.today().year+(100-int(age))} ')