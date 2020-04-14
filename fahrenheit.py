#Converting from fahrenheit to celcius

print("THIS PROGRAM CONVERTS CELSIUS TO FAHRENHEIT")
try:
    command= int(input("Enter Your Celsius:>>> "))

    formula= ((command-32) * 5)/9

    print("Answer: % d C" % formula)

except:
    print("Check your Input.. Numbers Only")
