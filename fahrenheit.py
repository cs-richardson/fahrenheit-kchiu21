#take user input to get Celsius, added float to make it only work for number inputs
c = float(input("Enter the temperature in Celsius: "))

#equation to convert celcius to farenheit, also it rounds the number so we don't get decimals
f = round((9/5) * c) + 32

#print out answer, and also added the degrees the symbol
print ('Degrees in farenheit is: ',f,'º')
