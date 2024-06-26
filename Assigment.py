# read me - 
#in the 1st code we are converting the text to list and removing 
#the last 2 letters from the word. And then we are reversing the rest of the word.
x=list('python')
del x[4:]
x.reverse()
output=''.join(x)
print(output)

#in the code 2 we are simply giving 2 input values to x and y. and performing various arthametic operations.
x = int(input("enter 1st digit"))
y = int(input("enter 2nd digit")) 

z = (x+y, x-y, x*y, x//y, x/y)
print(z)

#in code 3 we are  using replace inbuilt function to replace the word python with pythons. and printing it at the end
x = 'i love playing with python'
y = x.replace('python','pythons')
print(y)

#in code 4 we are we defing the grade based on the marks. we can see if the marks are above 90 then grade is A.....vice versa
marks=int(input("input marks  "))
if marks >=90:
  grade = 'A'
elif marks >=80:
  grade = 'B'
elif marks >=70:
  grade = 'C'
elif marks < 70:
  grade = 'F'

print(grade)
