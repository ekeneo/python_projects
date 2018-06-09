# To write a program that prompts the user for hours and rate per hour to compute expected pay.
# Also compute the pay if the employee gets 0.5 times the hourly rate
# for hours worked above 40hoursself.

sh = input('Enter hours: ')
sr = input('Enter rate per hour: ')
try:  # to mitigate a traceback error that may occur if the user enters an input that is not numeric.
    fh = float(sh)  # to convert the input numeric string to a float.
    fr = float(sr)
except:
    print('Error, please enter numeric input')
    quit()  # to end the program/restart if an error occurs.

if fh > 40 :
    print('Overtime')
    reg = fr * fh  #for regular pay
    otp = (fh - 40.0) * (fr * 0.5)  # for Overtime
    print('regular pay:',reg,'overtime extra:',otp)
    xp = reg + otp  #for expected pay
else :
    print('Regular')
    xp = fh * fr
print('Expected pay: ', xp)
