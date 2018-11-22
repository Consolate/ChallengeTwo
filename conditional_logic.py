#this is input
year=eval(input ('Enter your year of birth:'))
 #this is a variable
current_year=int(2018)
age = current_year-year

if age<18:
    print('you are a minor')

elif age == 18  and age <=36:
    print('you are a youth')
else:
    print('You are an adult')

