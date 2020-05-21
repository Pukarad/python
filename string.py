intro_1 = "Pukar, it's my name" # we use " if we have to use ' inside a veriable
intro_2 = 'i live in "Kharibot"' # we use ' if we have to use " inside a veriable
intro_3 = '''hello and namaste,
I'am from "Gorkha, Nepal".
it's my pleasurre to learn python programming.''' #we use ''' if we have to enter multiple line in as veriable
print(intro_1[2]) #we use [] to print a specific character in output
print(intro_2[-6]) #number that starts from beginning is o and from last is -1
print(intro_2[3:9]) # we use : to determine a range of a character excluding last character ans work as a mid operator of a QBASIC
print(intro_2[3:]) # if we didin't define end then it will print from initial defined character to last
print (intro_2[:7]) # if we didn't define start then it will print from initial to defined character
copyintro_2 = intro_2[:] # this will copy ie will assume the initial and final as start and ending of a veriable
print(copyintro_2)
print(intro_3)
#exercise
print(intro_2[3:-2]) #it works same as mid operator