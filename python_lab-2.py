	ornek - 1

number = input("Please enter a number: ")
sum = 0
while not number.isnumeric():
   print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
   number = input("Please enter a number: ")
if number.isnumeric():
   for i in range(len(number)):
        sum += int(number[i])**len(number)
   if  sum == int(number):
        print("{} is an Armstrong number".format(int(number)))
   else:
       print("{} is not an Armstrong number".format(int(number)))




https://github.com/HasanKaval?tab=repositories
https://github.com/HasanKaval/Assignment_1_Python.git
