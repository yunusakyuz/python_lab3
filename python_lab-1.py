
    ornk
line = 10
print()
for i in range(line):
    print(' '*16+' '*19+'*'*12+' '*7+'*'*12+' '*7+'*'*(line-1-i)+'*'*(3*i+1))
for i in range(line*2-7):
    print(' '*(line+5-i)+'*'*(i+1)+'*'*12+' '*7+'*'*12+' '*7+'*'*12+' '*7+'*'*12)
for i in range(5):
    print(' '*16+'*'*19+'*'*19+'*'*12+' '*7+'*'*12)

  	ornek

price = 200
hälfte_price = 100
saved_amount = int(input('enter saved_amount'))
if saved_amount <= hälfte_price :
    print('You must save more, keep saving!')
elif hälfte_price < saved_amount < price :
    print('You saved more than half, keep saving!')
else :
    print('Yippee! You can buy your PS$')


 ornek - 1

names = ['susan', 'tom', 'edward']
mood = ['happy', 'sad']
for i in names:
    for ii in mood:
        print(f"{i} is {ii}")

   ornek - 2

a=range(1,10)
b=range(1,10)
for x,y in zip(a,b):
    print(str(x)*y)

  ornek - 3

a = range(10)
for i in a:
    print(i * str(i))

  ornek - 4

number =list(range(1,10))
for i in number:
    i_len= i
    i_strint=str(i)
    print(i_strint*i_len)

  ornek - 5

c=int(input("how many times should I write:"))+1
for i in range(c):
        print(str(i)*i)

   ornek - 6

given_nr = int(input("Enter a number : "))
for i in range(1, given_nr+1):
    print(i * str(i))

   ornek - 7

a=["1","2","3","4","5","6","7","8","9"]
b=range(1,10)
for x,y in zip(a,b):
    print(x*y)

   ornek - 8

a=["1","2","3","4","5","6","7","8","9"]
b=range(1,10)
for x,y in zip(a,b):
    print(x*y)
ornek - 9

exp_numbers = [12, 75, 77, 82, 4, 79, 88, 441, 73, 49, 87]
count = 0
evens = 0
odds = 0
while count < (len(exp_numbers)) :
    if not exp_numbers[count] % 2 == 0:
        evens +=1
    else :
        odds += 1
    count +=1
print(evens)
print(odds)

   ornek - 10

cift = 0
tek = 0
l = [11, 2, 24, 61, 48, 33, 3]
for i in l:
    if i%2== 0:
        cift = i+1
    else:
        tek = i + 1
print(cift)
print(tek)



list = [11, 36, 24, 61, 48, 33, 3]
even = 0
odd = 0
for i in list:
    if i %2 == 0:
        even += 1
    else:
        odd += 1
print ("The number of evens : ", even)
print ("The number of odds : ", odd)


evens = []
odds = []
for i in range(9):
    if i%2 == 0:
        evens.append(i)
    elif i%2 != 0:
        odds.append(i)
print(evens)
print(odds)


   ornek - 11

print(list(range(0,10,2)))
print(list(range(1,10,2)))

text = ['one', 'two', 'three', 'four', 'five']
numbers = [1, 2, 3, 4, 5]
klm = [11, 22, 33, 44, 55]
for x, y, z in zip(text, numbers, klm):
    print(x, ':', y, ':', z)

letters = ['a','b','c','d']
numbers = list(range(1,5))
for i,y in zip(letters,numbers):
    print(i,y)

