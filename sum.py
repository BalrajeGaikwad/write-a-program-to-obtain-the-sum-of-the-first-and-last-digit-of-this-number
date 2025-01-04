#If a four-digit number is input through the keyboard, write a program to obtain the sum of the first and last digit of this number.

a=int(input("Enter the four digit number :- "))

num=a//1000
print(num)
num2=a%10
print(num2)

sum=num+num2
print("The sum of first and last digit is :-", sum)