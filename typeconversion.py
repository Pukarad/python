#conversion DOB into age
birth_year = input('enter your birth year: ')
print(type(birth_year)) #shows the class of veriable i.e. int or float or string or boolen
age = 2020 - int(birth_year) #int converts string to integr veriable
print(type(age))
print(age)
#exercise
wt_pound= input ('enter your weight is pounds: ')
wt_kg = 0.45 * int(wt_pound)
print('age of a person from pounds to kilogram is',wt_kg)